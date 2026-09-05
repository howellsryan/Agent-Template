# Install and maintain shared workflows

Agent-Template is the maintained source. A consuming repository records which
revision it uses; installed caches are dependencies, never editable skill forks.
Start with the repository bootstrap below for reproducible cloud/CLI checkouts.
The plugin marketplace is an alternative distribution path for compatible hosts.

## Repository bootstrap (the reproducible default)

Requires Python 3.10+, Git, network access to GitHub/raw.githubusercontent.com on
first install, and directory symlink support (Linux/macOS; Windows requires an
environment that permits symlinks, such as WSL). No Python/npm package is needed.

From a **clean, validated and pushed** Agent-Template commit:

1. Create `.agents/` and `tools/` in the consumer.
2. Run `python3 -B scripts/create_lock.py` here and save its stdout as the
   consumer's `.agents/skills.lock.json`.
3. Copy `templates/agent-skills.py` to the consumer's `tools/agent-skills.py`.
   This small loader is the only copied code; all installation logic and skills
   remain central. Compare it with the template when upgrading the bootstrap.
4. Ignore `.agents/cache/`, `.agents/skills/`, `.agents/skills-installed.json`,
   `.agents/install.lock`, and each generated `.claude/skills/<selected-name>`.
   Do not ignore the lockfile or unrelated project-specific skills.
5. Run `python3 tools/agent-skills.py`, then
   `python3 tools/agent-skills.py --check` in the consumer.
6. Add the loading instruction to the consumer's always-on instructions and run
   install + check in a dedicated CI job. Do not tie skill downloads to the game
   build, runtime dependencies, npm install or production deployment.

The lock pins the installer commit **and SHA-256**, the first-party source commit
and every upstream source commit. The loader verifies bytes before execution.
The installer fetches only those Git revisions and exposes complete selected
directories through `.agents/skills/` (Codex) and `.claude/skills/` (Claude Code).
The checkout retains the upstream LICENSE and supporting resources. It never
fetches a floating branch and never silently substitutes another version.

Only generated links recorded in `.agents/skills-installed.json` may be updated
or removed. Existing local skills and changed links are protected. Failed fetches
and preflight checks leave the previous discovery links in place; link-write
exceptions roll back. Interrupted processes can leave `.agents/install.lock`:
confirm no installer is running before removing that guard and rerunning.

`--check` is offline: it verifies cached Git revisions, detects cache edits,
checks selected skill entrypoints and checks both discovery paths. It does not
download or repair. Repeated installation is safe. Upgrades retain older source
caches so switching back to an earlier lock can work offline. Do not edit caches;
preserve accidental edits elsewhere before removing the affected cache.

After bootstrap, read the selected skill's full `SKILL.md` immediately. If the
host populated its skill menu before bootstrap, a new session may be needed for
native automatic discovery. A menu refresh is not required to read files directly.
For `superpowers:<name>` references in upstream text, use the corresponding
installed `<name>` directory. The profile includes test-driven-development because
systematic-debugging calls it; its supporting test guidance is included too.
The user's task and repository testing policy still govern what work is appropriate.

## GitHub-only / restricted environments

An AGENTS.md link is an instruction to retrieve a file, not an automatic install.
If shell/bootstrap networking is unavailable but the GitHub connector works, read
`.agents/skills.lock.json` and fetch the required `SKILL.md` and referenced resources
from its exact repository/path/revision. Record what was loaded. This supports
instruction reading, not automatic discovery or execution of unavailable scripts.
If neither path is available, report the missing dependency instead of claiming
to have run it. Do not use a stale copied version as an undisclosed substitute.

## Claude Code marketplace (alternative)

The root `.claude-plugin/marketplace.json` publishes `engineering-workflow` under
`ryan-agents`. Once this distribution is merged to the default branch:

```text
/plugin marketplace add howellsryan/Agent-Template
/plugin install engineering-workflow@ryan-agents
```

Install the upstream Superpowers plugin separately using its canonical README.
This native route uses the host's version/update controls; it is **not governed
by a consumer's bootstrap lockfile**. Do not simultaneously activate a native
plugin and bootstrapped standalone copies of the same skills. For strict per-repo
pinning use the bootstrap route, or a separate native-plugin-only environment.

## Codex marketplace (alternative)

The root `.agents/plugins/marketplace.json` exposes the same plugin through the
Codex marketplace schema. In a compatible local Codex installation, register the
checkout explicitly: `codex plugin marketplace add /absolute/path/to/Agent-Template`.
Then install `engineering-workflow` from `ryan-agents` in its plugin browser and
install the external companions separately. This documents the supported local
flow, not an assertion that an arbitrary GitHub marketplace is installable in
every ChatGPT mobile account. No native plugin is automatically activated by
committing this repository's marketplace files.

## Release and adoption

1. Edit skills or installer in Agent-Template. Update both plugin versions for a
   plugin release, and update the profile SHA when adopting upstream changes.
2. Run `python3 -B scripts/validate_distribution.py` and
   `python3 -B -m unittest discover -s tests -v`; run catalog-review on the diff.
3. Commit, push, review and merge the central PR first. Do not delete a referenced
   commit; prefer a retained merge commit for distribution releases.
4. Generate a new consumer lock from the desired clean commit. Review changed
   upstream instructions/resources, install, check and run the consumer's gates.
5. Merge the consumer adoption PR. Roll back by restoring its previous lock and
   rerunning bootstrap. Existing consumers never silently follow central `main`.

For a coordinated pair of PRs, a consumer may initially pin the central PR commit
once it has been pushed. Merge the central PR before the consumer. If the central
PR is squash/rebase merged, regenerate the consumer lock from the merged SHA
and re-verify before merging the consumer; do not rely on unreachable PR commits.

## References (checked September 2026)

- [OpenAI skill authoring](https://learn.chatgpt.com/docs/build-skills)
- [OpenAI plugin packaging](https://learn.chatgpt.com/docs/build-plugins)
- [Codex instructions](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
- [Claude Code marketplaces](https://code.claude.com/docs/en/plugin-marketplaces)
- [Superpowers](https://github.com/obra/superpowers)
