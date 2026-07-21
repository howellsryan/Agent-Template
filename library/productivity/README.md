# Productivity — how the work gets executed

## What this distinction is

Productivity here means **execution discipline**, not typing speed. An agent with a correct idea still fails when it tackles a ten-step task as one shapeless push, drops step 6, and ends the session with a half-applied change nobody can review. These skills encode the two habits that keep long or multi-part work legible and safe to unwind: **decomposing into a tracked checklist** so nothing is silently dropped, and **working in small reversible steps** so any point in the work is a clean place to stop, review, or roll back.

They pair with the base template's `plan-gate` (write the plan before novel/multi-system work) and `scope-fence` (change only what was asked). Those two decide *whether and what*; these two govern *how you carry it out*.

## When to reach for these

- A task with more than a few sequential steps, or spanning multiple files/areas → **checklist-driven-work**.
- A change big enough to span multiple commits or a long edit session → **small-reversible-steps**.

## When not to

- Single-step tasks, trivial fixes, and pure questions. A checklist for a one-line change is ceremony, and these skills say so in their own non-trigger clauses.
- Don't stack these on top of `plan-gate` for the *same* decision — `plan-gate` produces the plan; `checklist-driven-work` tracks its execution. Use each for its half.

## Skills in this category

| Skill | Fires when | What it enforces |
|---|---|---|
| [`checklist-driven-work`](skills/checklist-driven-work/SKILL.md) | Multi-step / multi-area tasks | Decompose into an explicit, visible, updated checklist; nothing dropped |
| [`small-reversible-steps`](skills/small-reversible-steps/SKILL.md) | Large or long-running changes | Small increments, each leaving the build/tests green and individually revertible |

## Related base-template skills

- **`plan-gate`** — the written plan before the first edit on novel/multi-system work.
- **`scope-fence`** — do exactly what was asked; flag adjacent issues, don't fix them.
- **`memory-hygiene`** — what to persist across sessions and how to trust it.

Together with the two here, that's the full "work carefully" loop: plan it, scope it, track it, ship it in reversible pieces, remember what mattered.

## Rules for this area (path-scoped)

Execution discipline is behavioural, not file-scoped, so it rarely belongs in a path-scoped rule — it's skill/`CLAUDE.md` territory. The exception: if your repo has a strict contribution workflow (commit-message format, required checks, branch conventions), a rule scoped to `.github/**` or a `CONTRIBUTING.md` can carry it.

## Consuming these

Copy a skill folder into `.claude/skills/`. These are close to domain-agnostic — little to localise beyond your commit/verification commands. See the [library index](../README.md#consuming-a-skill).
