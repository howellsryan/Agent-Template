---
name: subagent-economy
description: Use when deciding whether to spawn a subagent or do the work in the current session. Enforces spawning only where it earns its cost - broad read-only fan-out searches that would otherwise flood the main context - and preferring skills, rules, and direct work for small-to-medium tasks. Do not use to avoid legitimate parallelism the user asked for, or genuinely large independent workstreams.
---

# subagent-economy: a subagent starts cold and pays twice

A subagent is not free help — it starts with none of your context, re-reads the always-on material to get oriented, and returns a summary you then have to reconcile. For small-to-medium tasks that overhead exceeds the benefit: you'd spend more tokens spinning one up and unpacking its answer than doing the work inline. Spawn one only where its structural advantage is real.

## When a subagent earns its cost

- **Broad, read-only fan-out.** Sweeping many files/directories to answer one question ("where is X handled across the codebase?", "which files follow convention Y?"). The subagent reads the mess and returns only the conclusion — keeping dozens of file dumps *out of* your main context. This is the strong case.
- **A genuinely large, independent workstream** the user asked to run in parallel — big enough that cold-start overhead is a rounding error against the work itself.

## When to stay in-session instead

- **Small-to-medium changes.** Reading a few files and editing them is cheaper done directly than delegated. The round-trip isn't worth it.
- **Anything needing your accumulated context.** A subagent can't see what you've established this session; if the task depends on it, you'll spend more re-explaining than doing.
- **Behavioural discipline.** "Work carefully / plan first / stay in scope" is a *skill or rule*, not a subagent. Don't spawn an agent to enforce a habit — load a skill.

## The default order

1. Can a **skill or path-scoped rule** encode this? Prefer it — near-free, no cold start.
2. Can I just **do it inline**? For small-to-medium, yes.
3. Is it **broad read-only fan-out** or a **large independent stream**? Now a subagent earns its keep.

## Checks

- Would the subagent spend more tokens orienting than the task itself costs? Then do it inline.
- Am I reaching for a subagent to enforce a behaviour? That's a skill's job.
- Will it flood my context with file dumps I don't need to keep? That's exactly when to delegate — let it return only the conclusion.

## When this does not apply

Don't use this to refuse parallelism the user explicitly wanted, or to cram a genuinely large multi-part job into one overloaded session. The point is matching the tool to the size of the work, not avoiding subagents on principle.
