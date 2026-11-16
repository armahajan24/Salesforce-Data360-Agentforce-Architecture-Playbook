# Case 03 — Architecture alternatives and decision records

## ADR-001: Ticket status source

- **Context:** customers expect an accurate answer after an agent changes their ticket.
- **Options:** (A) query a daily Snowflake table; (B) query Data 360 ingested request DMO; (C) call an authenticated authoritative ticket API.
- **Decision for phase one:** C, because current status is a transaction-oriented read and the data source owner can provide a scoped API with timestamp and SLA. A and B may support reporting and summarization, not current truth without a verified freshness contract.
- **Risk:** service API latency/unavailability. **Mitigation:** bounded timeout, protected backoff, honest unavailable response, human escalation.
- **Revisit when:** a supported federated source is proven to meet currentness, authorization, P95 and cost requirements.

## ADR-002: Data 360 adoption

- **Options:** (A) mandatory single data layer for all intents; (B) selective Data 360 for identity/insights and reusable context; (C) no Data 360 in MVP.
- **Decision:** B as a target possibility, but allow C for an initial narrow read-only pilot if no cross-source use case requires Data 360. Prove identity and insights value before additional ingestion or federation costs.
- **Risk:** fragmented permissions and additional complexity. **Mitigation:** centralized authorization contract, data ownership map and explicit provenance.

## ADR-003: Policy retrieval

- **Options:** (A) static prompts with pasted policy; (B) general semantic retrieval; (C) approved, versioned retrieval with permission trimming, citations and abstention.
- **Decision:** C. A becomes stale; B risks wrong versions and internal-only guidance. A deterministic FAQ can still outperform RAG for extremely narrow invariant rules.
- **Risk:** missing chunks, stale policies, injection. **Mitigation:** content governance, retrieval golden sets and index/source inventory reconciliation.

## ADR-004: Mutation boundary

- **Options:** (A) agent-generated SQL or unrestricted API; (B) direct, unrestricted Flow action; (C) typed controlled service/Flow/Apex with confirmation and reauthorization.
- **Decision for phase two:** C. Phase one has no mutation tool. Deny unsupported values/fields; use idempotency receipts and audit. Rollout requires extra security approval.

## ADR-005: Cache and performance

- **Decision:** policy excerpts may cache by document-version, access scope and locale; live ticket values should not be cached without approved max-age and invalidation semantics. Prefer removing irrelevant prompt context over relying on a stale high-hit cache.
- **Revisit when:** measured P95, cost and freshness justify a new design.

## Comparative scorecard (qualitative, not a product benchmark)

| Pattern | Freshness | Reusability | Complexity | Best fit |
|---|---|---|---|---|
| Live status API | High if API authoritative | Medium | Low–medium | Single-account current status |
| Batch Data 360 DMO | Tied to refresh | High | Medium | Analytics, stable unified context |
| Streaming ingestion | Near-real-time, async | High | Medium–high | Incremental analytical context |
| Snowflake federation | Source-consistent per query contract | High | Medium–high | Governed external tables where features supported |
| RAG policy search | Index/update dependent | High for docs | Medium | Versioned knowledge questions |

These are design hypotheses. Measure in the target platform before treating a row as a performance guarantee.
