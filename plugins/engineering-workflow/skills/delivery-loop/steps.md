# delivery-loop — step charters

These are portable mindset charters. Repository-specific architecture, commands and invariants stay in that repository's own `AGENTS.md`/`CLAUDE.md`, rules and tests.

## Plan — always

Turn the request into buildable, testable work **from evidence, not memory**. Read/search the relevant repository areas before deciding the shape.

Emit:

```text
GOAL:             <one observable outcome>
UNKNOWNS:         <each unknown + how it will be verified>
SUCCESS CRITERIA: <commands/tests/observations that prove the outcome>
STEPS:            <ordered implementation + verification work>
EDGE CASES:       <boundary/failure scenarios worth covering>
OUT OF SCOPE:     <adjacent work explicitly excluded>
```

Ask the user only for genuine product decisions that live evidence cannot resolve. Use `plan-gate` when the change is novel/multi-system, crosses a trust boundary, changes persisted formats/migrations, or alters a core build/deploy pipeline.

**Handoff:** the chosen approach, success criteria, optional steps enabled, and any remaining product decision.

## Architect — optional

Run before the first edit when a wrong ownership or sequencing decision would be expensive.

Settle, with file/system-level specificity:

- ownership boundaries: which layer/module owns each new responsibility;
- trust boundaries: which inputs/state are authoritative and where validation belongs;
- data/persistence: schema shape, migrations, compatibility and rollback;
- source-of-truth boundaries: generated output vs editable source;
- sequencing: schema before code, API before UI, migration ordering, rollout constraints;
- non-goals: tempting architecture work deliberately left outside this change.

If the requested design violates an existing invariant, surface the conflict and choose/propose a compliant shape rather than working around it silently.

**Handoff:** architecture decisions, sequencing constraints and files/areas Build may change.

## Build — as needed

Implement the plan inside the `scope-fence`.

- Follow existing repository patterns before introducing new abstractions.
- Change the source of truth, not generated output.
- Add/update tests with behaviour changes where the repository supports automated tests.
- Preserve trust, persistence and module boundaries established by Plan/Architect.
- Flag adjacent defects; do not fold them into the diff unless the requested change cannot be correct without them.

**Handoff:** implementation decisions, touched areas, tests added, and any issue Code Review should scrutinise.

## Code Review — always after Build, before Verify

Review the **actual working diff**, independently of the builder mindset. This gate judges the diff itself; Verify judges it against the task's success criteria.

Look for:

1. correctness bugs and unhandled edge cases;
2. security/trust-boundary mistakes;
3. persistence/backward-compatibility problems;
4. duplicated logic or missed reuse that increases failure risk;
5. unnecessary complexity that can be simplified without widening scope;
6. accidental unrelated edits, generated files or formatting churn;
7. tests that merely mirror implementation instead of protecting behaviour.

Verdict **PASS** or **FAIL**. Every FAIL finding names the location and concrete failure scenario. FAIL → Build fixes findings → Code Review runs again until PASS.

For new helpers, abstractions or dependencies, check whether the existing domain
owner, standard library, native platform or an installed dependency already meets
the complete requirement. Prefer the simplest maintainable option with equivalent
behaviour. Do not optimise for line count, collapse useful module boundaries,
drop requested scope, or remove validation, accessibility or regression coverage.
Report a simplification only when its concrete benefit justifies the change.

**Handoff:** verdict, resolved findings and risks Verify must exercise.

## Verify — always

Be adversarial: try to prove the change wrong.

1. Compare the final diff with Plan's success criteria and scope.
2. Run the repository's authoritative test/build/lint/typecheck/validation gate as applicable.
3. Reproduce the original failure for bug fixes and confirm the fail→pass transition where practical.
4. Exercise boundary/negative cases not guaranteed by the happy-path suite.
5. For user-visible changes, inspect the actual rendered/interactive result when tooling permits; state explicitly if a visual check was impossible.
6. Read command exit codes and outputs before making completion claims.

Verdict **PASS** or **FAIL**. A green suite with a known uncovered failure scenario is still FAIL. FAIL → Build → Code Review → Verify.

**Handoff:** fresh evidence run, what was visually/manually checked, and anything not verified.
