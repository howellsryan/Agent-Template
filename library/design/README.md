# Design — how it looks, not just how it works

## What this distinction is

Design is the layer above frontend behaviour: not "does the button work" but "does this screen read clearly, feel consistent, and hold together as one system". Agents are competent at making something *function* and weak at making it *cohere* — they pick arbitrary hex colors, invent one-off spacing, and pile on decoration before establishing what the eye should see first. These skills push toward the two habits that separate designed-looking work from assembled-looking work: **using a system's tokens instead of magic values**, and **establishing hierarchy before polish**.

This category is about *visual and structural craft*. Behaviour, state, and accessibility live in [`frontend/`](../frontend/) (though accessibility and design overlap — contrast is both).

## When to reach for these

- Writing styles or choosing colors, spacing, type sizes, radii, shadows → **design-tokens-first**.
- Laying out a screen or component, deciding what draws attention → **visual-hierarchy**.

## When not to

- Pure logic/data work with no visual output.
- You're implementing a fixed, pixel-specified mockup exactly — then follow the mockup; these skills are for when *you* are making the visual decisions.
- No design system exists yet. `design-tokens-first` assumes a token set to draw from; if there isn't one, defining it is the prerequisite, not the skill.

## Skills in this category

| Skill | Fires when | What it enforces |
|---|---|---|
| [`design-tokens-first`](skills/design-tokens-first/SKILL.md) | Choosing any style value | Use the system's tokens/scale, never hard-coded magic colors or spacing |
| [`visual-hierarchy`](skills/visual-hierarchy/SKILL.md) | Laying out a screen/component | Establish what the eye sees first via size/weight/space/contrast, before decoration |

## Related built-ins (use these, don't re-encode them)

Anthropic ships two design skills that are excellent and already loaded — reference them instead of duplicating:

- **`artifact-design`** — design fundamentals for building polished HTML/React artifacts and pages.
- **`dataviz`** — the authority on charts, dashboards, categorical/sequential palettes, and stat tiles. Read it *before* writing any chart code.

The two skills here fill the gap those leave: the general habits (tokens, hierarchy) that apply to *all* UI work, not just artifacts or charts.

## Rules for this area (path-scoped)

If you maintain a design-system spec, a tokens file, or a brand/visual-language doc, a path-scoped rule can point every styling session at it:

```yaml
---
paths:
  - "src/styles/**"
  - "tokens/**"
  - "**/*.css"
---
```

Put the token names, the spacing/type scale, and a pointer to the brand doc in it — so the agent reaches for real values, not invented ones.

## Consuming these

Copy a skill folder into `.claude/skills/` and localise it to your token names and scale. See the [library index](../README.md#consuming-a-skill).
