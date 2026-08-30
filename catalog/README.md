# Catalogue conventions

`catalog/` is **external-source only**. It is pointer-first so this repository stays useful without becoming a stale vendor mirror.

## Individual skill cards

Functional folders (`workflow-hygiene/`, `ui-ux/`, `frontend-engineering/`, `threejs/`) contain small cards for specific skills worth bookmarking.

A card should answer:

- **What it does** — one practical summary.
- **Source** — the canonical upstream GitHub path.
- **Get the latest** — upstream install/fetch guidance when known.
- **Notes** — optional upstream-only detail.

## Source repository cards

`catalog/sources/` captures prominent skill libraries, specialist collections, standards, harnesses, helpers, and discovery indexes. Very large repositories get **one source card**, not hundreds of copied or hand-maintained skill cards.

Source cards describe the resource and its purpose. Mutable adoption metrics do not belong in individual cards; dated ecosystem research lives only in [`sources/README.md`](sources/README.md).

## What never belongs here

- copied external `SKILL.md` bodies;
- scripts, datasets, nested reference directories, rules, or licences copied from upstream;
- downstream/private project links or “used in” fields;
- first-party workflows (those belong under `bespoke/`);
- undated claims that a repository is “the most used”, “the biggest”, or otherwise permanently ranked.

See [`CONTRIBUTING.md`](../CONTRIBUTING.md) for the contribution checklist.
