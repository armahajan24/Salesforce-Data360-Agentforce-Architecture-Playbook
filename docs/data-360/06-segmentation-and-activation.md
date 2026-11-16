# 06 — Segmentation, calculated context and activation

**Segmentation** selects a population based on records and calculated attributes. **Activation** sends eligible results to downstream destinations. A segment definition is a business contract and a privacy decision, not just a filter.

## Fictional example: support-risk outreach

An operations team wants to contact customers with **three or more service requests in the last 30 days**, provided they have valid contact consent and are not in active dispute resolution.

1. Create a trustworthy request count by customer and time window.
2. Confirm deterministic identity and source-correct account relationships.
3. Evaluate explicit opt-in/opt-out and contact preferences at the point of activation.
4. Exclude sensitive or unsupported channels; define precedence if a customer qualifies for multiple segments.
5. Calculate estimated audience size and a suppression test before activation.
6. Monitor delivery, drift and reversals, including if consent is withdrawn.

### Example segment contract

| Property | Value |
|---|---|
| Population grain | Unique authorized customer identity |
| Eligibility | `open_or_closed_requests_30d >= 3` |
| Exclusions | Consent missing; active dispute; legally restricted |
| Refresh | Daily, with explicit freshness label |
| Activation target | Fictional permitted service outreach system |
| Audit | Definition version, run timestamp, eligibility/suppression totals |

**Not a default Agentforce pattern:** a live agent answering a ticket-status question does not require an activated segment.

## Problems to detect

- **Overcounting:** one individual linked to two accounts, or a many-to-many join duplicating requests.
- **Consent lag:** customer opts out after segment calculation but before downstream delivery.
- **Destination policy mismatch:** target accepts fields that shouldn't be exported.
- **Priority conflicts:** one person in both retention and no-contact audiences.
- **Drift:** a segment's rule changes without consumer approval.

## Metrics

Eligible population, suppressed share, delivery correctness, activation lag, opt-out violations (target zero), invalid/unmatched destination identifiers, and cost/credit consumption. Use a holdout or controlled analysis if claiming an effect on customer outcomes.

**Architecture decision:** Should we activate all unified customers to a marketing tool? **No.** Choose business purpose, consent scope, field minimization and destination controls first.

**Sources:** [Data 360 architecture](https://developer.salesforce.com/docs/data/data-cloud-dev/guide/dc-architecture.html) · [Feature overview](https://developer.salesforce.com/docs/data/data-cloud-dev/guide/dc-features-overview.html).
