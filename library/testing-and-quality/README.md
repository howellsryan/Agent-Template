# Testing & quality — knowing it works, not hoping

## What this distinction is

The difference between "I made the change" and "the change works" is a test that can tell them apart. Agents are fluent at producing plausible code and weak at proving it correct — they'll declare victory on unrun code, patch a bug they never reproduced (so they can't know it's fixed), and skip the self-review pass that would have caught the obvious mistake. These skills close that gap with three habits: **write the test alongside the change**, **reproduce a bug before fixing it**, and **review your own diff before calling it done**.

They're about *earning confidence*, cheaply and at the right moment — not about coverage vanity metrics.

## When to reach for these

- Changing behaviour, adding a feature, or modifying logic → **test-with-change**.
- Fixing a reported bug → **reproduce-before-fix**.
- About to declare any change complete → **diff-self-review**.

## When not to

- Pure exploration/spikes you'll throw away, and non-behavioural edits (docs, comments, formatting) — `test-with-change` and `reproduce-before-fix` say so themselves.
- `diff-self-review` is close to universal, but a one-character typo fix doesn't need a ceremony; use judgement.

## Skills in this category

| Skill | Fires when | What it enforces |
|---|---|---|
| [`test-with-change`](skills/test-with-change/SKILL.md) | Behaviour/logic changes | Add or update the test in the *same* change as the code; never leave logic untested |
| [`reproduce-before-fix`](skills/reproduce-before-fix/SKILL.md) | Fixing a bug | A failing test that reproduces the bug *first*, then the fix that turns it green |
| [`diff-self-review`](skills/diff-self-review/SKILL.md) | Before "done" | Read your own diff as a reviewer would; catch debris, gaps, and scope creep |

`diff-self-review` overlaps the base template's `scope-fence` on one axis — both police scope creep — but adds passes `scope-fence` doesn't: hunting leftover debug/debris, checking the change is actually complete, and a cold correctness re-read of the whole diff. If you already run `scope-fence`, `diff-self-review` is the final "read it as a reviewer would" sweep on top, not a duplicate.

## Rules for this area (path-scoped)

If your repo has non-obvious testing conventions — a specific runner, a fixtures pattern, "integration over unit here", a coverage gate — a rule scoped to your test directory carries them so every session applies them:

```yaml
---
paths:
  - "tests/**"
  - "**/*.test.ts"
  - "**/*_test.py"
---
```

Put the run command, the layout convention, and the "what we test vs don't" line in it. The base template's `CLAUDE.md §8` (commit gate) is the always-on companion — the exact command that must pass before commit.

## Consuming these

Copy a skill folder into `.claude/skills/` and localise the `<test command>` and framework references to your stack. See the [library index](../README.md#consuming-a-skill).
