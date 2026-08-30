# catalog-review — bespoke review agent

`catalog-review` is the independent review gate for this catalogue and for similar open-source agent-resource repositories.

Its job is not to re-describe what the author says they changed. It reads the **actual diff**, repository contract and live upstream evidence, then decides whether the change is trustworthy, portable and easy for a stranger to consume.

## Package contents

- `AGENT.md` — standalone reviewer instructions that can be used as a dedicated review agent/persona.
- `SKILL.md` — model-invoked version of the same review process.
- `checklist.md` — detailed review dimensions and release-readiness checklist.

## What it reviews

1. requirement and repository-boundary fit;
2. external provenance and licensing hygiene;
3. research/current-claim integrity;
4. information architecture and newcomer readability;
5. installability and portability of bespoke packages;
6. maintainability and single-source-of-truth discipline;
7. verification of links, paths and the final diff.

## Output

The reviewer returns one verdict:

- **READY** — no material issues found.
- **READY WITH NOTES** — safe to publish; non-blocking improvements remain.
- **NOT READY** — blocker/important findings must be fixed first.

Findings are ranked `BLOCKER`, `IMPORTANT`, then `SUGGESTION`, each with evidence and a concrete fix.

## Independence rule

The PR body, author summary and previous agent output are context only. They are never accepted as proof that a source was verified, a link works, a package installs, or a requirement was met.
