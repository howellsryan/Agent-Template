# Agent Template Catalogue

A lightweight index of the agent skills, rules, and workflow helpers used across my repositories.

**This repo is a catalogue, not a vendor mirror.** Do not copy third-party `SKILL.md` files into this repository. Each card explains what a skill does, where its canonical source lives, where I currently use it, and how to fetch the latest version when I need it.

## Layout

```text
catalog/
├── workflow-hygiene/       # planning, scope, debugging, verification, writing hygiene
├── ui-ux/                  # visual design and interface review
├── frontend-engineering/   # React/component architecture and performance
├── threejs/                # Three.js reference skills
├── project-specific/       # recipes that only make sense in one of my products
├── rules/                  # pointers to project rule systems, not copied rule bodies
└── helpers/                # token/context and skill-authoring references
```

Start with [`SKILLS.md`](SKILLS.md) for the complete inventory or [`catalog/README.md`](catalog/README.md) for the catalogue rules.

## Repository audit

| Repository | Agent material found | Catalogue impact |
| --- | --- | --- |
| `3site` | 5 external UI/frontend skills under `.claude/skills/` | Vercel, Anthropic-style frontend design, UI/UX Pro Max |
| `chat` | shared workflow/hygiene skills plus `frontend-design` and `web-design-guidelines` | confirms the portable shared set |
| `pitch` | `delivery-loop`, `plan-gate`, `scope-fence`, `systematic-debugging`, `verification-before-completion`, `memory-hygiene` | shared delivery/debugging set |
| `footy-sim` | `delivery-loop`, `plan-gate`, `scope-fence`, `memory-hygiene` referenced by the contributor guide | shared lightweight set |
| `pocketRPG` | shared workflow skills, 4 project-native recipes, 10 vendored Three.js references, extensive path-scoped rules | biggest source of first-party recipes and 3D references |
| `career-catalogue` | contributor guide, no root `.claude/skills` catalogue found | no skill card added |
| `companion`, `ordermate` | no root `CLAUDE.md`/`SKILLS.md` inventory found in this audit | no skill card added |

## Rules of this repository

1. **Reference, never vendor.** External skill bodies stay upstream.
2. **Prefer canonical upstream links.** A local copy is listed only to show where I use or adapted it.
3. **One card per skill.** Bundles still get one card per skill so they are easy to browse.
4. **Keep project-native recipes separate.** They point back to the product repo that owns them.
5. **Refresh before copying.** Use the source link or install command on the card instead of copying an old local version from another project.
