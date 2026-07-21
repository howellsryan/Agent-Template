---
name: diff-self-review
description: Use before declaring any code change complete or opening a pull request. Enforces reading your own diff end to end as a critical reviewer would - catching leftover debris, missed cases, unintended scope, and half-done edits - before handing it off. Do not use for trivial single-character edits where the diff is self-evidently complete.
---

# diff-self-review: read your own diff before anyone else has to

The cheapest reviewer is you, thirty seconds before you say "done". Agents finish an edit and immediately declare victory, shipping the debug `print`, the commented-out false start, the case they meant to handle and forgot, the unrelated line an auto-formatter touched. Every one of those is obvious in the diff and invisible in your memory of "what I meant to do". Read the actual diff — not your intention — as if someone else wrote it and you're the one who has to approve it.

## The pass (read the whole diff, top to bottom)

- **Debris.** Debug prints/logs, commented-out code, TODOs you meant to resolve, temporary hacks, leftover scaffolding. Remove them.
- **Completeness.** Does the diff actually do everything the task asked? Every requirement, every case you intended? A half-applied change is worse than none — it looks done.
- **Scope.** Is every changed line part of the task? Formatting churn on untouched lines, a drive-by "improvement", an unrelated file — revert it. The diff should be exactly the task and nothing else. (This is `scope-fence` applied to your own output.)
- **Correctness re-read.** Reading the change cold, in one piece, surfaces the off-by-one, the inverted condition, the wrong variable that felt right while typing it line by line.
- **The obvious check.** Does it build? Do the tests pass? Are new files actually saved and included? The "of course it does" that turns out it doesn't.

## Why it catches so much

Writing code is local — one line at a time, each feeling right in the moment. Reviewing the diff is global — the whole change at once, in the reader's frame, where the gaps and the leftovers stand out precisely because they *don't* fit the story the diff tells.

## Checks

- Would I approve this diff if a colleague sent it, or would I leave comments? Address my own comments first.
- Is there anything here I'd be embarrassed to have a reviewer point out? Fix it before they can.
- Is every line in the diff explained by the task?

## When this does not apply

Trivial single-character or single-line edits where the diff is self-evidently the whole task. For anything with more than a couple of changed lines, the thirty-second pass pays for itself.
