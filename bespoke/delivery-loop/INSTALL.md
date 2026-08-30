# Install delivery-loop in another repository

## Minimal install

Copy these two files into the destination agent-skill directory:

```text
.claude/skills/delivery-loop/SKILL.md
.claude/skills/delivery-loop/steps.md
```

Then add the activation snippet from `templates/always-on-agent-rule.md` to the destination `AGENTS.md`, `CLAUDE.md`, or equivalent always-on contributor instructions.

## Recommended companions

Copy the first-party companion skills when you want the full discipline:

```text
.claude/skills/plan-gate/SKILL.md
.claude/skills/scope-fence/SKILL.md
```

Install/fetch external companions from their canonical upstream instead of copying them from this repository:

- `obra/superpowers` → `systematic-debugging`
- `obra/superpowers` → `verification-before-completion`

See `dependencies.md`.

## Localise, do not fork blindly

Keep repository-specific facts outside the generic skill:

- authoritative build/test/CI commands;
- architecture/module boundaries;
- security and trust invariants;
- persistence/migration rules;
- generated-output restrictions;
- visual verification tooling.

Put those in the destination's always-on instructions or path-scoped rules. The loop should point to them, not duplicate them.
