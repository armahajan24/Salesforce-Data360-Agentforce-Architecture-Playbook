# 04 — Reliability, performance, observability and production incident handling

A system can be factually correct in a demo and still fail in production because of P95 latency, data drift, missing chunks, token costs, API rate limits or unhandled access-denied paths.

## Define nonfunctional requirements before implementation

| NFR | Discovery question | Proposed evidence |
|---|---|---|
| Availability | What uptime is required for each intent? | Dependency map, uptime and fallback tests |
| P95 latency | How long will users wait? | Timed tests by route and concurrency |
| Freshness | How stale can each field be? | Source-vs-served timestamp comparison |
| Correctness | Which mistakes are unacceptable? | Golden tests, manual severity review |
| Security | What leakage is zero-tolerance? | Negative entitlement test suite |
| Cost | What is acceptable per successful request? | Token/credit/API cost model |
| Recovery | How do we resume after outages? | Replay/backfill and incident drill |

## Stage latency budget (all numbers illustrative)

Example target P95 8s for a policy query: routing 1s + retrieval 1.5s + model 4s + network/UI 1.5s. The **sum of individual stage P95s is not necessarily equal to end-to-end P95**; measure both. Use different budgets for single API status lookup, RAG search and multi-step confirmed update.

## Observe the right things

Collect anonymized session/tracing data with explicit retention and data-space access; for each request: channel, intent, trace ID, routing version, document/version IDs (not raw PII), retrieval result count, selected action, tool error category, end-to-end and per-stage latency, refusal/escalation reason, policy outcome and approximate compute/credit consumption.

**Core dashboards:** P50/P95 by intent and channel; successful authorized resolution; unauthorized attempted access (rate and zero leaks); retrieval no-answer and citation defects; tool success/retry/timeout; cache age; indexing completeness; credit/warehouse compute per eligible resolution.

## Safe failure strategy

- If ticket API is unavailable, **do not invent the current status**; apologize briefly, present a timestamp only if clearly labeled historical, and offer escalation.
- If policy retrieval returns contradictory sources, provide no decisive policy recommendation; escalate to owner.
- If a write returns timeout after acceptance, check idempotency receipt/current state before retrying or claiming success.
- If authorization service fails, treat access as denied until safely revalidated.

## Production runbook

1. Triage severity based on trust/business impact, not just traffic.
2. Stop problematic actions or route to human workflow before stopping all read-only functions when safe.
3. Capture minimally necessary trace IDs, config versions, index version and deployment hash.
4. Compare error rate, retrieval coverage, stale-age and latency around a change.
5. Roll back compatible metadata/configuration, not blindly old state to new schemas.
6. Validate recovery, process backlog/backfill and publish transparent follow-up with owner/actions.

**Operational takeaway:** "We manage production AI like any other enterprise integration, plus additional retrieval, grounding and agent behavior signals."
