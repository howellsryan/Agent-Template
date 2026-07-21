---
name: reproducible-environment
description: Use when setting up dependencies, a development environment, a build, or a setup/bootstrap script, or when adding a new dependency or tool a project relies on. Enforces pinned versions, a single deterministic setup path, and no reliance on ambient machine state, so a fresh clone builds and runs identically for anyone. Do not use for genuine local throwaway experiments with no need to reproduce.
---

# reproducible-environment: a fresh clone should just work, identically

"Works on my machine" is a reproducibility failure: the machine has state — an installed tool, a global package, an env var, a cached artifact — that the repo doesn't capture, so the next person (or the CI runner, or an agent in a clean container) gets different behaviour or a broken build. The fix is to make the repo the single source of truth for how to stand it up, deterministically, from nothing.

## The rules

- **Pin versions.** Lockfiles committed (`package-lock.json`, `poetry.lock`, `go.sum`, …); language/runtime version declared (`.nvmrc`, `.python-version`, `go.mod`). Unpinned deps drift — the build that worked today breaks next week because a transitive dependency shipped a new version, and nothing in the repo changed.
- **One deterministic setup path.** A single documented command (or script) takes a fresh clone to runnable: `<setup command>`. Not a paragraph of prose steps people do differently; one path, same result every time.
- **No reliance on ambient state.** Don't depend on a globally-installed tool, a manually-set env var, or a file that happens to exist on your machine. Declare tools as dependencies; provide required config as a committed `.env.example` to copy; make the setup script create what it needs.
- **Fail loudly on missing prerequisites.** If setup needs a version or tool that's absent, error with a clear message — don't limp along producing subtly different output.
- **Same steps locally and in CI.** CI should run the *same* setup and build the repo documents, so green-in-CI actually predicts works-locally and vice versa. Divergence here is how "passes CI, breaks on deploy" happens.

## Why it compounds

- **Onboarding is clone + one command,** not a day of "why doesn't it build".
- **Agents and containers work first try** — a clean environment is exactly what a fresh clone should handle.
- **Bugs are reproducible.** If everyone's environment matches, a bug reproduces everywhere instead of being "can't repro on mine".

## Checks

- Could a teammate on a clean machine build and run this with only what's in the repo plus the documented command? If not, what hidden state am I assuming?
- Are all deps and the runtime version pinned/locked and committed?
- Does CI use the same setup path as a local clone, or a bespoke one that can drift?

## When this does not apply

Genuine throwaway local experiments you'll never share or rerun. Anything a second person or machine will build gets pinned and scripted.
