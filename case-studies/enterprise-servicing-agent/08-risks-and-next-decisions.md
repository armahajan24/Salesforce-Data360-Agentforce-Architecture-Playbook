# Case 08 — Risks, open assumptions and next decisions

## Risks ranked by trust impact

| Risk | Severity | Detection | Mitigation and owner |
|---|---|---|---|
| Unauthorized account lookup | Critical | T02/T03 negative tests, access audit | Server-side entitlement, security lead |
| Unapproved policy exposed | Critical | Staff-only document retrieval tests | ACL-trimmed index, knowledge/security |
| Update falsely reported | Critical | Receipt missing / timeout case | Strongly typed response state, engineering |
| Warehouse value described as current | High | Source timestamp discrepancy | Live API, data owner |
| Policy version stale or chunks missing | High | Source-to-index inventory comparison | Knowledge publishing workflow |
| Identity false-positive | High | Steward review, pairwise sample | Conservative matching / split process |
| P95 latency exceeds service expectation | Medium–high | Tracing by intent/action | Prompt/context reduction, SRE |
| Unexpected credit/compute cost | Medium | Per-intent cost accounting | Workload test, caching where safe, finance |
| Missing human escalation | High | Routing audit and user feedback | Service queue integration, support lead |
| New release changes action parameter | High | Contract regression tests | Versioned metadata, CI release gate |

## Unresolved assumptions to validate before building an org implementation

1. Which service owns committed ticket status and its freshness/availability SLO?
2. Which identity provider and entitlement service can authorize a customer to an account?
3. Are approved policy documents versioned, digitally accessible and classified by audience?
4. What is the license/feature availability for Data 360, federation and Agentforce Testing in the target environment?
5. Can support representatives delegate access or operate on customer records under special roles?
6. Which geographic/privacy regulations and retention policies apply?
7. What budget, concurrency and P95 can the business accept?
8. Are proposed phase-two mutations legally and operationally approved?

## Decision gates

- **Gate A:** finish intent/data discovery, confirm source of truth and policy ownership.
- **Gate B:** pass synthetic fixture and policy retrieval proof of concept.
- **Gate C:** security/operations approve UAT and initial pilot.
- **Gate D:** evaluate real measured resolution, P95, costs and quality before scale.

**Current state of this public project:** documentation and synthetic examples only. No external systems are connected, no Salesforce org has been provisioned, and there are no observed success metrics.
