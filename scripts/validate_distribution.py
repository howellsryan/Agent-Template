#!/usr/bin/env python3
"""Validate the repository's two manifests, skill entrypoints and local links."""
import json
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
plugin = root / "plugins/engineering-workflow"
codex = json.loads((plugin / ".codex-plugin/plugin.json").read_text())
claude = json.loads((plugin / ".claude-plugin/plugin.json").read_text())
assert codex["name"] == claude["name"] == plugin.name
assert codex["version"] == claude["version"] and re.fullmatch(r"\d+\.\d+\.\d+", codex["version"])
assert codex["skills"] == "./skills/"
assert (plugin / "LICENSE").read_bytes() == (root / "LICENSE").read_bytes()
for folder in [".agents/plugins", ".claude-plugin"]:
    marketplace = json.loads((root / folder / "marketplace.json").read_text())
    assert marketplace["name"] == "ryan-agents"
    assert len(marketplace["plugins"]) == 1
    entry = marketplace["plugins"][0]
    assert entry["name"] == plugin.name
    source = entry["source"]
    assert (source["path"] if isinstance(source, dict) else source) == "./plugins/engineering-workflow"
    if isinstance(source, dict):
        assert source["source"] == "local"
        assert entry["policy"] == {"installation": "AVAILABLE", "authentication": "ON_INSTALL"}
        assert entry["category"] == "Productivity"
skills = sorted((plugin / "skills").iterdir())
assert len(skills) == 4
for skill in skills:
    text = (skill / "SKILL.md").read_text()
    header = text.split("---", 2)
    assert len(header) == 3 and re.search(rf"^name: {skill.name}$", header[1], re.M), skill
    assert re.search(r"^description: .+", header[1], re.M), skill
    assert "[TODO:" not in text
assert (plugin / "skills/delivery-loop/steps.md").is_file()
# Root-level repository docs and actual package references must survive the move.
documents = [*root.glob("*.md"), *root.glob("bespoke/**/*.md"),
             *root.glob("plugins/**/*.md"), *root.glob("docs/**/*.md")]
links = 0
for document in documents:
    for target in re.findall(r"\]\(([^)\s]+)\)", document.read_text()):
        if ":" in target or target.startswith("#") or "<" in target:
            continue
        destination = target.split("#")[0]
        assert (document.parent / destination).exists(), f"Broken link: {document}: {target}"
        links += 1
print(f"Validated 2 plugin manifests, 2 marketplaces, {len(skills)} first-party skills and {links} local links")
