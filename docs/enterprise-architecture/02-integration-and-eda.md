# 02 — Enterprise integration: APIs, CDC, Platform Events, Pub/Sub and resiliency

Choose integration by **business semantics**: request-response for needed current data; change/event streams for asynchronous propagation; batch for historical reconciliation. Do not equate a data ingestion stream with a user-facing low-latency API.

## Patterns

| Pattern | Strength | Watch for |
|---|---|---|
| REST API | Synchronous business operation and explicit error | Source availability, timeout, auth and retries |
| Bulk / scheduled job | Large periodic movement | Freshness and partial-batch reconciliation |
| CDC | Capture source record change | At-least-once behavior, ordering, deletes, replay |
| Platform Event | Domain/event signaling | Subscriber error handling and loss avoidance |
| Pub/Sub API | Subscribe/publish supported events | Replay IDs, 72-hour event retention, backpressure |
| Middleware / API layer | Policy enforcement, versioning and backend abstraction | Additional hop, owner, cost and possible single point of failure |
| Event relay / external bus | Decouple subscribers | Observability, ordering and failure ownership |

**Event replay nuance:** Salesforce documents 72-hour published-event retention for Platform Events and CDC events in the event bus; treat replay IDs as opaque and **do not assume** contiguous sequences or indefinite recovery. For longer outages keep an authoritative reconciliation/backfill path.

## Event contract (fictional)

```json
{
  "event_id": "evt-00001",
  "event_type": "ServiceRequestUpdated",
  "source": "asg-ticket-service",
  "request_id": "R-5001",
  "account_id": "A-1001",
  "version": 12,
  "occurred_at_utc": "2026-01-15T10:30:00Z",
  "changed_fields": ["status"]
}
```

Minimize sensitive payload; consumers fetch details with proper credentials when needed. The event ID plus source version supports deduplication; an event should not be an implicit authority to disclose an account.

## Idempotent consumer design

1. Verify signature/transport trust and validate schema version.
2. Look up idempotency key (`source`, `event_id`) or compare source entity version.
3. Process only if new and applicable; transactionally record deduplication where possible.
4. On retryable error use bounded exponential backoff; on poison record send to protected dead-letter workflow.
5. Alert on stuck subscribers and reconcile gaps by comparing source snapshots/watermarks.

## Saga versus transaction

A single CRM update inside one data service may be atomic. A cross-system workflow often cannot be one distributed transaction; design **Saga** steps, durable state, compensating actions and manual repair for irreversible operations. Never promise rollback for an action that cannot be reversed.

## Architecture review question

"What is the difference between CDC and Platform Events?" CDC reports source record changes; Platform Events are explicitly defined business event messages. A subscriber can use Pub/Sub API to consume supported event streams. Neither should be assumed exactly-once, and neither replaces source of truth for an immediate state check.

**Source:** [Pub/Sub API durability](https://developer.salesforce.com/docs/platform/pub-sub-api/guide/event-message-durability.html) · [Data 360 ingestion](https://developer.salesforce.com/docs/data/data-cloud-int/guide/c360-a-ingestion-api.html).
