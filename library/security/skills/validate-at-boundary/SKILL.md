---
name: validate-at-boundary
description: Use when handling input that crossed a trust boundary - HTTP request bodies/params/headers, uploaded files, query strings, third-party API responses, webhook payloads, environment values, deserialized data. Enforces validating and normalising untrusted input at the point of entry, using parameterised queries, and encoding on output, so malformed or malicious input can't reach interpreters or corrupt state. Do not use for values already validated upstream within the same trust boundary.
---

# validate-at-boundary: distrust input until it's been checked

Every injection, overflow, and corrupt-state bug starts the same way: input from outside was used as if it were known-good. The defense is a clear boundary — at the edge where untrusted data enters, validate it, normalise it, and from there inward treat it as clean. Skip that and the untrusted value flows into a SQL string, a shell command, an HTML page, or your database, carrying whatever the attacker put in it.

## At the entry point — validate and normalise

- **Whitelist, don't blacklist.** Define what's *allowed* (type, format, length, range, enum) and reject everything else. Enumerating bad input always misses a case; enumerating good input can't.
- **Validate shape and bounds.** Right type, within length/size limits, matching the expected format. An unbounded input is a denial-of-service and a buffer waiting to happen.
- **Normalise once, early.** Canonicalise encoding, trim, decode — so later checks see one canonical form and can't be slipped past with an alternate encoding.
- **Fail closed.** Invalid input is rejected with a clear error, not coerced into something "close" that smuggles the payload through.

## Reaching interpreters — never concatenate untrusted input

- **SQL** → parameterised queries / prepared statements, always. Never build a query by string concatenation. This single rule kills SQL injection.
- **Shell/OS** → avoid shelling out with user input; if unavoidable, use argument arrays, never an interpolated command string.
- **HTML/JS output** → encode on output for the context (HTML, attribute, JS, URL). Output encoding is what stops XSS — and it's context-specific, so encode where you render, not where you store.
- **File paths** → validate against traversal (`../`); resolve and confirm the path stays inside the allowed root.

## The principle

Validate on the way *in*, encode on the way *out*, parameterise at the *interpreter*. Each defends a different step, and you need all three — input validation isn't a substitute for output encoding, and neither is a substitute for parameterised queries.

## Checks

- Is every external field validated (type, length, format, range) before use?
- Does any query, command, or markup get built by concatenating untrusted input? Parameterise / encode it.
- Could an alternate encoding or a `../` slip past my checks? Normalise before validating.

## When this does not apply

Values already validated at the same boundary upstream (don't re-validate ten times within one trusted layer). The rule is: validate once, at the edge where untrusted becomes trusted — and be honest about where that edge actually is.
