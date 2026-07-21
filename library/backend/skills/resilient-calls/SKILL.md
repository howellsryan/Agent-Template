---
name: resilient-calls
description: Use when writing code that calls something that can be slow or fail - an external API, another internal service, a database, a cache, a queue, any network or I/O boundary. Enforces bounded timeouts, retries with exponential backoff and jitter on transient failures only, and graceful degradation, so one slow or failing dependency can't hang the caller or cascade into an outage. Do not use for pure in-process computation with no I/O, or where a framework/mesh already applies these policies centrally.
---

# resilient-calls: every remote call can hang or fail — code for it

The default way to call a dependency — no timeout, no retry policy, assume it returns — is the one that takes your service down when the dependency gets slow. A call with no timeout waits forever; a naive retry loop turns a blip into a storm; an unhandled failure propagates until the whole request chain is stuck. The caller, not the dependency, owns its own resilience.

## The rules

- **Timeout everything.** Every network/I/O call gets an explicit, bounded timeout. "It usually responds fast" is not a timeout — a dependency that hangs with no deadline hangs *you*, and then everyone calling you. Set connect and read timeouts.
- **Retry only what's worth retrying.** Retry *transient* failures (timeout, connection reset, 503, 429). Never retry a deterministic error (400, 404, validation) — it will fail identically and just waste time. And never retry a **non-idempotent** write unless it's guarded (see `idempotent-writes`) — a retried charge is a double charge.
- **Backoff with jitter, and a cap.** Space retries by exponential backoff (1s, 2s, 4s…) plus random jitter, with a hard max attempt count. Fixed-interval retries from many callers synchronise into a thundering herd that keeps a recovering dependency down.
- **Fail fast when it's already down.** A circuit breaker (stop calling a dependency that's failing, retry it sparingly) stops you from piling requests onto something that can't answer and freeing resources for work that can succeed.
- **Degrade, don't collapse.** Decide what happens when the call ultimately fails: a cached/stale value, a sensible default, a partial response, a clear error — not an unhandled exception that takes the whole request with it. Isolate the failure to the feature that needed it.

## Checks

- Does every external call here have an explicit timeout? Find the one that doesn't — it's the one that hangs you.
- Am I retrying a non-idempotent write without an idempotency guard? Stop — that double-applies.
- If this dependency is down for 5 minutes, does my service degrade gracefully or fall over?
- Do my retries have backoff + jitter + a cap, or are they a tight loop?

## When this does not apply

Pure in-process computation with no I/O, and environments where a service mesh or framework already enforces timeouts/retries/breakers centrally (don't double-apply — know which layer owns it). Every hand-written call across a network boundary owns these decisions.
