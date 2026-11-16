# 03 — Primary keys, fully qualified keys, source contracts and data quality

A primary key is the stable identity of a row within a source. A **fully qualified key** combines that identity with the source namespace so `C-1001` in System A is not automatically `C-1001` in System B. Treat source key design and identity matching as separate concerns.

## Four different keys to distinguish

- **Source record key:** unique in its source dataset (`account_id`).
- **Source-qualified key:** `(source_system, account_id)`; safe cross-source record identification.
- **Relationship/foreign key:** links a request to an account *within a defined namespace*.
- **Unified person identifier:** output of matching/reconciliation, not a substitute for a source record's key and not proof that a user may access it.

### Example schema contract

| Field | Type | Rule | Example |
|---|---|---|---|
| `source_system` | string | non-null, controlled values | `snowflake` |
| `account_id` | string | non-null, stable per source | `A-1001` |
| `source_updated_at` | UTC timestamp | required for freshness | `2026-01-15T10:30:00Z` |
| `account_status` | enum | `ACTIVE`, `SUSPENDED`, `CLOSED` | `ACTIVE` |
| `contact_email` | string | optional PII; not a key or auth credential | `person@example.invalid` |

The accompanying [`validate_fixture.py`](../../labs/scripts/validate_fixture.py) checks synthetic keys and relationships, with negatives in `tests/`.

## Quality dimensions

| Dimension | Check | Why it matters |
|---|---|---|
| Completeness | Percent of rows with non-null keys | Missing identity breaks joins |
| Uniqueness | Duplicates by `(source, key)` | Duplicate retrieval or double counting |
| Referential integrity | Tickets with valid account FK | Orphaned case answers |
| Validity | Status enum; normalized phone/email | Bad mappings and routing |
| Timeliness | Source/event watermark vs query time | Stale customer status |
| Consistency | Comparison across source and replica | Incorrect account answers |
| Lineage | Field owner, source field and transform | Incident triage/audit |

## Failed-record policy

Reject or quarantine records with missing identity and invalid types. Do not silently turn `NULL` into a shared dummy customer ID. Retain reason codes, error source, processing time and replay strategy in protected telemetry. PII should be minimized in logs.

## Edge case: update arrives before create

Possible responses: queue for retry until parent exists; handle as idempotent upsert where business rules permit; or materialize with a pending-parent state and reconciliation. Choose based on whether missing-parent state can be safely exposed. Define *when* the orphan is escalated and how it is repaired.

## Security consequence

**Wrong keys can become access-control bugs.** Verify authorization after identity/relationship resolution, ideally using immutable IDs from authenticated context and server-side entitlements. Matching an email address does not confer account access.

**Source:** [Data 360 Data Model](https://developer.salesforce.com/docs/data/data-cloud-dmo-mapping/guide/c360dm-model-data.html). Actual primary-key/fully-qualified key configuration varies with source and model; consult current setup guide.
