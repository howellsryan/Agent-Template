# Engineering Workflow

One maintained, product-neutral implementation of the delivery discipline used
across repositories. This is a skills-only plugin: it adds instructions, not
GitHub access, network permissions, an MCP server or background automation.

## Contents and ownership

- `skills/delivery-loop/` — loop control and the self-contained review/verify charters.
- `skills/plan-gate/` — evidence-backed planning before high-impact changes.
- `skills/scope-fence/` — complete the requested work without incidental cleanup.
- `skills/memory-hygiene/` — maintain durable instructions without stale copies.
- `.codex-plugin/plugin.json` and `.claude-plugin/plugin.json` — two host manifests
  over the **same skill directories**, versioned together.
- `dependencies.md` — separately installed upstream companions.
- `design-rationale.md` and `templates/` — optional author/consumer guidance.

The essential runtime files are the manifests and complete skill directories.
No skill depends on a reference outside its own directory. The review charter
is part of delivery-loop; a separate `code-review` skill is not required.

## Provenance

First-party MIT-licensed material maintained by Ryan Howells. Delivery-loop,
plan-gate and scope-fence moved from this repository's `bespoke/delivery-loop/`
package; they are not second copies. Memory-hygiene is a portable first-party
instruction-maintenance workflow. External companions stay upstream and retain
their own licence; see [dependencies](dependencies.md).

Keep repository commands, architecture, testing restrictions and final handoff
requirements in each consumer's `AGENTS.md`/`CLAUDE.md`. Shared skills must read
those rules, not bake in one project's assumptions.

See [installation and updates](https://github.com/howellsryan/Agent-Template/blob/main/docs/distribution.md).
