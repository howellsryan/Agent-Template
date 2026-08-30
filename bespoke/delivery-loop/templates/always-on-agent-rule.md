# Always-on delivery snippet

Paste/adapt this into the destination repository's `AGENTS.md`, `CLAUDE.md`, or equivalent always-on agent instructions:

```md
## Agent delivery

- Every implementation task starts with skill `delivery-loop` before the first edit. Pure questions/research are exempt.
- Delivery is single-session: Plan → optional Architect → Build → Code Review → Verify. Do not spawn planner/builder/reviewer/QA agents; read-only Explore fan-out is allowed when useful.
- Any modification of existing work uses `scope-fence`: required supporting changes are in scope; adjacent cleanup is flagged, not silently fixed.
- Novel/multi-system, trust-boundary, persisted-format/migration, or build-pipeline changes use `plan-gate` before editing.
- Broken behaviour starts with `systematic-debugging` rather than a guessed fix.
- Nothing is complete without fresh evidence meeting `verification-before-completion`; use this repository's authoritative test/build/visual gates.
```

Replace the final sentence with the destination's exact commit-gate commands or a pointer to the section that owns them.
