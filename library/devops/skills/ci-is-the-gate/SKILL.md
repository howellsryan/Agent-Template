---
name: ci-is-the-gate
description: Use when reacting to a CI failure, or when adding/configuring checks that gate merges. Enforces treating red CI as a signal to fix the root cause - never retrying until it flukes green, never merging around it - and keeping the gate meaningful (fast, deterministic, required). Do not use to block on genuinely external outages unrelated to the change, which should be diagnosed and escalated, not "fixed".
---

# ci-is-the-gate: red means fix the cause, not press the button again

CI exists to answer one question: is this change safe to merge? When it goes red, the honest response is to find out why and fix it. The dishonest one — the one agents drift into — is to hit "re-run" until a flaky test happens to pass, or to merge past the failure because "it's probably unrelated". Both defeat the entire point: a gate you can retry or bypass isn't a gate, it's a suggestion, and the bug it caught ships anyway.

## When CI fails

1. **Read the failure.** Open the actual log, find the actual error. Not the summary — the line that failed and why.
2. **Diagnose the cause.** Is it *your change* (fix the change), a *flaky test* (fix or quarantine the test — flakiness is a bug, not weather), or a *genuine external outage* (a down registry, a provider incident — escalate, don't "fix")? Retrying blind never tells you which.
3. **Fix the root cause, then re-run once** to confirm the fix — not to roll dice. A re-run is verification of a fix, never a substitute for one.
4. **Never merge around a real red.** Bypassing a legitimate failing gate ships the exact defect the gate exists to stop.

## Flaky ≠ acceptable

A test that passes on retry without a code change is *flaky*, and flakiness quietly destroys the gate's value — people learn to ignore red, so real failures get ignored too. Treat a flake as a defect: make it deterministic (fix the race, the timing assumption, the shared state) or quarantine it explicitly. "Just re-run it" is how a suite rots into meaningless.

## Keeping the gate worth having (when configuring CI)

- **Deterministic** — same input, same result. A gate that lies at random isn't a gate.
- **Fast enough to respect** — a gate so slow people route around it protects nothing.
- **Required, and meaningful** — the checks that gate merge are the ones that actually predict breakage, marked required so they can't be skipped.

## Checks

- Do I know *why* it failed, or am I re-running to make red go away?
- If a test passed only on retry, did I fix the flakiness or just get lucky and move on?
- Am I about to merge past a failure I've decided is "probably unrelated" without confirming it?

## When this does not apply

A genuine external outage unrelated to your change (registry down, provider incident) — that's diagnosed and escalated, not "fixed" or retried into submission. The skill is about not *pretending* a real failure away, not about blocking forever on things outside the change.
