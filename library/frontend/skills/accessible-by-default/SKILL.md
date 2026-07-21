---
name: accessible-by-default
description: Use when building or modifying user-facing UI - components, pages, forms, buttons, modals, menus, any interactive element. Enforces semantic HTML, keyboard operability, labels, visible focus, and sufficient contrast as the UI is built, not as a later audit. Do not use for non-UI code, or for internal debug/tooling surfaces explicitly exempted from accessibility requirements.
---

# accessible-by-default: build it in, because bolting it on is a rewrite

Accessibility retrofitted is a rewrite: a `<div onClick>` that should have been a `<button>` has no keyboard handler, no focus, no role, and every fix ripples. Built in from the first render, it costs almost nothing — the right element usually *is* the accessible one. Agents default to `<div>`/`<span>` with click handlers because they render identically; the difference only shows up for someone using a keyboard, a screen reader, or high-contrast mode — who won't be in the room when you test with a mouse.

## The floor (non-negotiable, cheap when done first)

1. **Semantic elements over generic ones.** `<button>` for actions, `<a href>` for navigation, `<label>` tied to every input, real headings (`<h1>`–`<h3>`) for structure, `<nav>`/`<main>`/`<ul>` where they fit. You get keyboard behaviour, focus, and roles for free. A clickable `<div>` gives you none of it.
2. **Keyboard operable.** Everything you can do with a mouse works with Tab + Enter/Space. If you must make a non-semantic element interactive, you owe it `role`, `tabindex="0"`, and key handlers — which is why the semantic element is less work.
3. **Visible focus.** Never `outline: none` without a replacement. Keyboard users navigate by the focus ring; removing it blinds them.
4. **Labels & names.** Every input has an associated label; every icon-only button has an accessible name (`aria-label`). A screen reader announces the name — "button" alone is useless.
5. **Contrast.** Text meets WCAG AA (4.5:1 normal, 3:1 large). Don't convey meaning by color alone — pair it with text or an icon (colorblind users, grayscale).
6. **Images & media.** Meaningful images have `alt`; decorative ones have empty `alt=""` so they're skipped.

## Applying it

- Reach for the semantic element *first*; drop to `<div>` + ARIA only when no element fits, and then do the full job.
- ARIA is a patch, not a foundation — "no ARIA is better than bad ARIA". A correct `<button>` beats a `<div role="button">` every time.
- Tab through the feature before calling it done. If you can't reach or operate something with the keyboard, neither can a chunk of your users.

## Checks

- Can I Tab to every interactive element and activate it with Enter/Space?
- Does focus stay visible the whole way through?
- Does every input have a label and every icon-button an accessible name?
- Is any state (error, selected, required) shown by more than color?

## When this does not apply

Non-UI code, and internal-only debug surfaces your team has explicitly exempted. For anything a user might touch, the floor holds.
