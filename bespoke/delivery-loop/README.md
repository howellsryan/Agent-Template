# delivery-loop — bespoke first-party skill

`delivery-loop` is an original reusable delivery workflow maintained in this repository. Unlike `catalog/`, this folder intentionally contains the **full implementation** so it can be copied into another project without depending on a private/downstream repository.

## What it does

It runs software implementation as **one continuous agent session with explicit gates** rather than spawning separate planner/builder/reviewer/QA agents:

`triage → Plan → optional Architect → Build → Code Review → Verify`

The key design choice is that roles are **mindset/step switches inside one shared context**, preserving discipline while avoiding repeated cold context, file re-reads and handoff loss. Read-only Explore/research fan-out is the sole normal exception because it can reduce main-context intake.

## Package contents

- `SKILL.md` — trigger, triage model and loop control.
- `steps.md` — portable charters for Plan, Architect, Build, Code Review and Verify.
- `design-rationale.md` — why the workflow is single-session.
- `INSTALL.md` — copy/install guidance.
- `templates/always-on-agent-rule.md` — small CLAUDE.md/AGENTS.md snippet that wires the loop in.
- `companions/plan-gate/SKILL.md` — first-party planning gate for novel/multi-system work.
- `companions/scope-fence/SKILL.md` — first-party scope-control discipline.
- `dependencies.md` — external companion skills and their canonical upstream sources.

## Portability

This version deliberately removes product-specific paths, build commands, architecture section numbers and domain invariants from earlier project-local variants. A destination repository should keep its own build/test commands and invariants in `AGENTS.md`/`CLAUDE.md` or path-scoped rules; the delivery loop points to those sources rather than duplicating them.

## Provenance

The workflow evolved from repeated use of single-session Plan/Build/QA role switching and was consolidated here as the canonical open-source, product-neutral version. The design rationale records the reasoning rather than linking this package back to any product repository.
