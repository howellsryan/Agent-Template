# Security — the failures that don't announce themselves

## What this distinction is

Most bugs tell you they exist — a crash, a wrong number, a failing test. Security bugs stay silent until someone exploits them, which is why they need discipline built into how you write code rather than caught after. Agents introduce them by trusting input that came from outside, moving an authority check to where it can be bypassed, or leaving a secret in a place that gets committed. These skills target the three most common and most damaging: **who is authoritative for a decision**, **where untrusted input gets validated**, and **where secrets are allowed to live**.

This is the "get it right and keep it right" category — the base template's `CLAUDE.md §12` (trust model) is its always-on anchor, and Anthropic's built-in `/security-review` command is the audit pass. These skills keep the mistakes from being written in the first place.

## When to reach for these

- Deciding what the client can compute vs what the server must own — auth, money, grants, competitive state → **server-authoritative**.
- Handling any input that crossed a trust boundary — request bodies, params, uploads, third-party payloads, env → **validate-at-boundary**.
- Touching anything that could hold a credential — config, code, logs, commits → **secrets-hygiene**.

## When not to

- Fully internal, trusted-input utilities with no external surface (but be honest about "internal" — today's internal tool is tomorrow's exposed endpoint).
- These encode *habits*, not a substitute for a real security review on high-stakes changes. Run `/security-review` too.

## Skills in this category

| Skill | Fires when | What it enforces |
|---|---|---|
| [`server-authoritative`](skills/server-authoritative/SKILL.md) | Client/server trust decisions | Never trust the client for identity, authorization, or value; re-derive server-side |
| [`validate-at-boundary`](skills/validate-at-boundary/SKILL.md) | Handling external input | Validate/normalise all untrusted input at entry; parameterise; encode on output |
| [`secrets-hygiene`](skills/secrets-hygiene/SKILL.md) | Anything touching credentials | Secrets never in code, commits, logs, or client bundles — only in the secret store |

## Rules for this area (path-scoped)

Security-sensitive subsystems deserve a path-scoped rule that loads whenever they're touched — the place to spell out the trust boundary in detail:

```yaml
---
paths:
  - "src/auth/**"
  - "server/middleware/**"
  - "**/*permission*"
---
```

State plainly what's server-authoritative vs client-trusted and *why*, per the base template's `.claude/rules/` format. Ambiguity in the trust model is exactly where security bugs hide.

## Consuming these

Copy a skill folder into `.claude/skills/`. Pair with your repo's real trust-model documentation — these skills enforce the principle; your `CLAUDE.md §12`/rules hold the specifics. See the [library index](../README.md#consuming-a-skill).
