# Case study — Aster Service Group (ASG) servicing assistant

> **All details are invented for a public architecture exercise.** ASG is a fictional multi-region subscription-support company; every persona, account, policy, benchmark, number and system design in this case is synthetic. This exercise does not describe any actual customer engagement or production deployment.

## Business narrative

ASG supports customers with account preferences, service-request progress and subscription-policy questions. Today, customers wait while support specialists check separate systems and read internal-approved documentation. Leadership wants consistent answers, more convenient self-service and less repetitive work **without losing trust or violating customer access**.

The fictional enterprise uses a Snowflake warehouse for historical customer and request analytics, a transactional account/ticket service for authoritative current state, a CRM service console for human support, and a document management workflow for approved policies. No vendor license or external integration is assumed to be enabled.

## What we will design

**MVP:** authenticated account overview, verified ticket status, policy/product guidance with citations and safe human handoff. **Potential phase two:** tightly constrained profile preference update after explicit confirmation. Not included: payments, refunds, cancellations, account deletion, credit decisions, and autonomous cross-system writes.

## Read the case in sequence

1. [Discovery and requirements](01-discovery.md) — stakeholder questions, scope, acceptance.
2. [Reference architecture](02-architecture.md) — end-to-end components, data and trust boundaries.
3. [Options and ADRs](03-options-and-adrs.md) — why the chosen integration approach is appropriate.
4. [Controlled update](04-secure-account-update.md) — authentication, authorization, confirmation and idempotency.
5. [Test strategy](05-tests-and-acceptance.md) — negative paths and release gates.
6. [KPIs and rollout](06-kpis-and-rollout.md) — baseline, economics, pilot design.
7. [Presentation script](07-presentation-and-stakeholder-script.md) — how to explain it in natural language.
8. [Risk and open question review](08-risks-and-next-decisions.md) — operational dependencies and ownership.

## Success is deliberately not pre-claimed

There is no real pilot, live Salesforce environment or validated system architecture behind this case. Desired outcomes, numeric thresholds and costs below are **planning examples** that require sponsor agreement and measurement. They are *not observed metrics*.

## Supporting materials

- [End-to-end diagram](../../diagrams/end-to-end-architecture.md)
- [Servicing sequence](../../diagrams/servicing-agent-sequence.md)
- [Write sequence](../../diagrams/secure-update-sequence.md)
- [Synthetic example fixtures](../../labs/data/)
- [Golden questions](../../labs/evaluation/golden_questions.json)
