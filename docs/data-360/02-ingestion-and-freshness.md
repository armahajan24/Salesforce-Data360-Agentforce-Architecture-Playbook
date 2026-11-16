# 02 — Ingestion, CDC, batch, streaming and freshness

**Design outcome:** choose a change-delivery mechanism from business freshness and recovery requirements, not product names.

## Ask these questions first

1. What is the authoritative source? What *maximum stale age* is tolerated for the consumer?
2. Is this a backfill, ongoing change feed, or read-on-demand operation?
3. What are peak rate, per-record size, deletes, schema changes and burst frequency?
4. Can the consumer accept eventual consistency and duplicate events?
5. Who retries, backfills and reconciles after an outage longer than the replay window?

| Pattern | Typical fit | Important failure mode |
|---|---|---|
| Batch load | Historical backfill or periodic analytics | Staleness between runs; partial-load mismatches |
| Streaming ingestion API | Incremental micro-batches into Data 360 | Accepted payload not instantly queryable |
| Salesforce CDC → subscriber | Respond to Salesforce record changes | Gaps after retention window, duplicates |
| Business Platform Event | Explicit domain event (e.g., request submitted) | Delivery and consumer processing must be made idempotent |
| Secure live API | Exact current status or mutation | Source dependency, latency, throttling |
| Supported federation | Read external analytics/warehouse data without bulk copying | Feature, predicate, cost and query-performance constraints |

**Important precision:** Data 360's streaming ingestion API is a fire-and-forget, asynchronous micro-batch interface, with documentation describing processing approximately every three minutes. It does **not** give immediate strong-consistency guarantees for customer-facing status. The 72-hour retention cited for Salesforce event bus pertains to published Salesforce platform/CDC events, not a blanket ingestion SLA. Both behaviors must be checked against relevant current docs.

## Backfill + change capture

A robust generic migration sequence:

1. Snapshot data as of a known watermark and track batch ID, row counts and checksums.
2. Start capturing changes with stable event identity and source timestamps.
3. Apply backfill idempotently, then replay newer change records while comparing versions.
4. Confirm tombstone/delete handling, out-of-order behavior and cross-table consistency.
5. Reconcile counts and key-level diffs; alert on skipped offsets, failed records and staleness.

Use a source-qualified natural key or a durable surrogate plus source key mapping. Never silently choose last-arrival time over a trustworthy source version; network order is not necessarily business order.

## Synthetic example

Aster Service Group processes tickets in Snowflake. Policy FAQs may be batch indexed when published; analytics events can arrive by streaming; exact ticket status still uses an authorized status API. If the status API times out, the agent states it cannot verify the current value rather than presenting yesterday's warehouse value as live.

**SLO suggestion (illustrative, not observed):** status lookups must have authoritative as-of timestamps; freshness alerts on analytics if watermark age exceeds an agreed threshold. Define the threshold during discovery, not in a generic product diagram.

## Operational signals

Monitor ingestion request acceptance, downstream records visible, queue delay, watermarks, DLO rejection/error counts, schema drift, source-to-target row variances, and retries. Separate a transport success (HTTP accepted) from persisted/queryable success.

**Trade-off:** fewer integration components may simplify operations, but batch freshness can violate an operational use case. Conversely, a synchronous API is a poor choice for heavyweight historical aggregation.

**Sources:** [Ingestion API](https://developer.salesforce.com/docs/data/data-cloud-int/guide/c360-a-ingestion-api.html) · [Streaming semantics](https://developer.salesforce.com/docs/data/data-cloud-int/references/data-cloud-ingestionapi-ref/c360-a-api-streaming-ingestion.html) · [Event durability](https://developer.salesforce.com/docs/platform/pub-sub-api/guide/event-message-durability.html).
