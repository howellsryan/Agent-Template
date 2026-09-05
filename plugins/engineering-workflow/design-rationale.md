# Why delivery-loop is single-session

## Decision

Sequential implementation work runs in **one continuous context**. Planner, architect, builder, reviewer and verifier are step mindsets, not separate agents.

## Why

Spawning a fresh agent for each sequential role has recurring costs:

- **Cold context reload:** each role reloads always-on instructions and repository orientation.
- **File re-reads:** the next role must fetch code the prior role already held.
- **Re-briefing:** decisions must be summarized across an artificial boundary, creating token cost and drift.
- **Lost nuance:** a compact handoff cannot preserve every observation that remained available in shared context.
- **Little useful parallelism:** Build waits for Plan; Verify waits for the diff. Sequential dependencies mean extra agents often buy no concurrency.

In prior use, multi-agent sequential delivery could multiply context spend materially (roughly 4–15× depending on harness and task). Treat that range as an experience-derived directional signal, not a universal benchmark.

## What the loop keeps from role separation

The useful part of a delivery squad is the **change of objective**:

- Plan tries to define the right work.
- Architect tries to prevent expensive structural mistakes.
- Build tries to produce the change.
- Code Review tries to find defects in the diff.
- Verify tries to falsify the claim that the task is complete.

Explicit step entry plus a short handoff note preserves those perspective changes without throwing away context.

## The fan-out exception

Read-only research/Explore fan-out can be beneficial when it prevents large search results and file dumps from entering the main context. That is genuinely parallel and can reduce context cost. Writes remain single-threaded so there is one authoritative diff and one continuous decision history.

## Revisit condition

Reconsider this design if agent harnesses gain cheap shared mutable context across subagents, sequential role spawns stop reloading material, or a delivery task contains truly independent write streams that can be merged safely without duplicating analysis.
