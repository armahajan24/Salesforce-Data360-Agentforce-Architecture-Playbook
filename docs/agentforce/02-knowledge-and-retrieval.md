# 02 — Grounded retrieval: RAG, vector search, hybrid search and citation quality

An agent may be fluent yet wrong when retrieval returns irrelevant, outdated or restricted chunks. Retrieval is an **information system** with its own data contracts, permissions, quality metrics and release process.

## Pipeline and boundaries

1. Content owner approves sources and specifies audience, version, effective date and expiration.
2. Extraction yields normalized content with document and section IDs, avoiding unintentionally copying secrets.
3. Chunking keeps policy exceptions near their rule; enrich chunks with metadata.
4. Indexing supports semantic/vector search and, where useful, keyword/hybrid search.
5. Query handling applies tenant, audience, permission, locale, version and effective-date filters.
6. Retrieval returns bounded ranked candidates with provenance.
7. Generation cites evidence or explicitly refuses unsupported conclusions.

## When to choose search types

| Query | Default hypothesis | Why |
|---|---|---|
| "What is the return window?" | Semantic or hybrid | Natural language wording varies |
| "What does policy ASG-RET-003 say?" | Keyword or hybrid | Exact identifier is decisive |
| "Can I return after 40 days?" | Hybrid + effective-date policy filter | Need exact limits and exceptions |
| "What is my current account balance?" | **Not RAG**: authoritative API | Dynamic structured value, identity-sensitive |

Hybrid is not automatically better: test with a labeled corpus and real query distribution. An index may contain a document but not the necessary chunk; **source presence ≠ indexed chunk presence**.

## Query design principles

- **Context shaping:** send the smallest evidence set that justifies the answer. Avoid pasting full unfiltered documents into orchestration prompts.
- **Security trimming:** filter before retrieval; avoid retrieving data only to ask the LLM not to reveal it.
- **Versioning:** prefer current effective policy, record source version in answer metadata.
- **Citation verification:** confirm the cited excerpt supports the exact claim and includes exceptions.
- **No-answer behavior:** offer safe handoff when evidence is absent or conflicting.

## Failure diagnosis example

A policy document exists in the source library but never appears in any answer. Distinguish: content sync failure; chunk/index creation missing; wrong data space; source audience excluded; metadata filter mismatch; low top-k; relevance/reranking issue; model ignores retrieved context. Start by inspecting each stage before adjusting the prompt.

## Verification exercise

With a fictional return policy of 30 days and a 7-day damaged-item exception, test prompts for 20, 35 and 45 days; if the exception is not present in retrieved evidence, the agent should abstain rather than invent it. Add a superseded policy to confirm correct version filtering.

**Sources:** [Data 360 feature overview](https://developer.salesforce.com/docs/data/data-cloud-dev/guide/dc-features-overview.html) · [Agentforce actions](https://developer.salesforce.com/docs/ai/agentforce/guide/ascript-ref-actions.html).
