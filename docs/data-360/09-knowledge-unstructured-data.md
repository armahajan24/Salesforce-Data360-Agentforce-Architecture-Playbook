# 09 — Unstructured data: documents, transcripts, chunking and retrieval

Documents should not become an indiscriminate knowledge dump. First select **approved, versioned, access-scoped** material with business owners and an expiry/update workflow.

## Pipeline

`Approved sources → extraction/metadata → document classification → chunking → embeddings/index → hybrid/vector retrieval → reranking/filter → grounded response with citations`.

Choose chunk boundaries around semantic units (policy section, product procedure); preserve title, source ID, version, effective date, section and permitted audience in metadata. Embeddings enable semantic retrieval; keyword search is valuable for exact product IDs, ticket codes and unusual terms. Hybrid search can combine the strengths.

## Fictional approved corpus

| Document | Version | Effective date | Audience | Search behavior |
|---|---|---|---|---|
| `ASG_Returns_Policy_v3` | 3 | 2026-01-01 | Customers | Cite exact eligibility rule |
| `ASG_Service_Hours_v2` | 2 | 2026-01-01 | Customers | Cite hours and exceptions |
| `ASG_Internal_Escalation_v1` | 1 | 2026-01-01 | Staff only | Never retrieve for customer |

### Document failure modes

1. **Indexing gap:** document in source but zero chunks in index → no amount of prompt tuning can retrieve it. Compare source inventory to indexed item/chunk counts.
2. **Stale version:** older policy surfaced after new one is effective → filter by effective date and superseded status.
3. **Permission mismatch:** internal document indexed in a public retriever → enforce ACL during query/index, not simply in a response instruction.
4. **Overlong context:** irrelevant snippets overwhelm response and slow LLM orchestration → cap evidence, rerank, deduplicate.
5. **Partial citation:** chunk omits a critical exception → adjust chunk overlap/section boundaries and include source paragraph IDs.

## Retrieval strategy

Start with 20–50 labeled questions, including contradictions, version transitions, no-answer and unauthorized questions. Tune chunking/search/reranking against **recall@k** and **precision@k**, then evaluate groundedness, faithfulness, refusal quality and citation correctness end-to-end.

Do not index raw calls/transcripts into a customer-facing retriever by default: transcription accuracy, privacy, consent, retention and source credibility require separate review. Prior case notes may be inappropriate as a source of policy truth.

**Sources:** [Data 360 unstructured data and search](https://developer.salesforce.com/docs/data/data-cloud-dev/guide/dc-features-overview.html) · [Data 360 architecture](https://developer.salesforce.com/docs/data/data-cloud-dev/guide/dc-architecture.html).
