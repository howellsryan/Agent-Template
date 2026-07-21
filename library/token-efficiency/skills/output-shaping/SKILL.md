---
name: output-shaping
description: Use when composing any reply to the user, especially status updates after making an edit or running a command. Enforces leading with the answer and cutting preamble, postamble, restatement, and step-narration, so replies are short and scannable. Do not use when the user explicitly asks for a detailed explanation, a report, or a walkthrough - then depth is the goal.
---

# output-shaping: lead with the answer, cut the rest

Models pad by default — a warm-up sentence, a restatement of the question, a recap of what was just done, a closing offer to help further. None of it informs; all of it costs tokens and buries the one line the user needed. The reader wants the result, then (if relevant) the why. Give them that and stop.

## The rules (obey literally)

- **Lead with the answer or result.** First line is the outcome, not "Great question!" or "I'll now…" or a restatement of what they asked.
- **No preamble, no postamble.** Don't open by narrating what you're about to do; don't close by summarising what you just did or asking "anything else?". The work speaks.
- **Don't echo what they can already see.** File contents you just edited, tool output, the diff, their own request — point to it (`auth.ts:42`), don't reprint it.
- **No step narration.** "First I'll read X, then edit Y, then run Z" is noise unless the user asked for a plan. Just do it and report the result.
- **Budget the length.** Routine reply ≤ ~6 lines; a post-edit status is 1–3 lines. Exceed only when correctness genuinely needs a table, steps, or code — and even then, cut the dead sentences around it.
- **One idea per line, cut filler.** If a sentence survives deletion with no information lost, delete it.

## The test

Before sending, scan each sentence: *does the reader need this to know the outcome or decide the next move?* If not, cut it. A reply that's all signal reads as competent; padding reads as hedging.

## What this is not

- Not terse to the point of ambiguity — if a result needs three lines of context to be correct, give three lines. This cuts fat, never facts.
- Not a gag on genuine substance — code, a comparison table, a real explanation the task requires all stay. The cut targets *framing*, not *content*.
- Not for when the user asked for depth. "Explain how this works" is a request for the long form; honour it.

## When this does not apply

The user explicitly wants a detailed explanation, report, or walkthrough. Default to lean; expand on request.
