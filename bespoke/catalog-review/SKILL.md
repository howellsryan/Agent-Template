---
name: catalog-review
description: Use before publishing or merging changes to an open-source Agent Skills/resource catalogue, especially this repository. Independently review the actual diff for requirement fit, external provenance/licensing, current-research integrity, readability, installability, portability, maintenance cost and broken links/paths. Verify current upstream claims live; do not trust the author/PR summary as evidence.
---

# catalog-review: independent release gate

Review the change as if you did not author it.

Read the repository contract (`README.md`, `CONTRIBUTING.md`, agent instructions), then the actual diff and the relevant changed files. Use `checklist.md` for the full gate.

## Hard rules

- **Diff over narrative.** PR summaries describe intent; the diff proves reality.
- **Live state over remembered state.** Current external claims require a current upstream check.
- **Canonical upstream over mirrors.** Discovery indexes are not provenance.
- **Pointer-only means pointer-only.** No copied third-party bodies under an external catalogue.
- **One mutable fact, one home.** Popularity/adoption research belongs in one dated snapshot, not duplicated cards.
- **Install instructions must resolve after installation.** Test names, relative paths and companion references against the documented destination layout.
- **Reader first.** A new visitor should understand purpose, structure and the next action quickly without knowing the repository's history.

## Verdict

Return `READY`, `READY WITH NOTES`, or `NOT READY`, with findings ranked `BLOCKER`, `IMPORTANT`, `SUGGESTION`.

Each material finding states:

1. evidence/location;
2. concrete failure mode;
3. smallest sensible fix.

Finish with what was actually verified and anything that could not be checked.
