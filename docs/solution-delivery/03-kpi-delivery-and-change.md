# 03 — KPI contracts, delivery stages and business outcomes

Avoid goals such as "make the agent answer 80% of questions" without defining eligibility, correctness and customer impact. Measure **trustworthy successful resolution**, not merely conversation containment.

## Proposed KPI dictionary

| KPI | Definition | Why |
|---|---|---|
| Eligible automation rate | Successfully resolved, policy-compliant agent sessions / sessions marked eligible for automation | Outcome without rewarding unsafe deflection |
| Containment rate | Sessions without human transfer / all agent sessions | Useful operationally, insufficient by itself |
| Repeat contact | Customers contacting again for the *same issue* within agreed N days / prior resolved cohort | Quality guardrail |
| Correct-answer rate | Reviewer-approved truthful and grounded answers / labeled answer sample | Prevent fluent errors |
| Authorization violation | Confirmed unauthorized disclosures or writes | Critical safety measure; target zero |
| CSAT | Consistently collected satisfaction score by matched channel/cohort | Customer impact |
| P95 latency | 95th percentile wall-clock response by intent | Tail experience |
| Cost per resolved request | Variable platform + API + review/escalation costs / correctly resolved eligible requests | Economic effect |

**Cohorts matter:** include only intended pilot intents; distinguish web, chat, customer and rep usage; inspect sample size and seasonality. Never present a synthetic score as an observed improvement.

## Pilot phases

1. **Discovery (gate):** signed scope, baseline, allowed actions, test cases, data access approvals.
2. **Prototype (gate):** synthetic data, proof of retrieval/source API, P95 and permissions approach.
3. **Sandbox/UAT (gate):** golden sets, denial scenarios, adversarial prompts, human fallback and logs.
4. **Limited pilot (gate):** small approved audience, monitoring, qualitative feedback and a rollback switch.
5. **Controlled expansion (gate):** evidence against KPI guardrails; policy owner and incident operations sign-off.

## Causal claims

Pre/post improvements can be due to volume mix or seasonality. Prefer matched cohorts, phased rollout or an A/B holdout where ethical and operationally feasible, and report sample size plus uncertainty. When a pilot is too small, report directional findings and risks rather than a false precision percentage.

## Cost framework

`Variable cost = LLM + Data 360 / warehouse query + API / compute + retrieval + human review + escalation`.

`Cost per correct automated resolution = variable cost allocated to eligible automated traffic ÷ correctly automated resolutions`.

Use a stable unit, include human fallback and baseline ticket handling cost from finance. Evaluate how the **whole service operation** changes, not whether a chatbot interaction is cheap in isolation.

See [case scorecard](../../case-studies/enterprise-servicing-agent/06-kpis-and-rollout.md) and [measurement template](../../case-studies/enterprise-servicing-agent/07-presentation-and-stakeholder-script.md).
