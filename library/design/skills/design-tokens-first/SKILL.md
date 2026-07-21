---
name: design-tokens-first
description: Use when writing styles or choosing any visual value - colors, spacing, margins/padding, font sizes, line heights, border radii, shadows, breakpoints, z-index. Enforces using the design system's tokens and defined scale instead of hard-coded magic values, so the UI stays consistent, themeable, and dark-mode-capable. Do not use when no design system or token set exists yet (define one first), or for genuinely throwaway prototypes.
---

# design-tokens-first: no magic values

Every hard-coded `#3b7af0`, `margin: 13px`, or `font-size: 15px` is a small act of drift. Do it across a codebase and nothing lines up, nothing themes, and dark mode is a find-and-replace archaeology dig. A design system exists precisely so values come from a shared vocabulary. Reach for the token; invent a raw value only when you've confirmed none exists — and then add it to the system, don't inline it.

## The rule

- **Color** → semantic tokens (`--color-primary`, `--color-text-muted`, `--surface-raised`), never a raw hex/rgb in a component. Semantic ("text-muted") over literal ("gray-600") so themes can remap meaning.
- **Spacing** → the scale (`--space-2`, `spacing.md`, a 4/8px step), never an off-scale `13px`. Consistent rhythm is most of what makes a layout look intentional.
- **Type** → the type scale's sizes and line-heights, not arbitrary per-element values.
- **Radii, shadows, borders, z-index, breakpoints** → all tokenised too. A one-off `border-radius: 5px` next to the system's `4px` and `8px` is visible and cheap to avoid.

## Why it matters (beyond tidiness)

- **Theming & dark mode become free.** Swap the token layer; every consumer follows. Hard-coded values each need finding and changing by hand — and one gets missed.
- **Consistency is structural, not vigilant.** You can't accidentally use the wrong blue if there's one `--color-primary`.
- **Change happens in one place.** Rebrand or rescale by editing tokens, not grepping hex codes.

## Applying it

1. Before typing a literal value, check the token set for one that fits. Use it.
2. No token fits and the value is genuinely new → add a named token to the system, then reference it. Don't inline it "just this once" — the once becomes forty.
3. Match semantic intent, not appearance: use `--color-danger` for an error, not `--color-red`, so the meaning survives a theme change.

## Checks

- Grep your diff for raw hex/rgb, and for px values off the spacing scale. Each one is a token you skipped.
- Would this render correctly if the theme flipped to dark? If a hard-coded color breaks, that's the tell.

## When this does not apply

No token system exists yet (build one first — this skill consumes a system, it doesn't create it), or a genuine one-off throwaway. In any codebase with a design system, magic values are a regression.
