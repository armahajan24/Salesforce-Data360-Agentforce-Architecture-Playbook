# 07 — Snowflake, Zero Copy federation, caching and operational APIs

**Zero Copy is not "no cost" or "always live."** In the Salesforce context it means supported federation/access to external source data without first bulk copying all of it into native Data 360 storage. Query latency, warehouse compute, permissions and supported features still matter.

## Three approaches for fictional ASG

| Approach | Choose when | Avoid when | Owner to involve |
|---|---|---|---|
| Authorized service API | One customer's exact current ticket/account status or an update | Heavy batch analytics | App and security teams |
| Data 360 ingestion | Repeated unified joins, historical analysis, feature requiring native materialization | Every-second source accuracy without freshness plan | Data engineering |
| Data 360 Zero Copy federation | Supported Snowflake datasets, low-copy architecture, acceptable predicate/query latency | Desired feature unsupported for federated DLO/DMO | Snowflake and Data 360 admins |

### Crucial feature restrictions

Salesforce's **Zero Copy Data Federation Supportability** documentation lists supported features including data spaces, batch transforms, batch calculated insights, identity resolution, segmentation, activation, and external-DLO querying. It also lists **unsupported** features including streaming transforms, near-real-time identity resolution, rapid segmentation/activation, and some schema changes. **Search-index support for federated mappings has acceleration/caching conditions; check exact DMO mapping support.** Never imply every DMO is directly indexable under federation.

## Decision tree

1. **Must the answer reflect the committed current value?** Choose an authenticated read service/API with a timestamp, or assess a source-backed API gateway. Querying a federated warehouse can be acceptable only with a verified freshness/consistency contract.
2. **Is the use case cross-source analytics?** Evaluate harmonization and reuse through Data 360, with source/model mapping and governance.
3. **Is there an index/search requirement?** Confirm acceleration/cache or native ingestion requirements in official supportability documentation.
4. **Could Snowflake query rate explode?** Test predicate pushdown, scan patterns, query plan, caching, credits, concurrency and P95.
5. **Does the consumer need a write?** Zero Copy is not a write-through transaction strategy; use a controlled authoritative action.

## Example architecture alternatives

- **MVP:** keep Snowflake as analytics source; use live ticket API for status, separately index approved policies for retrieval. Lowest initial scope and clearest access boundary.
- **Unified service context:** use Data 360 for aggregated customer interactions and identity correlation; still use the live service for exact mutable status.
- **Warehouse-heavy reporting:** evaluate federation with proof-of-concept queries at realistic concurrency before committing to latency or cost.

## Proof of concept test matrix

| Test | Acceptance evidence |
|---|---|
| Correctness | 20 sampled accounts match authoritative source for approved fields |
| Access | Cross-account reads denied at service/policy layer |
| Performance | Measured P50/P95 including warehouse queue and network |
| Freshness | Capture as-of timestamp, cache age and source update latency |
| Cost | Credits/compute per 1,000 allowed lookups at expected concurrency |
| Feature support | Demonstrate required transform/index/identity feature in licensed org |
| Recovery | Timeout, unavailable warehouse and partial-data behavior |

**Sources:** [Zero Copy supportability](https://help.salesforce.com/s/articleView?id=data.c360_a_byol_data_federation_supportability.htm&language=en_US&type=5) · [Data 360 architecture](https://developer.salesforce.com/docs/data/data-cloud-dev/guide/dc-architecture.html).
