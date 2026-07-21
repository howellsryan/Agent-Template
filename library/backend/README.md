# Backend — the state you can't take back

## What this distinction is

Backend is where mistakes persist. A wrong pixel repaints next frame; a wrong migration, a double-charged card, or a broken API contract outlives the deploy and takes other people's systems down with it. These skills target where agents most reliably get server-side work wrong: the **interface** others depend on, the **schema** holding the data, the **retry** that turns one action into two, the **call** to a dependency that hangs you, and the **blind spot** where a production failure leaves no trace.

They're correctness and operability disciplines, not architecture opinions — not microservices vs monolith or Postgres vs Mongo, but how to change any of those without a silent, expensive regression.

## When to reach for these

- You're adding or changing an endpoint, RPC, GraphQL field, or event payload → **contract-first-api**.
- You're touching a database schema or any persisted/stored format → **migration-safety**.
- You're writing anything that mutates state and could be delivered twice — HTTP writes, queue consumers, webhooks, jobs → **idempotent-writes**.
- You're calling something that can be slow or fail — an external API, another service, a database → **resilient-calls**.
- You're writing a path you'd need to understand when it misbehaves in production → **observable-by-default**.

## When not to

- Pure read paths, internal refactors that keep the wire contract byte-identical, and throwaway/local-only prototypes with no consumers and no data worth preserving. Each skill's `description` states its own non-trigger — respect it, or the skill taxes work it can't help.
- Your product's *business* rules (pricing, tax, entitlement math) are not here — those are repo-specific and belong in your own `CLAUDE.md` / a path-scoped rule.

## Skills in this category

| Skill | Fires when | What it enforces |
|---|---|---|
| [`contract-first-api`](skills/contract-first-api/SKILL.md) | Adding/changing any consumed interface | Decide shape, status codes, errors, versioning **before** the handler; additive-only unless versioned |
| [`migration-safety`](skills/migration-safety/SKILL.md) | Schema / persisted-format changes | Expand→migrate→contract across deploys; reversible; backfill separated from DDL |
| [`idempotent-writes`](skills/idempotent-writes/SKILL.md) | Retryable mutations & consumers | One effect per logical request under at-least-once delivery |
| [`resilient-calls`](skills/resilient-calls/SKILL.md) | Calling a slow/failable dependency | Bounded timeouts, backoff+jitter retries on transient errors, graceful degradation |
| [`observable-by-default`](skills/observable-by-default/SKILL.md) | Production code paths | Structured logs, a trace id through the request, metrics you'd page on |

## Rules for this area (path-scoped)

Backend subsystems with real internal complexity deserve a path-scoped rule (`.claude/rules/`) that loads only when their files are touched — the place for architecture and invariants too detailed for `CLAUDE.md`. Good candidates: a payments/billing engine, an auth/session subsystem, a background-job framework, an event bus. Example frontmatter:

```yaml
---
paths:
  - "server/billing/**"
  - "src/payments/**"
  - "migrations/**"
---
```

Put in it: how the pieces fit, the non-obvious invariants (e.g. "amounts are integer cents", "webhook handlers must be idempotent — the provider retries"), the recipe for the most common change, and pointers to the one source-of-truth file per formula. See `.claude/rules/example-rule.md` in the base template.

## Consuming these

Copy a skill folder into your repo's `.claude/skills/`, then localise the `<placeholders>` — your migrations directory, your API framework, your idempotency-key column. See the [library index](../README.md#consuming-a-skill) for the full flow.
