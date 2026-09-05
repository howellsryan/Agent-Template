#!/usr/bin/env python3
"""Print a consumer lock from a clean, committed Agent-Template checkout."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
if subprocess.check_output(["git", "-C", str(root), "status", "--porcelain"], text=True).strip():
    sys.exit("Commit and validate the distribution before generating a consumer lock")
revision = subprocess.check_output(["git", "-C", str(root), "rev-parse", "HEAD"], text=True).strip()
profile = json.loads((root / "profiles/engineering.json").read_text())
lock = {
    "version": 1,
    "bootstrap": {
        "revision": revision,
        "sha256": hashlib.sha256((root / "scripts/install_skills.py").read_bytes()).hexdigest(),
    },
    "sources": [{
        "repository": "howellsryan/Agent-Template",
        "revision": revision,
        "skills": {p.name: str(p.relative_to(root)) for p in sorted(
            (root / "plugins/engineering-workflow/skills").iterdir()) if (p / "SKILL.md").is_file()},
    }, *profile["sources"]],
}
print(json.dumps(lock, indent=2))
