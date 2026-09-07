# Evaluate workflow efficiency

Read only when evaluating instruction cost or cache efficiency. This is a manual
comparison protocol, not a new gate for ordinary implementation.

Compare representative bug fixes, UI changes and domain changes on equivalent
repository snapshots with the same model, effort, tools and acceptance criteria.
Use several tasks/runs; keep cold-start and continued-session observations
separate. Record failures and rework rather than dropping unsuccessful runs.
Do not execute paid experiments unless included in the user's authorized scope.

| Record | Evidence |
| --- | --- |
| Task, repository SHA, workflow revision | Exact inputs and immutable refs |
| Host, model, effort and tool setup | Configuration available to the evaluator |
| Instruction bytes / loaded references | Context proxy, not token measurement |
| Input, cached input, cache writes, output/reasoning | Host/API telemetry if exposed; otherwise unavailable |
| Credits or billed cost, elapsed time | Observed values with units |
| Repeated reads, retries and rework | Trace or tool log |
| Correctness and acceptance | Unchanged repository gates, manual checks where needed |

Compare cost per accepted task alongside failure rate, latency and maintainability.
Where telemetry exists, aggregate cache reuse as total cached input divided by
total input (not the unweighted mean of request percentages). Account for cache
write charges where applicable and include output/reasoning cost. A higher cache
percentage or smaller diff alone is not success. Report unavailable telemetry
explicitly; do not derive savings from instruction-file size.

## Host boundary

ChatGPT Work/Codex assemble their own requests. Repository files can guide loading
and continuity; they do not set cache keys, breakpoints, retention or routing.
Filesystem dependency caches are also separate from model prompt caching.

In a runner you actually control, consult current model-specific API guidance
before changing request assembly. Keep stable content first, append history, and
preserve tool definitions/order where practical. Evaluate caching modes and
breakpoints against actual reuse rather than applying API options to Markdown.
Do not add provider settings to consumer repositories that do not own a runner.

Sources checked 2026-09-07; verify again before implementing provider controls:

- [OpenAI prompt caching](https://developers.openai.com/api/docs/guides/prompt-caching)
- [Astra model guidance](https://developers.openai.com/api/docs/guides/latest-model)
- [ChatGPT Work/Codex pricing](https://learn.chatgpt.com/docs/pricing)

No measured performance improvement is claimed by this instruction change.
