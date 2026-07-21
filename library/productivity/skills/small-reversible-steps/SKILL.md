---
name: small-reversible-steps
description: Use when implementing a change large enough to span multiple commits or a long edit session - a feature, a refactor, a migration touching many files. Enforces working in small, individually-verifiable, revertible increments that each leave the build and tests green, instead of one large unreviewable change. Do not use for genuinely atomic one-line fixes, or where the task explicitly requires a single squashed change.
---

# small-reversible-steps: every stopping point should be a safe one

One big change is a cliff: it's unreviewable, it's all-or-nothing to roll back, and when a test finally fails you've no idea which of forty edits did it. The same work as a series of small steps — each compiling, each passing tests, each independently revertible — means every point is a safe place to stop, the reviewer reads a story instead of a wall, and a regression is bisectable to one small diff. The total edits are the same; the *risk profile* is completely different.

## The practice

- **Slice by "still works".** Each increment leaves the system green — builds, tests pass — even if the feature isn't finished. Prefer vertical slices that do one small thing end-to-end over horizontal ones ("all the models", then "all the handlers") that are broken until the last piece lands.
- **Separate the kinds of change.** A pure refactor (behaviour-preserving) and a behaviour change are different commits. Mixing them means the reviewer can't tell which lines changed *what* — and a bug hides in the ambiguity. Refactor first, green, then change behaviour.
- **Verify each step, don't batch verification to the end.** The point of small steps is the fast feedback between them. Run the relevant check after each, so a failure points at the last small diff, not the whole session.
- **Commit at green boundaries** (when the task involves commits). Each commit is a coherent, reversible unit with a message that says what it did. `git revert` on one bad step beats untangling it from nine good ones.

## Why it's worth the discipline

- **Bisectable.** A regression traces to one small commit, not a monolith.
- **Reviewable.** Small, single-purpose diffs get real review; 2,000-line diffs get rubber-stamped.
- **Cheap rollback.** Undo the one step that was wrong; keep the rest.
- **Legible history.** The commit log reads as the reasoning, not "WIP" then "fix".

## Checks

- Is the tree green *right now*, or am I several edits deep with the build broken? If broken, get to green before the next change.
- Am I mixing a refactor and a behaviour change in one step? Split them.
- Could I `revert` the last unit cleanly, or is it entangled with unrelated work?

## When this does not apply

Genuinely atomic one-line fixes, and tasks that explicitly demand a single squashed change. This is for work big enough that "all at once" is a risk in itself.
