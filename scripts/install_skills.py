#!/usr/bin/env python3
"""Expose exactly the locked skills without vendoring them into the project."""
import argparse
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
import tempfile


def git(*args):
    env = dict(os.environ, GIT_TERMINAL_PROMPT="0")
    return subprocess.check_output(["git", *map(str, args)], env=env, text=True,
                                   stderr=subprocess.PIPE, timeout=120).strip()


def validate_lock(lock):
    if lock.get("version") != 1 or not lock.get("sources"):
        raise ValueError("Expected a version 1 lock with sources")
    names, repositories = set(), set()
    for source in lock["sources"]:
        repo, revision = source["repository"], source["revision"]
        if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repo):
            raise ValueError("Invalid GitHub repository")
        if repo in repositories or not re.fullmatch(r"[0-9a-f]{40}", revision):
            raise ValueError("Sources must be unique and pinned to full commit SHAs")
        repositories.add(repo)
        if not source.get("skills"):
            raise ValueError("Each source needs selected skills")
        for name, path in source["skills"].items():
            if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or name in names:
                raise ValueError("Invalid or duplicate skill name")
            names.add(name)
            parts = PurePosixPath(path)
            if parts.is_absolute() or ".." in parts.parts or "\\" in path or path != str(parts):
                raise ValueError("Skill paths must be normalized relative paths")
    return names


def verify_checkout(path, revision):
    if path.is_symlink() or git("-C", path, "rev-parse", "HEAD") != revision:
        raise ValueError(f"Wrong cached revision: {path}")
    # Include ignored/untracked files: caches are immutable, not working copies.
    if git("-C", path, "status", "--porcelain", "--untracked-files=all", "--ignored"):
        raise ValueError(f"Modified cache: {path}; preserve edits elsewhere before removing it")


def checkout(project, source, check):
    base = project / ".agents/cache/sources" / source["repository"]
    path = base / source["revision"]
    if not path.exists():
        if check:
            raise ValueError("Skills are not installed; run the repository bootstrap first")
        base.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(prefix="fetch-", dir=base) as temporary:
            stage = Path(temporary) / "source"
            git("init", "--quiet", stage)
            git("-C", stage, "fetch", "--quiet", "--depth=1",
                f"https://github.com/{source['repository']}.git", source["revision"])
            git("-C", stage, "checkout", "--quiet", "--detach", "FETCH_HEAD")
            verify_checkout(stage, source["revision"])
            stage.rename(path)
    verify_checkout(path, source["revision"])
    return path


def skill_path(root, relative, name):
    path = root / relative
    if not path.resolve().is_relative_to(root.resolve()) or path.is_symlink():
        raise ValueError(f"Skill escapes source checkout: {name}")
    if not (path / "SKILL.md").is_file():
        raise ValueError(f"Missing SKILL.md for {name}")
    for child in path.rglob("*"):
        if child.is_symlink() and not child.resolve().is_relative_to(root.resolve()):
            raise ValueError(f"External resource symlink in {name}: {child}")
    text = (path / "SKILL.md").read_text()
    header = text.split("---", 2)
    if len(header) != 3 or not re.search(rf"^name:\s*{re.escape(name)}\s*$", header[1], re.M):
        raise ValueError(f"Skill frontmatter name mismatch: {name}")
    return path


def read_state(path):
    if not path.exists():
        return {}
    state = json.loads(path.read_text())
    for key, target in state.items():
        if not re.fullmatch(r"\.(?:agents|claude)/skills/[a-z0-9]+(?:-[a-z0-9]+)*", key):
            raise ValueError("Invalid installer ownership record")
        if not isinstance(target, str):
            raise ValueError("Invalid installer link target")
    return state


def install(project, lock, check=False):
    validate_lock(lock)
    agents = project / ".agents"
    # Refuse directory redirection before writing any cache or discovery links.
    for relative in [".agents", ".agents/cache", ".agents/cache/sources", ".agents/skills",
                     ".claude", ".claude/skills"]:
        directory = project / relative
        if directory.is_symlink():
            raise ValueError(f"Managed directory cannot be a symlink: {relative}")
    agents.mkdir(exist_ok=True)
    guard = agents / "install.lock"
    try:
        descriptor = os.open(guard, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    except FileExistsError as error:
        raise ValueError("Another install is active; remove .agents/install.lock only if it was interrupted") from error
    os.close(descriptor)
    try:
        desired = {}
        for source in lock["sources"]:
            root = checkout(project, source, check)
            for name, relative in source["skills"].items():
                path = skill_path(root, relative, name)
                for discovery in [".agents/skills", ".claude/skills"]:
                    key = f"{discovery}/{name}"
                    desired[key] = os.path.relpath(path, project / discovery)
        state_file = agents / "skills-installed.json"
        if state_file.is_symlink():
            raise ValueError("Installer state cannot be a symlink")
        previous = read_state(state_file)
        # Preflight every collision before modifying any existing discovery path.
        for key in desired.keys() | previous.keys():
            path = project / key
            if path.is_symlink():
                if key not in previous or os.readlink(path) != previous[key]:
                    raise ValueError(f"Unmanaged or modified skill link: {key}")
            elif path.exists():
                raise ValueError(f"Refusing to overwrite local skill: {key}")
        if check:
            if previous != desired or any(not (project / key).is_symlink() or
                                           not (project / key).is_dir() for key in desired):
                raise ValueError("Installed skills differ from lock; rerun the bootstrap")
            return len(desired) // 2
        # Pre-test symlink support. Keep the old installation if the platform denies it.
        with tempfile.TemporaryDirectory(prefix="links-", dir=agents) as temporary:
            probe = Path(temporary) / "probe"
            probe.symlink_to(project, target_is_directory=True)
            backups = {}
            try:
                for key in desired.keys() | previous.keys():
                    path = project / key
                    backups[key] = os.readlink(path) if path.is_symlink() else None
                    path.parent.mkdir(parents=True, exist_ok=True)
                    if key in desired:
                        link = Path(temporary) / "next"
                        link.symlink_to(desired[key], target_is_directory=True)
                        os.replace(link, path)
                    elif path.is_symlink():
                        path.unlink()
                staged_state = Path(temporary) / "state.json"
                staged_state.write_text(json.dumps(desired, indent=2, sort_keys=True) + "\n")
                os.replace(staged_state, state_file)
            except BaseException:
                for key, target in backups.items():
                    path = project / key
                    if path.is_symlink():
                        path.unlink()
                    if target is not None:
                        path.symlink_to(target, target_is_directory=True)
                raise
        return len(desired) // 2
    finally:
        guard.unlink()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", type=Path, required=True)
    parser.add_argument("--check", action="store_true", help="Offline verification; never download")
    args = parser.parse_args()
    project = args.project.resolve()
    try:
        lock = json.loads((project / ".agents/skills.lock.json").read_text())
        count = install(project, lock, args.check)
        print(f"{'Verified' if args.check else 'Installed'} {count} pinned skills in both discovery paths")
    except (OSError, ValueError, KeyError, subprocess.SubprocessError) as error:
        print(f"Agent skills: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
