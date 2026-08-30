# Contributing

Contributions are welcome when they make the catalogue easier to trust, browse, or reuse.

The repository has two different contribution paths. Keep them separate.

## Adding an external resource

External resources belong under `catalog/` and remain **pointer-only**.

Before adding one:

1. Verify the canonical upstream repository or skill path exists.
2. Confirm it is actually a reusable skill, skill library, rule/helper collection, standard, or discovery tool — not just a search-result coincidence.
3. Prefer the original upstream over forks, mirrors, reposts, and downstream copies.
4. Read enough of the upstream README/content to classify it accurately.
5. Check the upstream licence before recommending copying/installing it.

Do not copy third-party `SKILL.md` bodies, scripts, datasets, reference folders, rules, or licence files into `catalog/`.

### Individual skill card

Use a functional folder when a specific skill is useful enough to bookmark directly. Keep the card short:

```md
# skill-name

**What it does:** one practical summary.

**Source:** canonical upstream GitHub path.

**Get the latest:** current upstream install/fetch guidance when known.

**Notes:** optional upstream-only detail.
```

### Source repository card

Use `catalog/sources/` for larger libraries, standards, specialist collections, harnesses, or discovery indexes:

```md
# owner/repository

**Kind:** library / specialist collection / standard / harness / discovery index / helper.

**What it offers:** one or two concise sentences.

**Source:** canonical GitHub repository.

**Use it for:** why somebody should open this source.
```

Do **not** put star counts, fork counts, or other mutable popularity numbers in individual cards.

## Refreshing ecosystem research

`catalog/sources/README.md` is the single home for dated ecosystem research.

When refreshing it:

- update the snapshot date;
- use live GitHub metadata rather than remembered numbers;
- treat stars/forks/activity as adoption signals, not installation counts;
- distinguish official vendor sources, high-adoption libraries, specialist collections, standards, harnesses, and discovery indexes;
- remove archived/dead sources and fix renamed repositories;
- avoid claiming the list is exhaustive or a definitive usage leaderboard.

A source can be worth including without being highly starred when it is an official/canonical implementation or a strong specialist resource.

## Adding or changing bespoke material

Full content under `bespoke/` must be original first-party material or carry explicit, compatible provenance and licensing.

Every bespoke package needs:

- a README explaining purpose and provenance;
- a clear install/copy path;
- dependency documentation;
- product-neutral defaults unless explicitly domain-specific;
- no broken relative references after installation;
- enough context for a stranger to use it without access to another repository.

External dependencies should normally remain upstream pointers rather than vendored copies.

## Before opening a PR

Run the [`catalog-review`](bespoke/catalog-review/README.md) process against the actual diff. At minimum verify:

- repository boundaries still hold;
- every external link points to canonical upstream;
- current/research claims were checked live;
- third-party material has not been copied accidentally;
- README/index links resolve;
- install instructions match the packaged file layout;
- a new reader can tell what changed and where to start.
