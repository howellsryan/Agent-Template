---
name: checklist-driven-work
description: Use at the start of any task with more than a few sequential steps, multiple files or areas, or several distinct requirements. Enforces decomposing the work into an explicit, visible checklist that is kept updated as you go, so no step is silently dropped and progress stays legible to you and the user. Do not use for single-step tasks, trivial edits, or pure questions.
---

# checklist-driven-work: make the plan visible and check it off

Held in your head, a ten-step task loses step 6 — not because you can't do step 6, but because after step 5 you're reasoning about step 7 and the middle evaporates. A written, checked-off list is external memory: it survives a long session, makes "am I done?" a lookup instead of a guess, and shows the user exactly where things stand. The cost is a few lines; the failure it prevents is shipping work with a requirement quietly unmet.

## The practice

1. **Decompose before starting.** Turn the request into a list of concrete, verifiable steps — including the verification steps (run tests, check the build), not just the edits. Use whatever tracking your harness provides (a todo tool, a checklist in your reply).
2. **Right granularity.** Each item is a thing you can finish and check in one focused move. "Build the feature" is not an item; "add the endpoint", "add its test", "wire the client call" are. If an item hides three sub-tasks, split it.
3. **One in progress at a time.** Mark an item in-progress when you start it, done the moment it's actually complete — not batched at the end, where you lose the running picture.
4. **Only real completion counts.** A step with a failing test or a partial edit stays open. Don't check it to feel progress; a checklist that lies is worse than none.
5. **Adapt as you learn.** New sub-task discovered mid-work → add it now, while you see it. The list is living, not a contract signed up front.

## Why it beats working from memory

- **Nothing drops.** Every requirement is a line that's either checked or visibly not.
- **Legible progress.** The user (and a future you, post-context-compaction) can see done / in-progress / remaining at a glance.
- **Clean resumption.** Interrupted or compacted, you resume from the list instead of reconstructing what you'd done.

## Checks

- Does every distinct requirement in the request map to a checklist item? (Re-read the request against the list.)
- Is anything checked that isn't actually, verifiably finished?
- Did a step balloon into several? Split it rather than checking it half-done.

## When this does not apply

One-step tasks, trivial edits, and questions. If the whole job is smaller than the checklist would be, just do it — this is for work big enough to lose your place in.
