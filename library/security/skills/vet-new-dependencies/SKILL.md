---
name: vet-new-dependencies
description: Use when adding a new third-party dependency to a project - a library or package, a CI/CD action, a container base image, a build plugin. Enforces a quick vetting pass (is the name right, is it real and maintained, is the license compatible, is it worth the weight) before it enters the dependency tree. Do not use when updating an already-vetted dependency, or for first-party/internal packages.
---

# vet-new-dependencies: adding a dependency is adding code you now trust

Every dependency you install runs with your code's privileges, ships in your artifact, and pulls its own dependencies behind it. Adding one is a supply-chain decision, not a convenience — a typosquatted name, an abandoned package, or a compromised maintainer becomes *your* security problem the moment it's in the tree. Agents install the first plausibly-named package that solves the task; spend thirty seconds vetting it first.

## The vetting pass (before `install`)

- **Name is exactly right.** Typosquatting hides one-character or look-alike names next to popular packages (`reqeusts`, `lodahs`). Confirm the exact package, from the expected author/org, is the one you're installing.
- **It's real and maintained.** Recent activity, multiple contributors or a reputable org, issues being addressed. A critical dependency that's one anonymous author with a last commit years ago is a risk — of abandonment and of takeover.
- **License is compatible** with your project's. A copyleft dependency in a proprietary product, or an unlicensed package, is a legal problem discovered too late. Check before adopting.
- **It's worth the weight.** Do you actually need it, or does the standard library / an existing dependency already do this? Each addition enlarges your attack surface, your build, and your maintenance. A one-function package pulling twenty transitive deps rarely pays for itself.
- **Reputation and adoption.** Widely-used, well-regarded packages have more eyes finding problems. Obscurity isn't disqualifying, but it raises the bar on the checks above.

Then **pin it** (lockfile, exact version) so what you vetted is what ships — see `reproducible-environment`.

## Checks

- Is this the exact, correctly-spelled package from the author I expect — not a look-alike?
- Is it maintained, or am I adopting an abandoned/single-owner critical dependency?
- Is the license compatible with this project?
- Do I actually need it, or can existing code do this without a new dependency?

## When this does not apply

Bumping a dependency you already vetted (that's routine maintenance), and internal/first-party packages. The gate is for *new* external code entering your trust boundary for the first time.
