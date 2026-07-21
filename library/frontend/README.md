# Frontend — the part users actually touch

## What this distinction is

Frontend is where correctness meets human beings. The backend can be flawless and the product still broken because a spinner never resolved, a form couldn't be reached by keyboard, or global state re-rendered the world on every keystroke. These skills target the failures agents ship most often when building UI: **skipping the states that aren't the happy path**, **treating accessibility as a later audit instead of a build-time property**, and **putting state in the wrong place** so the app becomes a tangle of re-renders and prop-drilling.

They're framework-agnostic — React, Vue, Svelte, Solid, plain DOM. They encode *what a robust component accounts for*, not which library renders it.

## When to reach for these

- Building any view backed by fetched/async/remote data → **full-state-ui** (loading, error, empty, and data — all four).
- Building or modifying components, pages, forms, interactive elements → **accessible-by-default**.
- Adding or moving client state — component state, context, stores → **state-colocation**.

## When not to

- Non-UI code, build config, and internal debug tooling explicitly exempt from a11y.
- Pure visual/aesthetic decisions (color, spacing, hierarchy) — that's the [`design/`](../design/) category, not this one. This category is about *behaviour and structure*; design is about *looks*.

## Skills in this category

| Skill | Fires when | What it enforces |
|---|---|---|
| [`full-state-ui`](skills/full-state-ui/SKILL.md) | Any async/data-driven view | Design loading, error, empty, and populated states — not just success |
| [`accessible-by-default`](skills/accessible-by-default/SKILL.md) | Building/editing UI | Semantic HTML, keyboard operability, labels, visible focus, contrast — while building |
| [`state-colocation`](skills/state-colocation/SKILL.md) | Adding/moving client state | Keep state as local as possible; lift only when genuinely shared |

## Rules for this area (path-scoped)

A design-system or component-library directory is a strong candidate for a path-scoped rule: the conventions for adding a component, the styling system in use, the accessibility floor, where shared primitives live. Example frontmatter:

```yaml
---
paths:
  - "src/components/**"
  - "src/ui/**"
---
```

Keep the glob tight enough that it only loads for sessions actually touching UI — reach for a directory scope like the above, not a broad `**/*.tsx`, which would also load the rule for backend-in-TypeScript work.

## Related built-ins

For the *visual* side of frontend work, Anthropic's built-in `artifact-design` and `dataviz` skills already cover layout, theming, and chart design — reference those rather than re-encoding them. This category stays focused on structure, state, and accessibility.

## Consuming these

Copy a skill folder into your repo's `.claude/skills/` and localise the `<placeholders>` (your framework, your component directory). See the [library index](../README.md#consuming-a-skill).
