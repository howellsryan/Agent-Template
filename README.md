# Agent Template Catalogue

A curated open-source map of useful Agent Skills, rules, helpers, skill repositories, and reusable agent workflows.

The goal is simple: **make good agent resources easy to rediscover without turning this repository into a stale copy of everybody else's work.**

## Start here

| I want to… | Go to |
| --- | --- |
| Browse specific skills | [`SKILLS.md`](SKILLS.md) |
| Discover prominent upstream skill repositories | [`catalog/sources/README.md`](catalog/sources/README.md) |
| Install the first-party delivery workflow | [`bespoke/delivery-loop/INSTALL.md`](bespoke/delivery-loop/INSTALL.md) |
| Understand how this catalogue is maintained | [`CONTRIBUTING.md`](CONTRIBUTING.md) |
| Review a catalogue change before publishing | [`bespoke/catalog-review/README.md`](bespoke/catalog-review/README.md) |

## Two zones, two rules

### `catalog/` — external references only

Third-party implementations stay upstream. Catalogue cards explain what a resource is, why it is useful, where the canonical source lives, and how to get the current version when relevant.

This keeps attribution clear and avoids freezing old copies of external `SKILL.md` files, scripts, rules, datasets, or licences in this repository.

### `bespoke/` — original reusable assets

First-party workflows created and maintained here may live in full so they can be copied as coherent packages. Each package documents its provenance, install shape, dependencies, and portability assumptions.

Current packages:

- [`delivery-loop`](bespoke/delivery-loop/README.md) — single-session Plan → Build → Code Review → Verify delivery discipline.
- [`catalog-review`](bespoke/catalog-review/README.md) — independent open-source/catalogue review agent and checklist.

## Layout

```text
catalog/
├── workflow-hygiene/       # individual external workflow/debugging skills
├── ui-ux/                  # individual UI/UX skill references
├── frontend-engineering/   # individual frontend skill references
├── threejs/                # individual Three.js skill references
└── sources/                # prominent upstream libraries, standards and indexes

bespoke/
├── delivery-loop/          # full first-party delivery workflow
└── catalog-review/         # full first-party review agent
```

## Research, not a leaderboard

There is no reliable public installation counter shared across Claude Code, Codex, Cursor, Copilot, Gemini CLI and other Agent Skills consumers. The source research therefore records **prominent repositories**, using live GitHub adoption signals, current activity, official ownership and specialist usefulness as evidence.

It is deliberately dated and non-exhaustive. GitHub stars are useful evidence, not usage telemetry, and mutable popularity numbers are not duplicated across source cards.

## Licensing

The original material in this repository is released under the repository's [MIT License](LICENSE).

External catalogue entries are links and summaries only. Their authors retain ownership and their own licences apply if you copy or install anything from upstream. Always check the upstream licence and documentation before redistributing third-party material.

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md). The short version: verify the canonical source, do not vendor third-party bodies, keep mutable research in one dated place, and run the `catalog-review` checklist before proposing a catalogue change.
