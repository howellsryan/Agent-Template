# External companions

`delivery-loop` is self-contained for step control and Code Review. Two external skills complement it and remain pointer-only here so their upstream implementations stay current.

## systematic-debugging

**Role in the loop:** When an implementation task begins with broken behaviour, diagnose root cause before Build proposes a fix.

**Canonical source:** https://github.com/obra/superpowers/tree/main/skills/systematic-debugging

## verification-before-completion

**Role in the loop:** Defines the evidence bar for Verify and for any claim that work is fixed, passing or complete.

**Canonical source:** https://github.com/obra/superpowers/tree/main/skills/verification-before-completion

## Why they are not copied here

They are externally maintained skills with clear upstream ownership. This package links them rather than creating a stale fork. The destination can install their latest versions directly or use equivalent local disciplines.
