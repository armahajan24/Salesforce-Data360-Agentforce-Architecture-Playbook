# 01 — Solution discovery: uncover the real business problem

The sponsor says, "Reduce cost and improve service with an AI agent." That is a direction, **not a measurable requirement**. A solution delivery lead converts it into **eligible workflows, baseline metrics, risk constraints, ownership and a decision cadence**.

## Ask by stakeholder

| Stakeholder | Questions | Expected output |
|---|---|---|
| Sponsor | Which cost/experience outcome matters? What is the target and decision date? | Ranked business outcomes |
| Product owner | Which 2–3 intents are in phase one, and what is expressly excluded? | Intent acceptance criteria |
| Support manager | Top contact reasons, repeat-contact reasons, escalation patterns? | Journey and baseline |
| Data/platform owner | Source of truth, IDs, data freshness, API vs Snowflake access? | Source/relationship map |
| Security/privacy | Customer identity, field access, audit and consent requirements? | Non-negotiable controls |
| Ops/SRE | Volume, concurrency, on-call, uptime/P95, incident handling? | Operational SLOs |
| Knowledge owner | Who approves and versions policies; how quickly do changes publish? | Trusted content lifecycle |

## Sample outputs for fictional Aster Service Group

**Proposed MVP intents:** authenticated account overview, ticket status, policy/product guidance. **Out of scope initially:** balance movement, payments, cancellation and unrestricted updates. **Unknown until measured:** baseline volumes, contact handling time, CSAT, ticket reopens, API latency and cost. **Security gate:** no cross-account disclosure.

## Discovery artifacts

1. Intent inventory with volume, risk, average handling time and eligibility.
2. Journey map showing current friction, handoffs and data lookup steps.
3. Data and access matrix including owner/refresh/consent.
4. Architecture alternatives with assumptions and ADRs.
5. Signed success criteria, testing plan and go/no-go owner.

## Discovery approach in plain language

"I would start by asking for the most frequent service contacts and a baseline of how they are resolved today. Then I would choose a small read-only pilot with the strongest value and lowest risk. I would not promise an automation percentage before we measure how many contacts are actually eligible."

## Harder follow-up: different stakeholder priorities

Finance wants a low cost per contact; support wants customer satisfaction; security wants no leaks. Make the trade-off explicit: a forced deflection metric could damage trust. Define a balanced scorecard and escalation thresholds before implementation. Escalation is often the correct result.

See [workshop template](../../templates/discovery-workshop-agenda.md) and [case study discovery](../../case-studies/enterprise-servicing-agent/01-discovery.md).
