# 07 — Agent latency and knowledge troubleshooting

**Key principle:** split the time between router/orchestration, retrieval, tool calls, model generation and channel rendering before choosing a fix.

## Useful trace schema (illustrative)

| Field | Why |
|---|---|
| Correlation ID, hashed subject | Trace safely without leaking PII |
| Intent, selected subagent | Routing error attribution |
| Retrieval query/top-k/index version | Explain misses and excessive context |
| Source count, eligible chunks, returned chunks | Distinguish indexing from relevance |
| Tool name, response status, duration | API/service bottlenecks |
| Prompt/context token count | Prompt bloat |
| Orchestration/model latency | Model routing and generation cost |
| Total P50/P95, cost per request | Operational SLA and economics |

## Investigation workflow

1. Reproduce with a synthetic utterance and pinned document corpus version.
2. Measure which stage dominates P95 and which intents are affected.
3. If the doc is missing, inspect source ingestion→chunking→index→retriever filters, not just prompt instructions.
4. If model orchestration dominates, reduce irrelevant context, improve routing specificity, avoid redundant reasoning and cache only safe stable knowledge.
5. If source API dominates, inspect network, queue time, retries, database indexes, and rate limits; add timeouts and circuit breakers.
6. Re-run behavioral regression tests; a speedup that bypasses security or omits relevant exceptions is a regression.

## Hypothetical scenario (not production metrics)

Suppose average total turn duration is 20 seconds, with 13 seconds in orchestration and 4 seconds in API calls. Optimizing a 0.3-second retrieval step will have little overall effect. A latency budget and high-cardinality traces allow more focused changes. Do not claim these synthetic figures describe a real client.

## Cache carefully

A policy handbook with an approved effective date can sometimes be cached by version. A rapidly changing ticket status should be fetched from its authoritative source; if cached, its stale-age contract must be explicit. Cache keys must include tenant, entitlement scope and version to prevent cross-customer mixing.

## Incident runbook prompts

- Has the source record/knowledge article been ingested/indexed? How many chunks?
- Are data space and audience filters excluding it?
- Did a subagent transition change session variables?
- Did the model invent a parameter not declared by the action?
- Was tool invocation merely attempted, or did the downstream operation succeed?
- Is the model answering a question with stale analytic context as though it were live?

**See also:** [production observability](../enterprise-architecture/04-nfrs-and-observability.md) · [RAG evaluation](03-rag-evaluation.md).
