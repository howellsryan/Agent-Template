---
name: narrow-context-intake
description: Use before reading files, searching a codebase, or fetching external content. Enforces pulling only what the task needs - targeted searches, file-list results before full-content, ranged reads, no re-reading what's already in context, no just-in-case fetching. Do not use to justify skipping genuinely necessary reads - under-reading and guessing is its own failure.
---

# narrow-context-intake: read like context is expensive, because it is

Everything an agent reads stays in context for the rest of the session, costing tokens on every subsequent turn and diluting attention across more material. The reflex to "read the whole file to be safe" or "grep and read all thirty matches" front-loads cost that most of the task never uses. Pull what you need, when you need it — not everything you might.

## The practice

- **Search narrow, then read narrow.** A targeted query (`Grep` for the symbol, `Glob` for the path) beats reading directories. Prefer **file-list results first**, look at the paths, *then* open the two files that matter — not the content of all of them at once.
- **Read ranges, not whole files,** when you know the region. `Read` with offset/limit on the relevant function beats pulling 2,000 lines to see forty.
- **Don't re-read what's already in context.** If you edited a file this session, its current state is known — re-reading to "verify" burns tokens for nothing (the edit tools already confirm success). Don't re-derive a fact you established earlier.
- **Fetch on demand, not just-in-case.** Don't pull docs, schemas, or dependencies you might reference — pull them when a step actually needs them. Most "might need" never gets used.
- **Batch independent reads** in one turn so they parallelise, rather than a slow serial trickle — same content, less wall-clock and turn overhead.

## The balance (this cuts both ways)

Under-reading is also a failure. Guessing at a file's contents, editing on a half-read function, or skipping the one file that holds the invariant produces wrong work that costs far more than the read would have. The rule is **necessary and sufficient**: read exactly what the task needs to be correct — no dumping, no starving. When unsure whether you need it, a cheap targeted probe (list, grep, ranged read) resolves it without committing to the whole file.

## Checks

- Am I about to read a whole file when I know which function I need? Range-read it.
- Am I reading this because the task needs it now, or because I might later? If later, wait.
- Is this already in my context from earlier? Then don't re-read it.
- Did I grab the file list first, or jump straight to reading everything's contents?

## When this does not apply

Don't wield this to justify guessing. If correctness needs the file, read the file. This optimises *how* you read, never *whether* you read what the task genuinely requires.
