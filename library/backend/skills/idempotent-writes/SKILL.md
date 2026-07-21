---
name: idempotent-writes
description: Use when implementing or modifying any operation that mutates state and could be retried or redelivered - POST/PUT/PATCH handlers, queue and webhook consumers, payment/email/notification side-effects, background jobs, event handlers. Enforces that a duplicate delivery produces one effect, not two. Do not use for pure reads, or for operations that are already naturally idempotent (setting a single field to a fixed value).
---

# idempotent-writes: assume every request arrives twice

Networks lose responses, clients retry, queues deliver at-least-once, and users double-click. In a distributed system a duplicate is not an edge case — it is the expected case. If your write isn't safe under duplication, you will eventually double-charge a card, send two emails, or create two orders. Design for the second delivery from the start.

## The mechanisms (pick the one that fits)

- **Idempotency key.** The caller sends a unique key (a V4 UUID per logical operation, e.g. an `Idempotency-Key` header). You persist "key → result" the first time; on a repeat key you return the stored result without re-running the effect. Store the key *in the same transaction* as the effect, or the guarantee has a hole.
- **Natural unique key.** A DB unique constraint on something that identifies the operation (order number, `(user_id, day)`) turns a duplicate insert into a caught conflict instead of a second row.
- **Upsert over blind insert.** When the desired end state is "this row exists with these values", `INSERT ... ON CONFLICT DO UPDATE` (or equivalent) is idempotent by construction.
- **Persisted "already done" marker for external effects.** Before charging/emailing, check-and-set a durable flag in the same transaction that records the outcome. The external call itself isn't transactional, so the marker is what makes the *decision to call* exactly-once.

## The trap: the check and the write must be atomic

```
if not already_done(key):     # <-- two duplicate requests both read "not done"
    do_effect()               # <-- both proceed
    mark_done(key)            # <-- effect ran twice
```

A read-then-write with a gap is a race, not a guard. Close it with a transaction, a unique constraint, or an atomic compare-and-set — so the *first* writer wins and the second is rejected, not admitted.

## Checks

- If this handler runs twice with identical input, is the end state identical to running it once? If no, it's not idempotent yet.
- Is the dedupe check in the same atomic unit as the effect it guards?
- For non-transactional side-effects (charge, email, third-party call): is there a persisted marker so a retry after a crash-mid-effect doesn't repeat it?

## When this does not apply

Pure reads, and operations already idempotent by nature (writing a fixed value to one field). Everything that creates, increments, charges, sends, or enqueues needs a guard.
