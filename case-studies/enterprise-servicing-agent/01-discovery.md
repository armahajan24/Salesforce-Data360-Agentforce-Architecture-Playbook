# Case 01 — Discovery, sponsor questions and MVP scope

## First meeting: 60-minute workshop

Do not open with a Salesforce product pitch. Start with the business journey and confirm a cost/quality trade-off. Ask sponsor, operations, data, security and knowledge owners to meet together.

### Suggested dialogue

**Sponsor:** "What do we actually want to improve? Cost per request, resolution speed, or customer satisfaction? How will we know in 90 days?"

**Service lead:** "Which three contact types consume the most time? What percentage require human judgment, verification or a privileged change? Why are requests reopened?"

**Product owner:** "Which intents can we safely automate today? What is the preferred human handoff experience? Which customer channels are in scope?"

**Data owner:** "Where do account status and ticket updates live today? Is Snowflake an analytic copy or authoritative for any of them? Which IDs link accounts, contacts and service tickets?"

**Security/privacy:** "How is a caller verified? Can one person access multiple accounts? Which fields are restricted, and how do we audit disclosures? Is there any regulatory/consent boundary?"

**Knowledge owner:** "Which policy documents are approved and current? Who publishes replacements and retracts superseded guidance?"

**Operations/SRE:** "What are peak volume, P95 budget, outage process, escalation queue, and on-call responsibilities?"

## Hypotheses, not facts

ASG's leadership suspects repetitive ticket status questions are a good first use case. We would **validate the assumption with ticket-level data**: volume, handling time, whether status is available from a reliable API, exceptions, language and privacy concerns.

### Requirements inventory (example)

| ID | Requirement | Acceptance evidence | Owner role |
|---|---|---|---|
| FR-1 | View an account summary | Only verified member sees allowed fields | Service + security |
| FR-2 | Check ticket status | Approved ticket, current source timestamp, safe error | Ticket service owner |
| FR-3 | Explain policy | Approved effective source citation or abstention | Knowledge owner |
| FR-4 | Escalate uncertain/denied issues | Channel routes to correct human queue | Support lead |
| NFR-1 | Unauthorized data exposure | Zero confirmed exposure in negative test suite | Security lead |
| NFR-2 | P95 and uptime | Threshold proposed, load tested, accepted | SRE + sponsor |
| NFR-3 | Cost and quality | Baseline and pilot scorecard | Finance + product |

## Define the initial eligible population

A customer is eligible for phase-one automation **only if** they are authenticated, the requested account is authorized, the question matches the approved intent set, the required source is available, and there is no high-impact exception requiring review. If a case is ambiguous, escalation may be the correct outcome.

## Scope control

**In:** account-overview fields approved by field-level policy; status for ticket owned/authorized to customer; published policy answer; safe ticket handoff.

**Out:** modifying payments, identity attributes, eligibility decisions or cancellation; claiming live status from delayed analytics; unapproved staff-only policy; automatically changing permissions.

## Deliverables at end of discovery

Signed intent priority list, baseline definition, field/source matrix, identity/entitlement data flow, API contract owners, document-index approval process, ADRs, risk log and release gate. Record unanswered questions explicitly, e.g. "Does the CRM API provide current status with updated_at?"—do not make assumptions invisible.
