# 01 — Architecture decision matrix

A good architecture answer begins with **constraints and outcomes**, then compares alternatives. Product-first diagrams miss freshness, authorization, operational and cost trade-offs.

## Start with six decisions

1. **Outcome:** which user journey improves, what is the measured baseline and who owns the metric?
2. **Authority:** which system is the source of truth, and which writes are permissible?
3. **Freshness:** seconds vs minutes vs daily? Is stale data permitted in the actual response?
4. **Entitlement:** who can read or change which record and why?
5. **Flow:** deterministic transaction, informational search, analysis, or a combination?
6. **Operations:** cost, P95, failure recovery, support ownership, release/rollback.

| Need | Primary candidate | Alternative | No-go signal |
|---|---|---|---|
| Current ticket status | Authenticated status API | Federated view with verified consistency | Data refresh delay unknown |
| Historical cross-channel trends | Data 360 mapped DMO + insight | Warehouse SQL | No recurring reuse or governed access |
| Semantic policy answers | Approved retrieval + citations | Simple FAQ/decision tree | No authoritative corpus |
| Change profile preference | Flow/Apex/domain service with confirmation | Manual service rep | No field-level entitlement or audit |
| Sync data changes | CDC/stream or batch by SLO | Periodic pull | No replay/backfill plan |
| Cross-system person view | Identity resolution + source IDs | Explicit master ID in upstream system | No match labels or false-match controls |
| Narrow deterministic FAQ | Decision tree / rule-based | LLM+RAG | Hallucination risk exceeds benefit |

## Illustrative constraints

- Aster Service Group accepts hourly freshness for weekly contact-volume dashboards, **not** for status after an account update.
- A customer may belong to multiple accounts; a linked profile is not permission to see all accounts.
- A question about a return policy needs an approved effective document; customer-specific refund state requires an authoritative transactional source.

## Questions for architecture review

- What happens if Snowflake is unavailable for 30 minutes?
- If we cannot access a customer's ticket, does the system leak its existence?
- Can a revoked permission continue to influence a cached answer?
- Are event retries idempotent, and how do we detect lost updates?
- What changes if the system must handle 10x more users or add another country?

## Decision record

Use [`templates/architecture-decision-record.md`](../../templates/architecture-decision-record.md). An ADR should explain alternatives rejected and revisit triggers, not only the chosen technology. Refer to the [fictional ADRs](../../case-studies/enterprise-servicing-agent/03-options-and-adrs.md).

**Executive explanation:** "For live account status we need an authoritative secure read; for customer context and analysis we may use Data 360 and Snowflake; for policy questions we need governed RAG; for updates we use confirmed typed actions. Those are different workloads, so using one storage pattern for all would add avoidable risk."
