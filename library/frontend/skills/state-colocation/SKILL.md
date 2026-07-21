---
name: state-colocation
description: Use when adding or moving client-side state - component-local state, context/providers, stores, global state, or deciding where a piece of state should live. Enforces keeping state as local as possible and lifting it only when genuinely shared, to avoid global-state sprawl, prop-drilling, and needless re-renders. Do not use for server/persisted data modeling (that's a backend concern) or for fixed compile-time constants.
---

# state-colocation: put state where it's used, lift only when forced

The reflex to reach for global state (a big store, a top-level context) for everything is what turns a UI into a re-render minefield and a debugging nightmare. State that lives higher than it needs to makes every consumer re-render on every change, drills props through components that don't care, and scatters one feature's logic across the tree. Default to the *lowest* place the state can live and move it up only when a real second consumer appears.

## The ladder — climb only as far as forced

1. **Local component state** — used by one component and its children. Start here. Most state stays here.
2. **Lifted to the nearest common ancestor** — two siblings genuinely need the same value. Lift to where they fork, not to the root.
3. **Shared context / store** — many distant components need it *and* it changes rarely (theme, current user, locale), or it's genuinely app-global. This is the exception, entered deliberately.

Climb one rung only when the current one can't serve a real, present need — not a hypothetical future one.

## Rules

- **Derive, don't store.** If a value can be computed from existing state/props, compute it in render. Duplicated state drifts out of sync — that's a whole class of bugs you avoid by not creating the second copy.
- **Server data isn't UI state.** Fetched/remote data belongs in a data-fetching layer (query cache) with its own caching and invalidation — don't hand-copy it into a global store and re-implement staleness by hand.
- **Split contexts by change frequency.** A context bundling rarely-changing (theme) with frequently-changing (mouse position) re-renders every consumer on every mouse move. Separate them.
- **Colocate the logic with the state.** The reducer/handlers live next to the state they own, not in a distant central file.

## Checks

- Does this state have more than one real consumer *right now*? If not, it stays local.
- Am I storing something I could derive? Derive it instead.
- Will putting this in a shared context re-render components that don't use it? Split the context or push the state down.

## When this does not apply

Persisted/server data modeling (a backend concern) and fixed constants that never change. This is about *where mutable client state lives*, nothing else.
