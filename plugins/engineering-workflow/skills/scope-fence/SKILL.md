---
name: scope-fence
description: Use on every task where you will modify existing work - code, documents, configs. Fences changes to exactly what was asked. Adjacent problems get FLAGGED, never silently fixed. Keeps diffs minimal and reviewable. Do not use it to refuse legitimate follow-through the task actually requires.
---

# scope-fence: do what was asked, flag what you found

The most reviewable diff contains the requested change and the supporting work it genuinely requires—nothing opportunistic.

## The fence

1. **Restate the task as a boundary.** One sentence before editing.
2. **Full effort inside the fence.** Required imports, tests, migrations or other supporting changes are in scope when the requested behaviour cannot be correct without them.
3. **Eyes open, hands off outside.** Notice adjacent problems but do not fold them into this diff.
4. **Flag, do not fix.** When relevant, report:

```text
Noticed, NOT touched: <issue> - <why it matters> - <suggested follow-up>
```

Do not list routine changed files—the diff already does that. No flags means no extra report.

## Gray-zone rules

- Would the requested change break without the extra edit? **In scope.**
- Is it merely "while I'm here"? **Out of scope.**
- Formatting/import churn on untouched work? **Revert it.**
- The real bug is somewhere outside the original boundary? **Stop and re-fence** rather than silently relocating the task.

## Before completion

Read the final diff against the boundary sentence. Split out unrelated paths, new dependencies, config/CI changes without a task reason, generated-output edits, formatting-only files and oversized refactors that do not directly support the requested outcome.
