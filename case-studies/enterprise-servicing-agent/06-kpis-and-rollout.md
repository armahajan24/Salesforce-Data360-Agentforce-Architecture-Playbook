# Case 06 — KPI plan, pilot scorecard and phased rollout

## The sponsor must commit to a balanced outcome

**Primary outcome:** increase **correctly resolved eligible customer requests** while preserving security and customer satisfaction. A high containment rate is not proof of resolution and can be achieved by frustrating customers into leaving.

## Metric contract

| Metric | Denominator / calculation | Guardrail / owner |
|---|---|---|
| Eligible automated resolution | Correctly closed without human action / eligible pilot intents | Quality reviewed, product owner |
| Same-issue repeat contact | Follow-up within approved window / resolved cohort | Watch for hidden failure; support owner |
| Policy answer groundedness | Claims supported by approved evidence / sampled claims | Content owner |
| Correct citation rate | Citation supports specific factual claim / sampled claims | Knowledge owner |
| CSAT | Same survey/capture method, comparable cohorts | Support lead |
| P95 latency | Timed request distribution by intent and channel | SRE |
| Cost per correct resolution | Total attributed variable spend / correct eligible resolutions | Finance |
| Unauthorized disclosure/write | Count of confirmed security violations | Critical, target 0, security |
| Human escalation quality | Routed to correct queue with sufficient sanitized context | Support lead |

## Fictional measurement example — NOT a pilot result

Assume for planning: 10,000 monthly requests; 40% in scope; 75% of eligible routed to agent; 60% of those correctly resolved without human action. Then:

```
Eligible = 10,000 × 0.40 = 4,000
Agent-tried = 4,000 × 0.75 = 3,000
Correctly automated = 3,000 × 0.60 = 1,800
All-request automation = 1,800 / 10,000 = 18%
Eligible automation rate = 1,800 / 4,000 = 45%
```

This arithmetic is merely a **scenario** and should never be framed as a real deployment outcome or guaranteed improvement. Account for repeat contacts, escalations, human review, incident costs and channel mix.

## Rollout approach

| Stage | Evidence required | Decision-maker |
|---|---|---|
| Design | Intent list, source/API contracts, access matrix | Sponsor + product + security |
| Synthetic POC | Contract tests, RAG golden set, safe denial flows | Engineering + knowledge |
| Sandbox/UAT | End-to-end cases and security/latency tests | Security + SRE + product |
| Limited pilot | Controlled cohorts, monitored outcomes and escalation | Sponsor + support |
| Scale | Stable guardrails, measured ROI, approved operations | Steering group |

## Pilot analysis

Segment by authenticated customer vs support rep, account type, product category, intent, and human escalation. Compare to a baseline cohort with equivalent case mix and measurement methodology; if sample sizes are small, report uncertainty. Monitor adverse shifts immediately, not only after the experiment concludes.

## Exit and rollback

Pause auto-resolution if critical security breach, incorrect account update, evidence integrity failure, unresolved systemic policy mistake, or unacceptable outage. Fall back to human handling and preserve incident trace IDs; do not retain sensitive raw content unnecessarily.

**Stakeholder line:** "We will optimize for correct automated resolution and satisfaction, with zero tolerance for unauthorized access—not for raw deflection."
