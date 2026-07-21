---
name: measure-before-optimizing
description: Use when about to make a change for performance reasons - speeding up a slow path, reducing memory, adding a cache, rewriting something you believe is a bottleneck. Enforces measuring first to locate the real cost, changing one thing, and re-measuring to confirm it helped, instead of optimizing on intuition. Do not use for an obvious known-cause fix (an accidental O(n^2), a missing index) or for correctness work.
---

# measure-before-optimizing: intuition points at the wrong bottleneck

The code you *think* is slow usually isn't the code that's actually slow. Optimizing on intuition spends real effort and adds real complexity to make a path faster that was never the bottleneck — while the actual cost sits somewhere you didn't look. Measurement replaces the guess with a fact, and turns "I made it more complicated and it feels faster" into "this number dropped from X to Y".

## The loop

1. **Measure to find the real cost.** Profile it, time it, look at the actual metrics/traces. Locate where the time or memory genuinely goes — not where you assume it goes. The bottleneck is frequently a surprise.
2. **Establish a baseline number.** Record the current cost (latency, memory, query count) so "did it help?" is a comparison, not a vibe. No baseline, no way to know.
3. **Change one thing.** A single, targeted change to the measured hot spot. Multiple simultaneous changes make it impossible to attribute the win — or the regression.
4. **Re-measure against the baseline.** Confirm the change actually moved the number, and by enough to matter. Sometimes it does nothing; sometimes it makes things worse.
5. **Keep only real wins.** If it didn't measurably help, revert it. Complexity added for an unmeasured or negligible gain is a permanent tax for a one-time illusion.

## The traps this avoids

- **Premature optimization.** Complicating code for performance nobody needs, before any evidence it's slow. Readable-and-fast-enough beats clever-and-marginally-faster.
- **Micro-optimizing the cold path.** Shaving microseconds off code that runs rarely while the real cost is an unindexed query or an N+1 (see `avoid-n-plus-1`) elsewhere.
- **Cache-as-reflex.** Adding a cache to hide a problem instead of measuring what's slow — now you own cache invalidation *and* the original cost.

## Checks

- Do I have a measured number showing this is the bottleneck, or a hunch?
- Do I have a before-baseline to compare against?
- Did I confirm the change actually improved the number, or just assume it did?
- Is the complexity I added justified by a measured, meaningful win?

## When this does not apply

An obvious bug with a known cause and fix (accidental quadratic loop, missing DB index — just fix it), and correctness work. This is for when you're trading complexity for speed: don't make that trade blind.
