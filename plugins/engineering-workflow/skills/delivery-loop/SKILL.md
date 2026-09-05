---
name: delivery-loop
description: Use at the start of implementation work before the first edit, especially cross-layer changes requiring planning, code review and verification. Do not use for pure questions or research, or re-invoke after the loop has already started.
---

# delivery-loop: one session, gated steps

All delivery happens in **one continuous session**. Plan, Architect, Build, Code Review and Verify are steps you switch between, not delivery agents you spawn. Shared context avoids cold reloads, re-reading the same files, re-briefing decisions and losing detail across handoffs.

**No delivery subagents.** Do not spawn planner/builder/reviewer/QA agents for sequential implementation. The normal exception is read-only Explore/research fan-out when it keeps large search/file dumps out of the main context. Writes stay in the main session.

## Triage first

State the tier and a one-line reason before acting:

- **`delivery-loop: spike`** — the deliverable is an answer, not a change. Investigate feasibility, architecture, cost or root context cheaply and stop. Code written only to answer the question is throwaway. If exploration turns into implementation, start a new delivery loop rather than quietly shipping the spike.
- **`delivery-loop: checklist`** — routine, bounded work with an existing checklist or obvious verification path. Apply the checklist and hold completion to the repository's verification gate.
- **`delivery-loop: stepped`** — non-trivial implementation, cross-layer work, novel mechanics, persistence/schema changes, trust-boundary work, build/deploy changes, or anything whose blast radius is not obvious. Run the loop below.

If a checklist task becomes surprising, stop and escalate to stepped. Do not silently downgrade or skip a gate once stepped delivery has started.

## The loop

Read `steps.md` once for the step charters. Announce entry on one line (`step: plan`) and end each step with a **≤5-line handoff note** containing decisions, files/areas touched and open findings.

1. **Plan (always)** — derive the implementation plan from live repository evidence. Define executable success criteria and the scope boundary.
2. **Architect (optional)** — run before editing when the work is novel, multi-system, persistence/schema, security/trust-boundary or build-pipeline design. Set ownership and sequencing while a wrong turn is cheap.
3. **Build (as needed)** — implement the scoped change using the repository's existing patterns and source-of-truth boundaries.
4. **Code Review (always)** — review the working diff itself for correctness, simplification/reuse opportunities, accidental scope, security/integrity issues and maintainability. Verdict PASS/FAIL with concrete failure scenarios. FAIL returns to Build, then Code Review runs again.
5. **Verify (always)** — adversarially check the finished change against Plan's success criteria using fresh tests/builds/observations. User-visible work gets a visual/interaction check when the environment allows it. FAIL returns to Build; because the diff changed, Code Review runs again before Verify.

Commit or completion claims happen only after Verify passes. A draft PR may expose a concrete, verified slice while clearly listing outstanding release gates; do not describe it as complete.

Read the destination repository’s contributor instructions for build/test commands,
plan-gate triggers, visual checks, commit policy and final handoff. Those
project-specific requirements remain binding. This skill grants no additional
permissions and does not override the user or host.

Code Review is performed using the charter in `steps.md`; it does not require an
unlisted `code-review` skill or a separate reviewer agent.

## Companion disciplines

- `plan-gate` — makes the Plan step mandatory and evidence-backed for risky/novel work; available as a sibling skill in this plugin.
- `scope-fence` — keeps Build and review inside the requested boundary; available as a sibling skill in this plugin.
- `systematic-debugging` — use when the task begins with a broken thing; canonical upstream is `obra/superpowers` (installed separately by the repository bootstrap).
- `verification-before-completion` — external evidence standard for the Verify gate; canonical upstream is `obra/superpowers`.
