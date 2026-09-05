# AGENTS.md — Agent Resource Catalogue

## Purpose

This repository is a curated catalogue of external Agent Skills resources plus first-party review assets in `bespoke/` and an installable workflow marketplace in `plugins/`.

## Boundaries

### `catalog/` — external pointer-only

- Never copy third-party `SKILL.md` bodies, scripts, reference folders, rules, datasets, or licence files into `catalog/`.
- Every card links to a canonical external GitHub source.
- Do not record downstream/private project usage or local copies.
- Large libraries belong under `catalog/sources/` as repository cards; individual skills worth bookmarking may also have cards in functional folders.
- Mutable popularity metrics belong only in the dated research snapshot, never duplicated across source cards.
- Describe stars/forks/activity as adoption signals, not exact usage or installation counts.

### `bespoke/` and `plugins/` — original full assets

- Full files are allowed only for first-party material intentionally published as reusable open-source agent infrastructure, or material with explicit compatible provenance/licensing.
- Each bespoke package needs a README explaining provenance, install shape, dependencies, and which files are essential vs optional.
- External dependencies remain upstream pointers unless there is an explicit reason and licence basis for vendoring.
- Keep bespoke packages portable: remove product-specific paths, commands, section numbers, and domain invariants unless the package is explicitly domain-specific.
- Check that internal references still make sense after following the package's install instructions.

## Inventory

- `README.md` is the two-minute orientation.
- `SKILLS.md` is the top-level human inventory.
- `CONTRIBUTING.md` defines the contribution and research-refresh contract.
- `catalog/README.md` defines reference-card conventions.
- `catalog/sources/README.md` contains the dated ecosystem research snapshot.
- `plugins/engineering-workflow/skills/` is the canonical first-party workflow source.
- `docs/distribution.md` owns install, update and rollback instructions.
- `profiles/engineering.json` pins external dependencies; third-party bodies stay upstream.
- `bespoke/delivery-loop/` retains compatibility links only.
- `bespoke/catalog-review/` is the independent review agent for catalogue/open-source changes.

## Verification

Run `python3 -B scripts/validate_distribution.py` and `python3 -B -m unittest discover -s tests -v` before publishing. Keep the Codex and Claude plugin names/versions synchronized. Skill changes are made centrally; consuming repositories adopt explicit commits.

## Review gate

Before publishing or merging a material catalogue/bespoke change, run `catalog-review` against the actual diff. Current claims require fresh upstream evidence. The author's PR summary is context, not proof.

## Updating

Before adding an external source, verify that the upstream repository still exists, is useful, and is accurately classified. Before changing a bespoke package, keep its README, skill/agent files, companion files, dependencies, and install instructions consistent in the same change.
