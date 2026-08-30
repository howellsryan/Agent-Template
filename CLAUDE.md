# CLAUDE.md — External Agent Resource Catalogue

## Purpose

This repository is a **pointer-only catalogue of external agent skills, rules, and helpers**. It exists to make useful upstream resources easy to rediscover without vendoring their implementations.

## Non-negotiables

- Only catalogue resources whose canonical source is an external repository.
- Never add copied third-party `SKILL.md` bodies, nested rules, scripts, datasets, or licence files.
- Never use a downstream/local project as a source link or record where a resource is used.
- Every card must link directly to the canonical upstream GitHub repository or skill path.
- `SKILLS.md` is the top-level inventory and must stay in sync with `catalog/`.
- If provenance is uncertain, omit the card until the upstream source is verified.

## Card format

Each card should contain:

- **What it does** — one short practical summary.
- **Source** — canonical GitHub repository/skill path.
- **Get the latest** — how to obtain the current upstream version.
- **Notes** — optional upstream-specific detail only.

Do not include “used in”, local-copy, fork, adaptation, or project-history fields.

## Categories

- `catalog/workflow-hygiene/` — externally sourced workflow/debugging disciplines.
- `catalog/ui-ux/` — interface design and review resources.
- `catalog/frontend-engineering/` — React/component/performance guidance.
- `catalog/threejs/` — Three.js reference skills.

## Updating

Before adding or refreshing a card, verify the upstream repository and path still exist. Prefer a stable upstream install command when the project documents one; otherwise link the source and instruct the reader to fetch the current skill directory from upstream.
