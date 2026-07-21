# Performance — fast enough, proven, not guessed

## What this distinction is

Performance work goes wrong in two opposite directions, and agents fall into both. One is optimizing on intuition — rewriting a "slow" path that was never the bottleneck, adding complexity for a win nobody measured. The other is shipping an accidental scaling bomb — the innocent-looking loop that fires a query per row and passes every test on seed data, then melts in production. These skills target each: **measure before you optimize**, and **don't write the N+1** that's the single most common real-world performance bug.

They're about earning speed with evidence, not folklore — and about catching the one pattern that reliably turns fine-on-my-machine into an incident.

## When to reach for these

- About to change something for speed/memory reasons → **measure-before-optimizing**.
- Writing a loop that does a query, request, or I/O call per item → **avoid-n-plus-1**.

## When not to

- An obvious bug with a known cause and fix (an accidental `O(n²)`, a missing index) — just fix it; you don't need the measurement ceremony.
- Correctness work, and genuinely single-item operations with no collection to batch.
- Micro-tuning a cold path. If it doesn't run hot, its speed rarely matters; spend the effort where measurement points.

## Skills in this category

| Skill | Fires when | What it enforces |
|---|---|---|
| [`measure-before-optimizing`](skills/measure-before-optimizing/SKILL.md) | Any perf-motivated change | Profile → baseline → change one thing → re-measure; keep only measured wins |
| [`avoid-n-plus-1`](skills/avoid-n-plus-1/SKILL.md) | A loop doing I/O per item | Batch or eager-load so N items cost one round-trip, not N |

## Related skills elsewhere in the library

- **`state-colocation`** ([frontend](../frontend/)) covers the render-performance side — state placed too high re-renders the world.
- **`observable-by-default`** ([backend](../backend/)) is how you get the latency metrics `measure-before-optimizing` depends on; you can't measure what you don't instrument.

## Rules for this area (path-scoped)

Performance discipline is behavioural and applies wherever hot paths live, so it rarely maps to a tight `paths:` glob. The exception: if your repo has a documented performance budget or benchmark suite, a rule scoped to that directory can carry the thresholds and how to run the benchmarks.

## Consuming these

Copy a skill folder into `.claude/skills/` and localise the profiler / ORM references to your stack. See the [library index](../README.md#consuming-a-skill).
