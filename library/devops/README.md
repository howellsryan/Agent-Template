# DevOps — repeatability over "works on my machine"

## What this distinction is

DevOps here is the discipline of making things happen the *same way every time* — the build, the setup, the deploy, the checks — so that "it worked once" becomes "it works for everyone, every time". Agents undermine this in two classic ways: they set things up with unpinned, drifting dependencies so a fresh clone behaves differently, and they treat a failing CI run as noise to retry rather than a signal to fix, hammering "re-run" until it flukes green. These skills target both: **a reproducible environment** anyone (human or agent) can stand up deterministically, and **CI as the real gate** where red means fix-the-cause, not retry.

This is deliberately the smallest category — most DevOps knowledge is repo- and platform-specific (your CI provider, your deploy target) and belongs in *your* config and rules, not a generic catalog. What's here is the two habits that generalise.

## When to reach for these

- Setting up dependencies, a dev environment, a build, or a setup/bootstrap script → **reproducible-environment**.
- Reacting to CI status, or wiring up checks that gate merges → **ci-is-the-gate**.

## When not to

- Platform-specific pipeline authoring (your exact GitHub Actions / GitLab CI / deploy scripts) — those are yours to own; these skills give the principles, not your YAML.
- Genuine local throwaway experiments where reproducibility buys nothing.

## Skills in this category

| Skill | Fires when | What it enforces |
|---|---|---|
| [`reproducible-environment`](skills/reproducible-environment/SKILL.md) | Setup / deps / build | Pinned deps, deterministic setup script, no reliance on ambient machine state |
| [`ci-is-the-gate`](skills/ci-is-the-gate/SKILL.md) | Reacting to CI / gating merges | Red = fix the root cause; never retry-until-green; the gate is not optional |

## Rules for this area (path-scoped)

Your CI/deploy configuration is a strong path-scoped-rule candidate — the conventions and gotchas that only matter when someone edits the pipeline:

```yaml
---
paths:
  - ".github/workflows/**"
  - "Dockerfile"
  - "scripts/setup*"
---
```

Put the "how our CI is structured", the required checks, and the deploy sequence in it. Claude Code provides a built-in `session-start-hook` skill for making web sessions reproducibly able to run your tests/linters — pair it with this category.

## Consuming these

Copy a skill folder into `.claude/skills/` and localise the `<setup command>` / `<CI provider>` references. See the [library index](../README.md#consuming-a-skill).
