---
name: server-authoritative
description: Use when implementing or changing anything spanning a client/server (or any trust) boundary - authentication, authorization checks, prices and totals, granting items/credits/permissions, or any mutation of shared or competitive state. Enforces that the server owns and re-derives every security- or value-relevant decision, and never trusts a client-supplied value for it. Do not use for values the client is deliberately and safely trusted to compute (cosmetic/UI-only state).
---

# server-authoritative: the client is an input, not an authority

Anything the client sends, an attacker can forge — the browser, the app, the API caller are all under the user's control. A price computed on the client, a "isAdmin" flag in the request, an item-grant the client asks for: each is a value you *received*, not a fact you can *trust*. The server must own every decision that matters and re-derive it from data the client can't tamper with. "The client wouldn't send that" is not a security model; it's the vulnerability.

## What the server must own (never move to the client)

- **Identity & authentication.** Who the user is comes from a verified session/token the server validates — never a user id in the request body.
- **Authorization.** *Can this user do this?* is checked server-side, on every request, against server-held roles/ownership. A hidden UI button is not access control; the endpoint must enforce it.
- **Value & economics.** Prices, totals, discounts, balances, scores — recomputed server-side from authoritative data. Never trust a client-sent `price` or `total`; the client says *what* it wants, the server decides *what it costs*.
- **Grants & mutations of shared state.** Awarding items/credits/permissions, and anything affecting other users or competitive state, is decided and applied by the server.

## The rule

- **Re-derive, don't accept.** For any security- or value-relevant field, ignore the client's number and compute your own from trusted state. If you find yourself trusting a client value for one of these, that's the bug.
- **Check authorization at the point of action**, not just at the point of display. Hiding an option in the UI does nothing for someone calling the API directly.
- **Validate the session on every protected request** — don't assume a prior check still holds.

## The bounded exception

The client is *deliberately* trusted for some things — UI state, cosmetic choices, latency-hiding optimistic updates. That's fine when the value can't grant advantage or move real state. Name the guardrail anyway (the server still reconciles, a regression check exists) — but the line is bright: nothing that grants access, moves value, or touches another user is ever client-authoritative.

## Checks

- If the client sends a malicious value for this field, what's the worst outcome? If it's "free stuff / someone else's data / elevated access", the server must own it.
- Is this authorization checked at the endpoint, or only hidden in the UI?
- Am I trusting a client-sent price/total/id/role for anything consequential? Re-derive it.

## When this does not apply

Genuinely cosmetic, UI-only state with no security or value implication. Everything that authenticates, authorizes, prices, or grants is server-authoritative, always.
