---
name: test-with-change
description: Use when adding a feature, changing behaviour, or modifying logic in code that can be tested. Enforces writing or updating the test in the same change as the code, and actually running it, so behaviour is verified rather than assumed. Do not use for throwaway spikes, or for non-behavioural edits like docs, comments, or pure formatting.
---

# test-with-change: the test ships with the code, or the code isn't done

"I'll add tests later" is how untested logic reaches main — later never comes, and the one moment you fully understand the change (right now, while writing it) is gone. A change without a test is a claim without evidence: it might work, but nothing can tell you, and the next person to touch it has no safety net. The test is part of the change, not a follow-up.

## The practice

- **Same change, not a later one.** New behaviour → a test that exercises it. Changed behaviour → update the test that pins the old behaviour to pin the new. The diff that touches logic touches tests.
- **Test behaviour, not implementation.** Assert on what the code *does* (inputs → outputs, effects), not how it does it internally — so a future refactor doesn't break the test without breaking anything real.
- **Cover the edges that bite**, not just the happy path: the empty input, the boundary value, the error case, the null. That's where bugs live and where the test earns its keep.
- **Actually run it, and watch it pass** — after watching it *fail without the change* if you can (a test that passes no matter what tests nothing). Unrun tests are decoration.
- **Match the house style.** Use the project's runner and conventions (`<test command>`, its fixtures/mocks pattern). A test that doesn't fit the suite rots.

## Why in the same change

- **You understand it now.** The intent, the edge cases, the reason — all in your head at the moment of writing. A week later it's reverse-engineering.
- **It gates the mistake immediately.** A wrong change fails its own new test before it ships, not in production.
- **It documents the behaviour.** The test is the executable spec the next contributor reads.

## Checks

- Does the logic I changed have a test that would fail if I reverted the fix but kept the test?
- Did I cover at least one edge/error case, or only the happy path?
- Did I run it and see it green? Did I confirm it's actually asserting (fails when the code is wrong)?

## When this does not apply

Throwaway spikes you'll delete, and edits with no behavioural surface (docs, comments, formatting). Anything that changes what the program *does* gets a test in the same breath.
