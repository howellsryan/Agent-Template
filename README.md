# Agent Template Catalogue

An open-source catalogue for useful agent skills, rules, helpers, and agentic workflow patterns.

The repository has two deliberately different zones:

- **`catalog/` — external references only.** Third-party implementations stay in their upstream repositories. Cards explain what a resource does, where the canonical source lives, and how to find the current version.
- **`bespoke/` — first-party reusable assets.** Original workflows created for this catalogue may live here in full, including their supporting files, so they can be copied into another project as a coherent package.

## Layout

```text
catalog/
├── workflow-hygiene/       # individual external workflow/debugging skills
├── ui-ux/                  # individual UI/UX skill references
├── frontend-engineering/   # individual frontend skill references
├── threejs/                # individual Three.js skill references
└── sources/                # prominent upstream skill repositories and ecosystem indexes

bespoke/
└── delivery-loop/          # full first-party single-session delivery workflow
```

Start with [`SKILLS.md`](SKILLS.md) for the human-readable inventory. The current ecosystem research and ranking methodology lives in [`catalog/sources/README.md`](catalog/sources/README.md).

## Repository rules

1. **Never vendor external skill bodies.** External `SKILL.md`, scripts, nested rules, datasets, and licence files remain upstream.
2. **Canonical sources only.** External cards point to the original/current upstream repository, not a downstream project copy.
3. **Bespoke means genuinely first-party.** Full content is allowed under `bespoke/` only for original reusable material maintained by this repository owner; adapted external material must retain clear provenance or remain a pointer.
4. **Research is dated.** Stars, forks, and activity are discovery/adoption proxies, not exact installation counts. Re-check live GitHub before treating a ranking as current.
5. **Prefer useful structure over mirrors.** Very large repositories get a source card and upstream browse link rather than hundreds of stale copied skill summaries.
