# Catalogue conventions

The cards in this directory are intentionally small. They answer **what is this, where is the source of truth, where do I use it, and how do I get the latest copy?**

## Types

- **External upstream** — maintained outside my repositories. Always fetch from upstream.
- **Adapted external** — upstream concept/body exists, but my project version has local changes. Re-sync deliberately; do not overwrite the adaptation blindly.
- **First-party portable** — workflow I maintain and reuse across my own repos.
- **Project-specific** — recipe tied to one product's architecture/data.

## Adding a card

Use this shape:

```md
# name

**Type:** ...

**What it does:** ...

**Canonical source:** <GitHub link>

**Used in:** `repo`, `repo`

**Get the latest:** <install/copy instruction>

**Notes:** optional provenance/adaptation detail.
```

Do not paste the upstream skill body, nested rule files, scripts, data, or licences into this catalogue.
