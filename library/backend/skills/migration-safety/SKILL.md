---
name: migration-safety
description: Use whenever a change touches a database schema, a persisted data format, or a stored message/event shape - migrations, ALTER/DROP statements, new columns or indexes, backfills, changing a serialized format. Enforces expand/contract, reversibility, and separating the schema change from the data change so a deploy can roll back without data loss. Do not use for read-only queries, or for throwaway/local-only databases with no data to preserve.
---

# migration-safety: the old code and the new schema run at the same time

During any deploy there is a window where the **old application code is still running against the new schema** (and briefly the reverse). A migration that only makes sense once every server has the new code will break requests in that window — or worse, make rollback impossible. Design every schema change to be safe in that overlap.

## Expand / contract — the default for any non-trivial change

Never rename or drop in place. Split the change across deploys so each step is safe alone and reversible:

1. **Expand**: add the new column/table/field. Additive only — old code ignores it, keeps working.
2. **Migrate**: dual-write (write both old and new) and backfill existing rows. App reads still use the old field.
3. **Switch**: move reads to the new field. Deploy. Verify.
4. **Contract**: once nothing reads the old field, drop it — in a *later* deploy.

A rename becomes: add new → backfill → switch reads → drop old. Four safe steps instead of one irreversible one.

## Rules

- **Schema change and data change are separate migrations.** DDL (add column) is fast and transactional; a backfill over millions of rows is neither. Mixing them means a slow backfill holds a lock, or a failure leaves you half-migrated with no clean rollback.
- **Backfills are batched and resumable.** Chunk by id/time, commit per batch, safe to re-run from where it stopped. Never one `UPDATE` over the whole table.
- **Every migration has a tested down path** — a real `down`, or a documented forward-fix. "We'll figure out rollback if we need it" is how an incident becomes an outage.
- **Avoid long locks.** Adding an index on a hot table locks writes — use the concurrent/online variant your database offers. Adding a `NOT NULL` column with a default can rewrite the whole table on older engines; add nullable, backfill, then constrain.
- **Additive-only during the same deploy as code that doesn't know about the change.** Destructive steps wait until the code that needed the old shape is fully gone.

## Before applying

- If this deploy rolls back but the migration doesn't, does the old code still run? If no, split the migration.
- Is there a step here that can't be undone? If yes, it must be its own deploy, after the switch is proven.
- Point edits at `<your migrations directory>` — that's the single source of truth for schema state.

## When this does not apply

Read-only analysis queries, and local/disposable databases you can drop and reseed. Anything holding data a user would miss gets the full treatment.
