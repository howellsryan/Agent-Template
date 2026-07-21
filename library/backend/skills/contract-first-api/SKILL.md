---
name: contract-first-api
description: Use when adding or changing any interface another system consumes - an HTTP/REST/RPC/GraphQL endpoint, a response shape, an event or message payload, a public function signature in a shared library. Forces the contract (request/response shape, status codes, error format, pagination, versioning) to be decided and written down BEFORE the handler is implemented, and enforces backward-compatibility rules on changes. Do not use for internal-only refactors that keep the wire contract byte-identical, or for prototypes with no consumers.
---

# contract-first-api: the interface is the product

The expensive backend mistake is shipping the handler first and discovering the response shape was wrong *after* a client depends on it. By then the shape is load-bearing and every fix is a breaking change. The contract is cheap to change before code exists and costly after. Decide it first.

## Before writing the handler

Write the contract down — in the response, a design doc, an OpenAPI/proto/GraphQL schema, or a test. It has five parts, all of them:

1. **Request**: method, path/params, body shape, required vs optional, auth required.
2. **Success response**: exact shape, and which status code (200 vs 201 vs 202 — they mean different things to clients).
3. **Errors**: the error *format* (a stable machine-readable `code`, not just human prose) and which conditions map to which status. Errors are part of the contract; clients branch on them.
4. **Pagination / list semantics**: if it returns a collection, how the caller gets the next page and what "empty" looks like.
5. **Versioning stance**: is this frozen for external callers, or free to change?

Only then implement. The handler conforms to the contract; the contract does not emerge from the handler.

## Changing an existing contract

The rule is **additive-only under a stable name**:

- **Safe (backward-compatible)**: adding an optional request field with a default; adding a field to a response; adding a new endpoint; accepting a new value in an enum you *read*.
- **Breaking**: renaming or removing a field; changing a field's type or meaning; making an optional field required; adding a value to an enum clients must *exhaust*; tightening validation on existing input; changing a status code.
- A breaking change requires **a new version** (`/v2`, a new field alongside the old, a new event type) **or an announced deprecation window** where both work. Never change the meaning of a name callers already use — a silent semantic change is the worst kind because nothing errors, data just goes wrong.

## Checks

- Would an existing client break if it never updated? If yes, it's breaking — version it.
- Is every error a caller can hit representable in the documented error format?
- Does the status code match the semantics (created→201, accepted-async→202, client error→4xx, never 200-with-an-error-body)?

## When this does not apply

Internal refactors that keep the serialized contract identical, and genuine throwaway prototypes with no consumers. The moment a second system reads your output, the contract exists whether you wrote it down or not — so write it down.
