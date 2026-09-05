import copy
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

SPEC = importlib.util.spec_from_file_location("installer", Path(__file__).parents[1] / "scripts/install_skills.py")
installer = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(installer)


class InstallTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.project = self.base / "project with spaces"
        self.project.mkdir()
        self.source = self.base / "source"
        for name in ["delivery-loop", "plan-gate"]:
            skill = self.source / "skills" / name
            skill.mkdir(parents=True)
            (skill / "SKILL.md").write_text(f"---\nname: {name}\ndescription: Example\n---\nRead steps.md\n")
            (skill / "steps.md").write_text("Supporting resource\n")
        self.lock = {"version": 1, "sources": [{"repository": "owner/repo", "revision": "a" * 40,
                     "skills": {"delivery-loop": "skills/delivery-loop", "plan-gate": "skills/plan-gate"}}]}
        self.mock = patch.object(installer, "checkout", return_value=self.source)
        self.mock.start()
        self.addCleanup(self.mock.stop)

    def install(self, **kwargs):
        return installer.install(self.project, self.lock, **kwargs)

    def test_install_repeat_check_and_resources(self):
        self.assertEqual(self.install(), 2)
        for location in [".agents", ".claude"]:
            self.assertEqual((self.project / location / "skills/delivery-loop/steps.md").read_text(), "Supporting resource\n")
        self.assertEqual(self.install(), 2)
        self.assertEqual(self.install(check=True), 2)

    def test_unmanaged_skill_preserved(self):
        local = self.project / ".claude/skills/local-feature"
        local.mkdir(parents=True)
        (local / "SKILL.md").write_text("local")
        self.install()
        self.assertEqual((local / "SKILL.md").read_text(), "local")

    def test_collision_does_not_partially_install(self):
        local = self.project / ".claude/skills/plan-gate"
        local.mkdir(parents=True)
        (local / "SKILL.md").write_text("keep")
        with self.assertRaisesRegex(ValueError, "overwrite local"):
            self.install()
        self.assertFalse((self.project / ".agents/skills/delivery-loop").exists())
        self.assertEqual((local / "SKILL.md").read_text(), "keep")

    def test_update_removes_only_owned_stale_links(self):
        self.install()
        del self.lock["sources"][0]["skills"]["plan-gate"]
        with self.assertRaisesRegex(ValueError, "differ from lock"):
            self.install(check=True)
        self.assertEqual(self.install(), 1)
        self.assertFalse((self.project / ".claude/skills/plan-gate").is_symlink())

    def test_update_and_rollback_switch_both_paths_to_selected_source(self):
        self.install()
        second = self.base / "second-source"
        import shutil
        shutil.copytree(self.source, second)
        (second / "skills/delivery-loop/steps.md").write_text("new revision")
        with patch.object(installer, "checkout", return_value=second):
            self.lock["sources"][0]["revision"] = "b" * 40
            self.install()
            for location in [".agents", ".claude"]:
                self.assertEqual((self.project / location / "skills/delivery-loop/steps.md").read_text(), "new revision")
            self.install(check=True)
        self.lock["sources"][0]["revision"] = "a" * 40
        self.install()
        self.assertEqual((self.project / ".agents/skills/delivery-loop/steps.md").read_text(), "Supporting resource\n")

    def test_later_download_failure_preserves_previous_install(self):
        self.install()
        state = (self.project / ".agents/skills-installed.json").read_bytes()
        self.lock["sources"].append({"repository": "another/repo", "revision": "b" * 40,
                                     "skills": {"debugging": "skills/debugging"}})
        with patch.object(installer, "checkout", side_effect=[self.source, OSError("download failed")]):
            with self.assertRaisesRegex(OSError, "download failed"):
                self.install()
        self.assertEqual((self.project / ".agents/skills-installed.json").read_bytes(), state)
        self.assertTrue((self.project / ".claude/skills/plan-gate").is_dir())

    def test_changed_link_is_not_overwritten(self):
        self.install()
        link = self.project / ".agents/skills/delivery-loop"
        link.unlink()
        link.symlink_to(self.source)
        with self.assertRaisesRegex(ValueError, "modified skill link"):
            self.install()
        self.assertEqual(link.resolve(), self.source.resolve())

    def test_missing_resource_does_not_change_existing_install(self):
        self.install()
        self.lock["sources"][0]["skills"]["plan-gate"] = "absent"
        with self.assertRaisesRegex(ValueError, "Missing SKILL"):
            self.install()
        self.assertTrue((self.project / ".claude/skills/delivery-loop").is_dir())

    def test_missing_discovery_link_fails_check_then_repairs(self):
        self.install()
        (self.project / ".claude/skills/plan-gate").unlink()
        with self.assertRaisesRegex(ValueError, "differ from lock"):
            self.install(check=True)
        self.install()
        self.assertEqual(self.install(check=True), 2)

    def test_invalid_locks(self):
        for field, value in [("revision", "main"), ("repository", "--upload-pack=evil")]:
            lock = copy.deepcopy(self.lock)
            lock["sources"][0][field] = value
            with self.assertRaises(ValueError):
                installer.validate_lock(lock)
        for value in ["../outside", "/absolute", "skills/../outside", "skills//name"]:
            lock = copy.deepcopy(self.lock)
            lock["sources"][0]["skills"]["plan-gate"] = value
            with self.assertRaises(ValueError):
                installer.validate_lock(lock)

    def test_duplicate_skill_rejected(self):
        self.lock["sources"].append({"repository": "another/repo", "revision": "b" * 40,
                                     "skills": {"plan-gate": "skills/plan-gate"}})
        with self.assertRaisesRegex(ValueError, "duplicate skill"):
            self.install()

    def test_redirected_discovery_root_rejected(self):
        (self.project / ".claude").symlink_to(self.source, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "cannot be a symlink"):
            self.install()

    def test_external_resource_link_rejected(self):
        (self.source / "skills/plan-gate/outside").symlink_to(self.project, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "External resource"):
            self.install()

    def test_failed_link_write_rolls_back(self):
        self.install()
        original = (self.project / ".agents/skills-installed.json").read_text()
        original_targets = json.loads(original)
        self.lock["sources"][0]["skills"].pop("plan-gate")
        replace = os.replace

        def fail_state(source, destination):
            if str(destination).endswith("skills-installed.json"):
                raise OSError("simulated disk failure")
            return replace(source, destination)

        with patch.object(installer.os, "replace", side_effect=fail_state):
            with self.assertRaisesRegex(OSError, "disk failure"):
                self.install()
        self.assertEqual((self.project / ".agents/skills-installed.json").read_text(), original)
        for key, target in original_targets.items():
            self.assertEqual(os.readlink(self.project / key), target)

    def test_concurrent_install_rejected(self):
        (self.project / ".agents").mkdir()
        guard = self.project / ".agents/install.lock"
        guard.touch()
        with self.assertRaisesRegex(ValueError, "Another install"):
            self.install()
        self.assertTrue(guard.exists())


class CheckoutTests(unittest.TestCase):
    def test_immutable_checkout_rejects_wrong_revision_and_edits(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            installer.git("init", "--quiet", root)
            (root / "SKILL.md").write_text("original")
            installer.git("-C", root, "add", ".")
            installer.git("-C", root, "-c", "user.name=Test", "-c", "user.email=test@example.invalid",
                          "commit", "--quiet", "-m", "fixture")
            revision = installer.git("-C", root, "rev-parse", "HEAD")
            installer.verify_checkout(root, revision)
            with self.assertRaisesRegex(ValueError, "Wrong cached revision"):
                installer.verify_checkout(root, "0" * 40)
            (root / "SKILL.md").write_text("changed")
            with self.assertRaisesRegex(ValueError, "Modified cache"):
                installer.verify_checkout(root, revision)

    def test_missing_cache_check_never_fetches(self):
        with tempfile.TemporaryDirectory() as temporary:
            with patch.object(installer, "git") as call:
                with self.assertRaisesRegex(ValueError, "not installed"):
                    installer.checkout(Path(temporary), {"repository": "owner/repo", "revision": "a" * 40}, True)
                call.assert_not_called()


class BootstrapTests(unittest.TestCase):
    def test_corrupt_bootstrap_is_not_executed(self):
        import hashlib
        with tempfile.TemporaryDirectory() as temporary:
            project = Path(temporary)
            (project / "tools").mkdir()
            bootstrap = project / "tools/agent-skills.py"
            bootstrap.write_bytes((Path(__file__).parents[1] / "templates/agent-skills.py").read_bytes())
            cache = project / ".agents/cache/bootstrap"
            cache.mkdir(parents=True)
            digest = hashlib.sha256(b"expected").hexdigest()
            (cache / f"{digest}.py").write_text("raise RuntimeError('EXECUTED')")
            (project / ".agents/skills.lock.json").write_text(json.dumps({"bootstrap": {"revision": "a" * 40, "sha256": digest}}))
            result = subprocess.run(["python3", str(bootstrap), "--check"], text=True, capture_output=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("checksum mismatch", result.stderr)
            self.assertNotIn("EXECUTED", result.stderr)


if __name__ == "__main__":
    unittest.main()
