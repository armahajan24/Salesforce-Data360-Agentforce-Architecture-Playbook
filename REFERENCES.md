# Reference index — official Salesforce documentation

This bibliography was assembled for the November 2026 educational release. URLs link to documentation, not to copied proprietary content. Check current release notes and org-specific edition/licensing before implementing.

## Data 360

- [Salesforce Data 360 Architecture](https://developer.salesforce.com/docs/data/data-cloud-dev/guide/dc-architecture.html) — end-to-end features and data modeling.
- [Object Model in Data 360](https://developer.salesforce.com/docs/data/data-cloud-dev/guide/dc-object-model.html) — DLO, DMO, unified DMO and calculated insight object.
- [Customer 360 DMO Mapping](https://developer.salesforce.com/docs/data/data-cloud-dmo-mapping/guide/c360dm-model-data.html) — mapping concepts.
- [Data 360 Development Cycle](https://developer.salesforce.com/docs/data/data-cloud-dev/guide/dc-dev-overview.html) — APIs and ingestion/unification flow.
- [Ingestion API](https://developer.salesforce.com/docs/data/data-cloud-int/guide/c360-a-ingestion-api.html) and [Streaming ingestion](https://developer.salesforce.com/docs/data/data-cloud-int/references/data-cloud-ingestionapi-ref/c360-a-api-streaming-ingestion.html) — asynchronous microbatch semantics.
- [Zero Copy Data Federation Supportability](https://help.salesforce.com/s/articleView?id=data.c360_a_byol_data_federation_supportability.htm&language=en_US&type=5) — explicitly supported and unsupported federation features.
- [Data 360 SQL reference](https://developer.salesforce.com/docs/data/data-cloud-query-guide/references/dc-sql-reference) — Data 360 SQL syntax, not identical to Snowflake SQL.
- [Data 360 Features](https://developer.salesforce.com/docs/data/data-cloud-dev/guide/dc-features-overview.html) — unstructured retrieval and segmentation.
- [Data 360 data spaces](https://help.salesforce.com/s/articleView?id=sf.c360_a_data_spaces_secure_data.htm&language=en_US&type=5) and [Assign Data Access](https://help.salesforce.com/s/articleView?id=data.c360_a_dc_access.htm&language=en_US&type=5) — access control.

## Agentforce

- [Agent Script](https://developer.salesforce.com/docs/ai/agentforce/guide/agent-script.html) — code-first orchestration.
- [Agent Script reference](https://developer.salesforce.com/docs/ai/agentforce/guide/ascript-reference.html) — `subagent` and control-flow vocabulary.
- [Agent Script flow](https://developer.salesforce.com/docs/ai/agentforce/guide/ascript-flow.html) — routing/execution behavior.
- [Agent Script actions](https://developer.salesforce.com/docs/ai/agentforce/guide/ascript-ref-actions.html) — Flow, Apex and reasoning tool patterns.
- [Agentforce DX](https://developer.salesforce.com/docs/ai/agentforce/guide/agent-dx.html) — source-driven development.
- [Agentforce APIs and SDKs](https://developer.salesforce.com/docs/ai/agentforce/guide/get-started-agents.html) — available programmatic interfaces.
- [Agent testing API](https://developer.salesforce.com/docs/ai/agentforce/guide/testing-api-get-started.html) — sandbox and testing considerations.
- [Agentforce DX testing](https://developer.salesforce.com/docs/ai/agentforce/guide/agent-dx-test.html) — notes legacy workflow vs new testing UI.

## Integration

- [Salesforce Pub/Sub API event durability](https://developer.salesforce.com/docs/platform/pub-sub-api/guide/event-message-durability.html) — 72-hour published-event retention (not an SLA for replay beyond the window).

**Interpretation conventions:** "can" means feature documented, not licensed/enabled in every org; "should" means an opinionated design recommendation. External SQL/architecture patterns are illustrations, not product capabilities unless cited.
