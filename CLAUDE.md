# CLAUDE.md — Agent Template Catalogue

## Purpose

This repository is a **reference catalogue** for agent skills, rules, and workflow helpers used across my projects. It is not the runtime source for third-party skills and must not become a vendor mirror.

## Non-negotiables

- Never add a third-party `SKILL.md` body here. Add or update a short card in `catalog/` instead.
- Every external card must link to the canonical GitHub source and say how to fetch/install the latest version.
- Every first-party card must point to the repository/file that currently owns the implementation.
- Mark adaptations clearly: upstream source and local adapted source are different things.
- `SKILLS.md` is the top-level human inventory. Keep it in sync with cards.
- Project-specific path-scoped rules belong in their product repos. This catalogue stores pointers only.

## Card format

Each card should contain: **What it does**, **Type**, **Canonical source**, **Used in**, **Get the latest**, and optional **Notes**. Keep cards short; do not reproduce implementation instructions.

## Categories

- `catalog/workflow-hygiene/` — delivery, planning, scope, memory, writing, debugging, verification.
- `catalog/ui-ux/` — interface design and review.
- `catalog/frontend-engineering/` — React/component/performance guidance.
- `catalog/threejs/` — Three.js reference bundle cards.
- `catalog/project-specific/` — product-owned recipes.
- `catalog/rules/` — pointers to rule systems.
- `catalog/helpers/` — context/token/authoring helpers.

## Updating

Before adding a new external card, verify the upstream repository still exists and prefer its main branch/release instructions. If a project stops using a skill, update the card's `Used in` list; do not delete the card solely because one repo removed it if it remains part of my working toolkit.
