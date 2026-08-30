---
name: plan-gate
description: Use before starting novel or multi-system work - anything spanning multiple layers together (e.g. client + server + migration), touching a security/trust boundary, a persisted data format, or a core build/deploy pipeline. Forces a short written plan (goal, unknowns, success criteria, step order) BEFORE the first change. Do NOT use for routine work an existing checklist already covers - content/data authoring, single-area fixes, UI tweaks, doc edits - or for pure questions.
---

# plan-gate: no edits until the plan exists

The most expensive failure mode in agentic work is discovering the real shape of a task halfway through changing things. This gate forces that discovery before edits, when changing direction is cheap.

## The gate

Before the first edit, write:

```text
GOAL: <one sentence: what is true when this is done>
UNKNOWNS: <what is not verified yet - each with how it will be verified>
SUCCESS CRITERIA: <a command, test, or observable that proves the outcome>
STEPS: <numbered, smallest useful granularity, verification included>
OUT OF SCOPE: <adjacent things deliberately not changed>
```

Rules:

1. **The plan comes from evidence, not memory.** Read/search the relevant live repository first.
2. **Every unknown gets a verification step.** "Probably X" is not a plan line.
3. **Success criteria are executable/observable.** "Code works" is not enough.
4. **More than seven steps means decompose**, not write a ceremonial mega-plan.
5. **When reality contradicts the plan, stop and re-plan.** Do not improvise silently past a structural surprise.

## When it applies

Use it for new/multi-layer subsystems, trust/security boundaries, persisted formats and migrations, build/packaging pipelines, or cross-cutting refactors. Skip it for routine work already protected by a clear checklist/test path. If a routine task becomes surprising, escalate immediately.
