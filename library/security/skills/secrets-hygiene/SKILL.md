---
name: secrets-hygiene
description: Use when touching anything that could contain a credential - API keys, tokens, passwords, connection strings, private keys, config files, CI configuration, logging code, or client-side bundles. Enforces that secrets never appear in source, commits, logs, error messages, or client-shipped code, and live only in a secret store or environment injected at runtime. Do not use for genuinely public, non-sensitive configuration values.
---

# secrets-hygiene: a secret in the repo is a secret already leaked

A credential committed to git is compromised the moment it's pushed — it's in the history forever, visible to everyone with repo access, and deleting it in a later commit does nothing (the old commit still has it). The same key printed to a log, baked into a client bundle, or echoed in an error message is exposed to whoever reads logs, views source, or triggers the error. Secrets have exactly one safe home: a secret store or environment, injected at runtime, never written down where code lives.

## The rules

- **Never in source or commits.** No hard-coded keys, tokens, passwords, or connection strings — not even "temporarily", not even in a test file. Read them from environment / a secrets manager at runtime.
- **`.gitignore` the secret files before creating them.** `.env`, key files, local config — ignored *first*, so they can't be staged by reflex. Ship a `.env.example` with blank/placeholder values as the template.
- **Never in logs or errors.** Don't log request bodies, headers (`Authorization`!), tokens, or full connection strings. Redact before logging. An error message that echoes a secret leaks it to every log reader.
- **Never in the client bundle.** Anything shipped to the browser/app is public — an API key in frontend code is readable by anyone with devtools. Secret-requiring calls go through your server, which holds the secret.
- **Rotate on exposure, don't just delete.** If a secret hit a commit, a log, or a bundle, it's burned — rotate it. Removing the line is not remediation; the value is already out.

## Before committing

- Scan the diff for anything that looks like a key, token, password, or connection string. Long random strings, `sk-…`, `-----BEGIN … KEY-----`, `user:pass@host` — treat each as a secret until proven public.
- Did I add a config/env file? Is it gitignored?
- Does any new logging print a header, body, or credential? Redact it.

## Checks

- Would this value give access to something if a stranger read it? Then it's a secret — it goes in the store, not the repo.
- Is there a real secret in this diff, in history, or in a log line I just added?
- Am I about to ship a key to the client? Route the call through the server instead.

## When this does not apply

Genuinely public, non-sensitive configuration (a public API base URL, a feature flag, a published client id explicitly designed to be public). Everything that grants access is a secret and never touches the repo, the logs, or the client.
