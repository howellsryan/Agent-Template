---
name: full-state-ui
description: Use when building or modifying any UI that fetches, mutates, or depends on async or remote data - list views, detail pages, forms that submit, search, dashboards, anything with a loading spinner. Enforces designing all of loading, error, empty, and populated states, not just the happy path. Do not use for purely static content with no async, conditional, or user-driven data.
---

# full-state-ui: the happy path is one of four states, not the only one

An async view has at least four states, and agents reliably build only one — the populated one, with real data already present. Then production hits a slow network, a 500, or a new user with nothing yet, and the UI shows a frozen spinner, a blank screen, or a crash. The other three states aren't edge cases; every user sees loading on every visit, and empty on their first.

## The four states — account for each, every time

1. **Loading** — the request is in flight. Show a skeleton or spinner. Don't show stale data as if it were fresh, and don't lay out the page so it jumps when data lands (reserve the space).
2. **Error** — the request failed. Show what happened in human terms and a way forward (retry, go back). Never a raw stack trace, never a silent swallow that leaves the user staring at a spinner that will never resolve.
3. **Empty** — the request succeeded but there's nothing: no results, no items yet, first-run. This is a *designed* state (a prompt, a "create your first X" call to action), not an accidental blank. Distinct from loading and from error.
4. **Populated** — data is present. The state agents build by default.

For anything that *mutates* (a form, an action button), add the in-between: **submitting** (disable the control, show progress — so it can't be double-fired) and **success/failure** feedback.

## How to apply it

- Before writing the component, name the four states out loud and decide what each renders.
- Model them explicitly — a status enum (`loading | error | empty | ready`), not a scatter of `isLoading` / `data == null` booleans that combine into impossible or unhandled combinations.
- A boolean pair like `isLoading` + `data` has four combinations; make sure each maps to a defined render, not an accidental one.

## Checks

- Throttle the network / force a failure / point at an empty account — does each of the four states render something deliberate?
- Can any state leave the user with a spinner that never ends or a screen with no way forward?
- On a mutation: can the user fire it twice by clicking fast?

## When this does not apply

Static, synchronous content with no fetch, no conditional data, and no user-triggered async. The moment there's an `await`, there are four states.
