# The Skill Library — a browseable catalog, organised by distinction

The base template (`CLAUDE.md`, `SKILLS.md`, `.claude/`) ships **five domain-agnostic behavioural skills** — how to work carefully in any repo. This `library/` is the other half: a **catalog of domain-specific skills, rules, and practices** grouped by distinction (backend, frontend, design, …) that you browse, pick from, and copy into your own repo.

## The one thing to understand first

**Nothing in `library/` is active.** These skills live under `library/<category>/skills/`, not under `.claude/skills/`, so no agent auto-loads them — including the agent that maintains *this* repo. This is a shelf, not a running config. To make a skill active in *your* project you **copy it into your repo's `.claude/skills/`** (see [Consuming a skill](#consuming-a-skill) below).

That separation is deliberate: a one-stop-shop should let you read every option without paying the context cost of all of them, and without them firing on unrelated work.

## Category map

| Distinction | What it covers | Start here if… |
|---|---|---|
| [`backend/`](backend/) | Server-side correctness: API contracts, schema migrations, retries/idempotency | you write endpoints, jobs, or anything that owns persisted state |
| [`frontend/`](frontend/) | Client UI: accessibility, async states, state placement | you build user-facing screens or components |
| [`design/`](design/) | Visual & UX craft: design tokens, hierarchy | you decide how things look, not just how they behave |
| [`productivity/`](productivity/) | Execution discipline: checklists, small reversible steps | your agent sessions sprawl or drop steps on big tasks |
| [`token-efficiency/`](token-efficiency/) | Session cost & speed: output shaping, narrow intake, subagent economy | sessions feel slow, expensive, or bloated |
| [`testing-and-quality/`](testing-and-quality/) | Confidence: tests-with-change, reproduce-before-fix, self-review | changes ship without a way to know they worked |
| [`security/`](security/) | Trust boundaries: server authority, input validation, secrets, dependency vetting | anything you build touches auth, money, untrusted input, or new dependencies |
| [`performance/`](performance/) | Earned speed: measure-before-optimizing, avoid-n-plus-1 | you're tuning on a hunch, or a loop quietly does I/O per row |
| [`devops/`](devops/) | Repeatability: reproducible setup, CI as the gate | "works on my machine" or green-by-retry keeps biting |

Each category folder has its own `README.md` that explains what the distinction represents, lists its skills, and says when to reach for them and when not to.

## How this library is structured

```
library/
├── README.md                     ← you are here (the catalog index)
└── <category>/
    ├── README.md                 ← what this distinction is; when to use / not
    └── skills/
        └── <skill-name>/
            └── SKILL.md           ← one skill, copy-pasteable into .claude/skills/
```

Rules (path-scoped `.claude/rules/*`) are inherently repo-specific — they key off *your* directory globs — so the library doesn't ship pre-baked rule files. Instead, each category README has a **"Rules for this area"** section: what path-scoped rules make sense there, with a concrete `paths:` frontmatter example you adapt. See `.claude/rules/README.md` in the base template for the format.

## Consuming a skill

1. **Browse** the category README, then read the `SKILL.md` that matches a problem you actually have.
2. **Copy** the skill's folder into your repo: `cp -r library/backend/skills/migration-safety <your-repo>/.claude/skills/`.
3. **Localise it.** Replace every `<placeholder>` (source dirs, script names, your migrations directory). A skill that references paths your repo doesn't have will misfire. Tighten the `description` to your stack if needed — the description is the only part always in context, so it alone decides when the skill fires.
4. **Register it** in your `SKILLS.md` inventory and, if it's short and universal, add a one-line pointer in `CLAUDE.md`. A skill nobody lists is a skill nobody maintains.
5. **Test it fires** on a real task before trusting it. If it over- or under-triggers, fix the `description` first, the body second.

## How to decide what to take

- **Take what pushes your agent off its defaults**, not what merely sounds good. A skill restating obvious practice burns a trigger slot and tokens for nothing. If your agent already does the thing reliably, skip the skill.
- **Start with 3–5, not twenty.** Every active skill's name+description sits in context every session. Eight to twelve well-chosen skills cover most of a senior engineer's day; past that you pay a context tax on work that never uses them. Audit periodically and drop anything you haven't triggered.
- **One job per skill.** These are intentionally small and composable — some reference each other (e.g. a domain skill ending with a `ruthless-editor` pass). Prefer several sharp skills over one monolith.

## When NOT to use this library

- You need product-specific domain knowledge (your pricing rules, your data model). That belongs in *your* `CLAUDE.md`/rules, not a generic catalog.
- The behaviour is already your agent's reliable default. Don't encode defaults.
- You'd be copying all of them "to be safe". That's the anti-pattern this structure exists to prevent — the context tax is real and paid every session.

## Authoring or contributing a skill

Follow the same practices the base template documents in `SKILLS.md §4`: the description is the contract (state the trigger AND the non-trigger), encode only what beats the default, exact examples over abstractions, prune overlap in the same change. Anthropic's own guidance — concise SKILL.md, progressive disclosure, one level of file references — is worth reading before you add one. On naming: this library uses short verb/adjective forms (`idempotent-writes`, `reproduce-before-fix`) to match the base template's house style; Anthropic suggests gerund/noun forms (`writing-tests`, `test-writing`). Either works — pick one and stay consistent across your set.

---

Further reading: [Anthropic — Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) · [Equipping agents with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) · [Agent Skills open standard](https://agentskills.io) · [mattpocock/skills](https://github.com/mattpocock/skills).
