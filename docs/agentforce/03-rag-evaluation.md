# 03 — Evaluate RAG: precision, recall, groundedness and refusal

RAG evaluation needs **at least two layers**: (1) did retrieval deliver the right evidence, and (2) did the model use that evidence correctly? End-user satisfaction alone cannot distinguish the two.

## Retrieval metrics

Suppose the evaluator labels relevant passage IDs for a query: `{P01, P02, P03}`. Retriever returns top-3 `{P02, P09, P03}`:

- **Precision@3** = 2 relevant returned / 3 returned = **0.667**.
- **Recall@3** = 2 relevant returned / 3 known relevant = **0.667**.

These are **illustrative** values; the ranking and completeness of human labels control their reliability. Vary `k` and measure rank-sensitive metrics (MRR/NDCG) when needed. `Precision@k` is not the same as citation correctness.

## Answer-level evaluation

| Dimension | Evaluation question | Failure example |
|---|---|---|
| Groundedness | Is every factual claim supported by retrieved evidence? | Adds an unsupported refund promise |
| Citation correctness | Does the cited section say what the answer claims? | Cites a general policy for a specific exception |
| Answer completeness | Were required steps/exceptions included? | Omits approval condition |
| Refusal | Does the agent abstain when evidence is missing? | Invents a policy |
| Access compliance | Was restricted content withheld? | Customer receives staff-only procedure |
| Temporal accuracy | Is effective policy version current? | Quotes superseded v1 |
| Tool correctness | Did it call the right tool with verified inputs? | Guesses account ID |

## Golden set design

Create at least these categories: common positive queries, paraphrases, multi-hop, exact-ID, stale-version, contradictory sources, no-answer, injection attempts, cross-account prompts, malformed/missing data and escalations. Include expected evidence passage IDs, allowed actions, forbidden claims and escalation behavior. See [`labs/evaluation/golden_questions.json`](../../labs/evaluation/golden_questions.json).

## Diagnosing a miss

- **Relevant document never retrieved:** check indexing, source permissions, chunk metadata, top-k, keyword overlap and semantic retrieval.
- **Correct evidence retrieved, answer wrong:** adjust prompt grounding, citation constraints and evidence compactness; inspect answer tests.
- **Only incorrect older version retrieved:** fix effective date/supersession filters; do not patch the answer with a general disclaimer.
- **Good average, bad tail:** inspect per-intent and per-language slices, not only aggregate score.

## Production process

Baseline the current knowledge-assisted service. Use a held-out evaluation set; track results by intent, document version and severity; run regressions on indexing changes, retriever configs and prompts. Human-review critical security/policy failures before broad rollout. Do not optimize solely for a high auto-answer rate.

**Local evaluation exercise:** run `python3 labs/scripts/evaluate_retrieval.py` to score a tiny **synthetic** labeled fixture. It validates math, not Agentforce model quality.
