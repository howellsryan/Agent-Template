---
name: avoid-n-plus-1
description: Use when writing code that loops over a collection and does a query, request, or I/O call per item - rendering a list with related data, serializing records with their associations, calling an API once per element. Enforces batching or eager-loading so N items cost one (or a few) round-trips instead of N. Do not use for genuinely independent single-item operations, or where per-item calls are unavoidable and already batched at a lower layer.
---

# avoid-n-plus-1: one query for the list, then one per row, is the classic killer

The N+1 is the most common real-world performance bug, and it hides in code that looks fine: fetch a list (1 query), then loop over it and fetch each item's related data (N queries). Ten rows, eleven queries; ten thousand rows, ten thousand and one. It passes every test on seed data and falls over in production where the collection is large. Each round-trip carries latency, so N of them serialised is death by a thousand cuts.

## Spotting it

Any loop body that does I/O is a suspect: a query, an HTTP call, a cache lookup, a file read — executed once per element of a collection you already have. ORMs make it invisible: accessing `order.customer` inside a loop can silently fire a query every iteration through lazy loading.

## The fixes

- **Eager-load the relation.** Tell the ORM to fetch the associations up front (`JOIN` / `include` / `with` / `select_related`) so the related data comes back with the list in one query, not N.
- **Batch-fetch, then map in memory.** Collect the ids from the list, do *one* query for all of them (`WHERE id IN (…)`), build a lookup map, and resolve each item from the map. One round-trip instead of N.
- **Batch at the boundary** for external calls: a bulk endpoint, or a dataloader-style batcher that coalesces per-item requests fired in one tick into a single call.
- **Same rule for any I/O**, not just SQL — an HTTP or cache call per loop iteration is an N+1 too, and batches the same way.

## Checks

- Does this loop do a query / request / I/O call per iteration? That's an N+1 unless it's already batched below.
- Could I fetch everything the loop needs in one query *before* the loop, and look it up in memory inside?
- Have I tested with a realistically large collection, not three seed rows? The bug only shows at scale.

## When this does not apply

Genuinely independent single-item operations (you have one item, not a collection), and cases where per-item calls are truly required and already coalesced at a lower layer. Whenever you hold a collection and need related data for each element, fetch it in bulk.
