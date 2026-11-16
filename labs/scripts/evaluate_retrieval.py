#!/usr/bin/env python3
"""Illustrative precision@k and recall@k calculation on synthetic evidence IDs."""
import json
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / 'evaluation' / 'golden_questions.json'

def precision_recall(relevant, retrieved, k):
    """At most k unique retrieved passage IDs. Zero relevant means no-answer test."""
    if k < 1:
        raise ValueError('k must be >= 1')
    rel = set(relevant)
    deduped = list(dict.fromkeys(retrieved))[:k]
    hits = len(rel.intersection(deduped))
    precision = hits / len(deduped) if deduped else 1.0 if not rel else 0.0
    recall = hits / len(rel) if rel else (1.0 if not deduped else 0.0)
    return (precision, recall)

def main():
    data = json.loads(DATA.read_text(encoding='utf-8'))
    for item in data:
        p, r = precision_recall(item['relevant_passage_ids'], item['retrieved_passage_ids'], 3)
        print(f"{item['id']}: precision@3={p:.3f} recall@3={r:.3f}")
    print('Note: tiny synthetic dataset; not a live RAG/Agentforce evaluation.')

if __name__ == '__main__':
    main()
