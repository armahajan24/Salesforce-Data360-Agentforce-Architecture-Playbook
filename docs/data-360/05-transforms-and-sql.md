# 05 — Data transforms, SQL and calculated insights

**Rule of thumb:** transform data once when several consumers need a normalized/derived shape; query on demand when the value must reflect an authoritative current state.

## Choose a transformation layer

| Requirement | Reasonable option | Watch for |
|---|---|---|
| Normalize `open`, `OPEN`, `Opened` to `OPEN` | Inline/batch transform | Data type, future enum drift |
| Reconcile historical service activity across systems | Batch transform / reusable mapping | Join grain and backfill strategy |
| Incrementally prepare event-derived fields | Streaming transform where source and feature support it | Stream compatibility, observability |
| Count 30-day cases per account | Calculated Insight / analytical query | Timezone, grouping, replay, source latency |
| Read exact current account balance/status | Live authorized service | Timeout and consistency |

**Data 360 calculated insights** are reusable aggregations with clearly specified **dimensions**, **measures** and refresh semantics. Don't add a measure to an unrelated grain: if a request joins three activity events, `COUNT(*)` after the join can incorrectly triple count requests.

## Fictional query: current open tickets in a warehouse

The SQL below is **Snowflake-like ANSI SQL** against synthetic table names, not a paste-ready Data 360 SQL query and not an executable Data 360 Calculated Insight definition.

```sql
SELECT
    account_id,
    COUNT(DISTINCT request_id) AS open_request_count,
    MAX(updated_at_utc) AS most_recent_request_update
FROM service_requests
WHERE status IN ('OPEN', 'IN_PROGRESS')
GROUP BY account_id;
```

For multi-table reports, project keys into consistent source namespaces and **aggregate before joining** where joins could multiply rows. See [`labs/sql/`](../../labs/sql/) for concrete queries.

## Worked transform example

Raw records:

```
ASG-1001, " active ", 2026-01-15T10:30:00Z
ASG-1002, "Suspended", 2026-01-15T11:00:00Z
```

Expected normalized statuses: `ACTIVE` and `SUSPENDED`. Preserve the raw field, normalized field, transformation version, source timestamp and rejection reason. Perform validation before exposing the field to an agent.

## When not to create a calculated insight

A customer says "Did my refund just post?" An hourly open-ticket aggregate is not appropriate evidence. Fetch the transaction state from its authoritative service and return a timestamp. Insights are for derived context and segmentation, not a substitute for transactional truth.

## Production checklist

- [ ] Define grain and deduplication rule per metric.
- [ ] Define source event time vs processing time, timezone, late-arrival behavior.
- [ ] Verify `COUNT(DISTINCT)` vs `COUNT(*)` in all joins.
- [ ] Validate precision, null/zero behavior, division by zero and denominator.
- [ ] Backtest against hand-calculated synthetic fixtures and source reconciliations.
- [ ] Document refresh dependency, lineage, backfill and failure notification.

**Sources:** [Data 360 SQL reference](https://developer.salesforce.com/docs/data/data-cloud-query-guide/references/dc-sql-reference) · [Data 360 architecture](https://developer.salesforce.com/docs/data/data-cloud-dev/guide/dc-architecture.html).
