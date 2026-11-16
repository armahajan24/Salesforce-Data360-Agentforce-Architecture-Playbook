# 01 — Data 360 foundations, layers and object model

**Question this chapter answers:** How does Data 360 turn disconnected records into usable, governed context, and when is that preferable to querying a source system directly?

## The lifecycle

`Sources → Data streams / federation → DLO → DMO mapping → optional identity resolution → Unified DMO / insights → segmentation, activation and agent context`.

**DLO — Data Lake Object:** the arrival/staging representation of source-shaped data. It retains source identity and gives engineers a traceable record of what came in. External/federated DLOs are possible with supported Zero Copy paths.

**DMO — Data Model Object:** harmonized record shape with semantics and relationships (individual, contact point, engagement, custom request). A DMO is **not the same as** a Salesforce CRM sObject. It is a representation for data modeling and insight use, not automatically a transactional update endpoint.

**Unified DMO:** the output of identity resolution that links source profiles through rulesets. Underlying source records and their identifiers are retained. **CIO (Calculated Insight Object):** stored derived metric, for example open requests by customer and week.

### Fictional data map

| Source | Source key | DLO (conceptual) | Harmonized DMO | Grain |
|---|---|---|---|---|
| CRM contact | `crm:C-1001` | `CRM_Contact_DLO` | Individual | One source person |
| Snowflake account | `snowflake:A-1001` | `ASG_Account_DLO` | Account (custom) | One source account |
| Snowflake request | `snowflake:R-5001` | `ASG_Request_DLO` | Service Request (custom) | One service request |
| Portal member | `portal:P-8001` | `ASG_Portal_DLO` | Individual / Contact Point | One portal identity |

These names are **illustrative labels**, not guaranteed Salesforce API names. For each mapping document business keys, source namespace, joins, update mechanism, timestamp, data owner, retention and field classification.

## When Data 360 adds value

- Joining customer interactions across multiple systems and creating a reusable, governed relationship model.
- Periodic insights over engagement, service history, consented audiences, and cross-channel analytics.
- Providing filtered, relevant customer context to Agentforce *where the data is timely and the entitlement model is sound*.

### When a simpler service is better

If a customer asks for **the exact current ticket state**, a secure operational API may be safer than a data platform copy that can lag. If there is only one source and no cross-source query/reuse, an integration layer may be the right MVP. Avoid treating Data 360 as a mandatory hop for every agent action.

## Design exercise

You inherit two systems where `customer_id=1001` appears in both. Write a mapping that preserves `(source_system, customer_id)` before any profile match. Explain what happens if you join on the numeric ID alone. Expected: accidental cross-customer leakage, false unification and invalid service outcomes.

## Validation checklist

- [ ] Have source-of-truth and grain been recorded for each field?
- [ ] Does every source record have a stable, namespaced identifier?
- [ ] Are DLO→DMO field mappings and transformations version controlled?
- [ ] Are non-uniqueness, missing IDs and late events observable?
- [ ] Is the request operational (live) or analytical (eventually consistent)?

**Common architecture question:** Does identity resolution merge source CRM records? **No.** It creates a unified identity and links sources under configured rules; it does not eliminate the original records.

**Source:** [Data 360 object model](https://developer.salesforce.com/docs/data/data-cloud-dev/guide/dc-object-model.html) · [Architecture](https://developer.salesforce.com/docs/data/data-cloud-dev/guide/dc-architecture.html).
