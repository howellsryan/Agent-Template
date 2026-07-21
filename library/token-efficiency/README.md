# Token efficiency — sessions cost money and attention

## What this distinction is

Every token an agent reads or writes is paid for, on every session, and the more junk in the context the worse the model's attention on what matters. This distinction is about keeping sessions **cheap, fast, and sharp**: saying the answer without the padding, reading only what the task needs, and spending expensive subagents only where they earn it. It's the discipline that makes the *whole progressive-disclosure architecture* of this template pay off — no point in a lean `CLAUDE.md` if the agent then dumps four files it didn't need into context and writes six paragraphs to report a one-line change.

The base template's `CLAUDE.md §13` already carries the short form of this as always-on guidance. These skills are the expanded, copy-into-your-repo versions for teams that want it as explicit, triggerable discipline.

## When to reach for these

- Any reply, especially post-edit status → **output-shaping**.
- Any time you're about to read files or search → **narrow-context-intake**.
- Deciding whether to spawn a subagent → **subagent-economy**.

## When not to

- When the user explicitly asks for depth, a full explanation, or a report — brevity serves the reader, and sometimes the reader wants everything. These skills defer to that.
- On prose the user asked to preserve verbatim, or where cutting would lose real information. Clarity outranks brevity; this is about cutting *fat*, not facts.

## Skills in this category

| Skill | Fires when | What it enforces |
|---|---|---|
| [`output-shaping`](skills/output-shaping/SKILL.md) | Every reply | Lead with the answer; cut preamble, postamble, restatement; budget the length |
| [`narrow-context-intake`](skills/narrow-context-intake/SKILL.md) | Before reading/searching | Targeted reads, file-list before full-content, don't re-read or fetch just-in-case |
| [`subagent-economy`](skills/subagent-economy/SKILL.md) | Considering a subagent | Spawn only for broad read-only fan-out; prefer skills/rules for small-to-medium repos |

## Related base-template skills

- **`ruthless-editor`** — the cutting pass for *persistent public prose* (docs, READMEs, PR bodies). `output-shaping` governs *chat replies and status*; `ruthless-editor` governs *documents*. Different targets, same instinct.

## Rules for this area (path-scoped)

Token discipline is behavioural and applies every session, so its home is `CLAUDE.md` (always-on) plus these skills — not a path-scoped rule. There's nothing file-specific to scope it to.

## Consuming these

These are the most directly reusable skills in the library — near-zero localisation. Copy into `.claude/skills/`, **or** fold their guidance straight into your `CLAUDE.md §13` if you prefer it always-on rather than triggered — but not both, or you pay for the same guidance twice (the exact anti-pattern this category warns against). `output-shaping` in particular restates `CLAUDE.md §13`; pick one home for it. See the [library index](../README.md#consuming-a-skill).
