# Install delivery-loop in another repository

`delivery-loop` follows the `SKILL.md` pattern, but the exact project skill directory depends on the agent/harness you use. Put the files below into that harness's project-level skill location.

## Minimal package

Copy the `delivery-loop` skill directory with these two files:

```text
delivery-loop/
├── SKILL.md
└── steps.md
```

For Claude Code, a common project layout is:

```text
.claude/skills/delivery-loop/SKILL.md
.claude/skills/delivery-loop/steps.md
```

For another Agent Skills consumer, use its documented project skill directory rather than assuming the Claude-specific path.

Then adapt the activation snippet from `templates/always-on-agent-rule.md` into the destination `AGENTS.md`, `CLAUDE.md`, or equivalent always-on contributor instructions.

## Recommended first-party companions

For the full discipline, install these packaged companion directories as **sibling skills** named `plan-gate` and `scope-fence`:

```text
plan-gate/SKILL.md
scope-fence/SKILL.md
```

The source copies live under `companions/` only to keep this distribution package together. The installed skill names are `plan-gate` and `scope-fence`.

## External companions

Fetch external companions from their canonical upstream instead of copying them from this repository:

- `obra/superpowers` → `systematic-debugging`
- `obra/superpowers` → `verification-before-completion`

See `dependencies.md` for the direct upstream paths.

## Localise, do not fork blindly

Keep repository-specific facts outside the generic skill:

- authoritative build/test/CI commands;
- architecture/module boundaries;
- security and trust invariants;
- persistence/migration rules;
- generated-output restrictions;
- visual verification tooling.

Put those in the destination's always-on instructions or path-scoped rules. The loop should point to them, not duplicate them.
