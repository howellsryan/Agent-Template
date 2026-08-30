# Agent Template Catalogue

A lightweight, open-source catalogue of **external** agent skills, rules, and helpers that are useful enough to keep bookmarked for future projects.

**This repository is a reference index, not a vendor mirror.** It does not store third-party skill bodies or copies from other projects. Each card gives a short explanation, the canonical upstream GitHub source, and the quickest route to the latest version.

## Layout

```text
catalog/
├── workflow-hygiene/       # debugging and completion discipline
├── ui-ux/                  # visual design and interface review
├── frontend-engineering/   # React/component architecture and performance
└── threejs/                # Three.js reference skills
```

Start with [`SKILLS.md`](SKILLS.md) for the complete inventory or [`catalog/README.md`](catalog/README.md) for the catalogue conventions.

## Rules

1. **External sources only.** A catalogue entry must point to a repository maintained outside this repository owner’s projects.
2. **Reference, never vendor.** Do not copy `SKILL.md`, nested rules, scripts, data, or licences into this repository.
3. **Canonical upstream links only.** Do not point cards at local forks, adaptations, or downstream copies.
4. **One card per useful skill.** Bundles are split into individual cards so they are easy to browse by purpose.
5. **Refresh from upstream.** When using a skill, follow its source link and take the current version rather than relying on an old copied implementation.
6. **No project provenance.** The catalogue intentionally does not record which private or public projects happen to use a skill.
