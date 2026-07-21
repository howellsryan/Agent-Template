---
name: reproduce-before-fix
description: Use when fixing a reported bug, defect, or regression. Enforces first reproducing the bug with a failing test (or a deterministic manual repro), then applying the fix, then confirming the same test goes green - so the fix is proven and the bug can't silently return. Do not use for greenfield features with no bug to reproduce, or for cosmetic/non-behavioural tweaks.
---

# reproduce-before-fix: if you can't make it fail, you can't know you fixed it

A fix applied to a bug you never reproduced is a guess wearing a commit message. You don't know you found the real cause, you don't know your change addresses it, and you have nothing to stop it coming back. Reproducing first flips all three: the failing test *proves* you understand the bug, going green *proves* the fix works, and the test *stays* in the suite as a guard against regression. This is the single highest-leverage testing habit.

## The loop (red → green → keep)

1. **Reproduce it — deterministically.** Write a test that fails *because of the bug*: the input that triggers it, the assertion for what *should* happen. If it can't be a test yet, get a reliable manual repro first, then automate. An intermittent "sometimes" isn't reproduced — find the condition that makes it certain.
2. **Confirm the failure is the bug.** The test fails for the reported reason, not a typo in the test. Now you have the bug pinned.
3. **Fix it.** Change the code. Because you have a red test, you get immediate, unambiguous feedback on whether the fix works.
4. **Confirm green.** The same test now passes. The bug is provably addressed — not "should be".
5. **Keep the test.** It ships with the fix and becomes the regression guard. The next person who reintroduces this bug gets a red test instead of a production incident.

## Why not just fix it

- **You might fix the wrong thing.** Without a repro, a plausible-looking change can address a symptom while the real cause survives — and you can't tell.
- **You can't prove it's fixed.** "I think this does it" is not verification; a red-turned-green test is.
- **It comes back.** A fix with no test has nothing preventing the exact same regression next quarter.

## Checks

- Do I have something that fails *now*, because of this bug, and would pass after the fix?
- Did I watch it go red before the fix and green after — or did I just assume?
- Is the repro deterministic, or am I calling an intermittent failure "fixed" because it didn't happen this time?

## When this does not apply

New features with no existing bug to reproduce (that's `test-with-change`), and cosmetic edits with no behavioural failure. Any actual defect gets reproduced before it gets fixed.
