---
name: observable-by-default
description: Use when adding or changing code whose behaviour you'd need to understand in production - request handlers, background jobs, external calls, error-handling paths, state transitions. Enforces structured (machine-queryable) logging, a correlation/trace id carried through the request, metrics on what you'd page on, and correct log levels, so a production issue is diagnosable from telemetry instead of guesswork. Do not use for throwaway scripts or code with no real production runtime.
---

# observable-by-default: if it breaks in production, telemetry is all you have

In production you can't attach a debugger — you have logs, metrics, and traces, or you have guessing. Code written without observability is a black box the moment it's deployed: an incident becomes "add logging and wait for it to happen again" instead of "query what happened". Build the visibility in as you write the path, because the moment you need it is the moment it's too late to add.

## The rules

- **Log structured, not stringified.** Emit key/value fields (JSON), not `"user " + id + " failed " + err`. Structured logs are queryable and aggregatable across services; concatenated strings are grep-and-pray. One event = one structured record with named fields.
- **Carry a correlation/trace id** through the whole request and include it on every log line and downstream call. Without it you can't reconstruct one request's path through multiple services — you have disconnected fragments. Prefer OpenTelemetry for traces; it's the cross-platform standard.
- **Log at the boundaries and on every error** — request in/out, external calls, state transitions, and failures *with context* (what operation, what inputs-minus-secrets, what went wrong). An error logged as just `"failed"` tells you nothing.
- **Use levels meaningfully.** `error` = needs attention, `warn` = suspicious but handled, `info` = notable business events, `debug` = detail off in prod. Everything-at-info is noise; nothing-at-error hides real failures.
- **Metrics on what you'd page on** — request rate, error rate, and latency (the RED method) for each key path, plus the business counters that matter. You alert on metrics; you diagnose with logs and traces.
- **Never log secrets or PII.** Redact tokens, credentials, and personal data before they hit a log (see `secrets-hygiene`). A log is a data store with wide read access.

## Checks

- If this path misbehaves in production, can I reconstruct what happened from telemetry alone? If not, what's missing?
- Does every log line carry the correlation/trace id?
- Are my logs structured fields, or concatenated strings I'll have to regex later?
- Did I just log a header, body, token, or PII? Redact it.

## When this does not apply

Throwaway scripts and code with no production runtime. Anything that runs where users depend on it, and where "why did it do that?" will eventually be asked, gets built observable.
