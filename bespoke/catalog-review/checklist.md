# catalog-review checklist

## 1. Requirement fit

- Does the change match the repository's stated purpose?
- Does `catalog/` contain external canonical pointers only?
- Does `bespoke/` contain only first-party or explicitly licensed/provenanced full material?
- Are downstream/private project references absent from the public catalogue unless intentionally part of bespoke provenance?
- Has the change added useful structure rather than merely more files?

## 2. Provenance and licensing

- Is every external resource linked to its original/current upstream source?
- Are mirrors, forks and discovery indexes clearly distinguished from upstream ownership?
- Has third-party content accidentally been copied into the repository?
- Does any adapted/full material state provenance and have a compatible licence basis?
- Does public documentation remind users that upstream licences still apply?

## 3. Research integrity

- Are claims such as current, official, active, popular, largest, newest or most-used verified live?
- Are adoption proxies described honestly rather than presented as installation telemetry?
- Is mutable research dated?
- Are mutable metrics kept in one research snapshot rather than repeated across cards?
- Is the selection method clear enough that another maintainer can refresh it?
- Are official/standards/specialist sources allowed on merit rather than being excluded by a raw star threshold?

## 4. Information architecture and readability

- Can a first-time visitor understand the repository in roughly two minutes?
- Does the root README offer obvious next actions?
- Are `catalog/` and `bespoke/` clearly different?
- Do folder names match what is actually inside them?
- Are cards concise and consistent?
- Is important guidance linked rather than duplicated?
- Are classifications accurate (skill library vs helper vs harness vs standard vs discovery index)?

## 5. Bespoke package installability

- Is the essential file set explicit?
- Do install paths acknowledge harness differences where relevant?
- Do installed skill/agent names match references inside the package?
- Do relative links still resolve after following the install guide?
- Are external dependencies linked to canonical upstream?
- Have product-specific paths, commands and invariants been removed or clearly marked as examples?

## 6. Maintenance

- Is there a contribution/update contract?
- Does mutable data have a single source of truth?
- Are there obvious stale-copy traps?
- Can a future maintainer add one resource without understanding unrelated private history?
- Would automated link checking or a periodic refresh help, or would it create more noise than value?

## 7. Final verification

- Read the final diff, not only individual files.
- Check renamed/deleted paths have no stale inbound links.
- Verify key Markdown links and install references.
- Confirm no project-specific/private references leaked into external catalogue cards.
- Check repository licence and bespoke provenance.
- State explicitly what could not be verified.
