---
name: visual-hierarchy
description: Use when laying out a screen, page, card, or component, or reviewing why one looks cluttered or flat. Enforces establishing visual hierarchy - what the eye sees first, second, third - through size, weight, spacing, and contrast BEFORE adding color, borders, shadows, or other decoration. Do not use for pure logic/data work, or when implementing a fixed provided mockup exactly.
---

# visual-hierarchy: decide what wins the eye, then decorate

A cluttered UI is almost never a color problem — it's a hierarchy problem. When everything is the same size and weight, nothing is important, so the eye has nowhere to land. Agents reach for borders, boxes, and background colors to create separation, which adds noise instead of structure. Establish the order of importance first with the quiet tools (space, size, weight); add decoration only if structure alone isn't enough.

## Build hierarchy in this order

1. **Decide the ranking.** For this screen: what must the eye hit first (the primary action, the key number, the title)? Second? Third? If you can't name the top of the hierarchy, the design has no focal point yet — fix that before anything else.
2. **Express it with the quiet tools first**, in this order of preference:
   - **Space** — proximity groups related things; whitespace separates unrelated ones. Grouping by spacing beats drawing a box around everything. This is the most under-used and most powerful tool.
   - **Size & weight** — bigger/bolder reads as more important. A clear type scale (one large heading, medium subhead, small body) does most of the work.
   - **Contrast** — the primary action is high-contrast; secondary is muted. One loud element per view, not five competing.
3. **Only then, decoration.** Borders, shadows, background fills, accent color — reached for *after* space and type, and only where they add structure the quiet tools couldn't. A shadow to lift the primary card, not a border around every element.

## Anti-patterns this kills

- **Everything boxed.** A border around every group is visual noise; spacing usually separates better and quieter.
- **Flat weight.** All text the same size — no scanning path, no focal point.
- **Competing emphasis.** Three "primary" buttons, four accent colors — the eye gives up.
- **Decoration as structure.** Reaching for color/borders to fix a layout that actually needs spacing and a type scale.

## Checks

- Squint (or blur it): does a clear focal point survive, or does it all blur into one gray mass? A blur test exposes flat hierarchy instantly.
- Is there exactly one clear primary action per view?
- Did I separate groups with space before reaching for borders/boxes?

## When this does not apply

Non-visual work, and implementing a fixed mockup exactly (follow the mockup). This is for when you're the one deciding how a screen is composed.
