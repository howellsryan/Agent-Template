# CLAUDE.md — Agent Resource Catalogue

## Purpose

This repository is a curated catalogue of external Agent Skills resources plus a small `bespoke/` area for original reusable agent workflows maintained here.

## Boundaries

### `catalog/` — external pointer-only

- Never copy third-party `SKILL.md` bodies, scripts, reference folders, rules, datasets, or licence files into `catalog/`.
- Every card links to a canonical external GitHub source.
- Do not record downstream/private project usage or local copies.
- Large libraries belong under `catalog/sources/` as repository cards; individual skills worth bookmarking may also have cards in the functional category folders.
- Dated adoption research must state that stars/forks/activity are proxies, not exact usage counts.

### `bespoke/` — original full assets

- Full files are allowed only for first-party material intentionally published as reusable open-source agent infrastructure.
- Each bespoke package needs a README explaining provenance, install shape, dependencies, and which files are essential vs optional.
- If a bespoke workflow depends on an external skill, link upstream instead of copying it unless licence/provenance and the reason for vendoring are explicit.
- Keep bespoke packages portable: remove product-specific paths, commands, section numbers, and domain invariants unless the package is explicitly domain-specific.

## Inventory

- `SKILLS.md` is the top-level human index.
- `catalog/README.md` defines reference-card conventions.
- `catalog/sources/README.md` contains the current ecosystem research snapshot.
- `bespoke/delivery-loop/` is the canonical first-party delivery workflow in this repository.

## Updating

Before adding an external source, verify that the upstream repository still exists, is active enough to be useful, and is actually a skill library/standard/index rather than a coincidental search match. Before changing a bespoke package, keep its README, skill files, companion files, and install instructions consistent in the same change.
