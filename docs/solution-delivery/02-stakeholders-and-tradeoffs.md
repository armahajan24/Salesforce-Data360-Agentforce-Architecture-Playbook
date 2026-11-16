# 02 — Stakeholder influence, architecture decisions and difficult conversations

Technical correctness is insufficient if the sponsor, operations and security teams disagree about what success means. Use plain explanations, visible options, decision logs and named owners to reduce surprises.

## Simple architecture language

- **Live status vs cached context:** "For changing ticket status we call the source directly; for trends we use a reusable data platform view."
- **RAG vs transactional API:** "Documents explain policies; an API verifies an individual account's current state."
- **Agent vs workflow:** "The AI understands the request and speaks naturally; verified code decides whether an update is permitted."
- **Zero Copy trade-off:** "We avoid copying all the data, but still pay attention to supported features, query time and warehouse compute."
- **Security:** "An agent is only allowed to see what the signed-in user could see through an approved service."

## Decision communication method

1. **State the common outcome:** e.g., reduce repeat contact without exposing protected records.
2. **Present 2–3 real alternatives:** options, user impact, dependency, cost and risk.
3. **Define recommendation and assumption:** "I recommend read-only phase one because account updates need a higher validation bar."
4. **Ask for explicit decision:** sponsor owns scope, security owns control acceptance, operations owns handoff readiness.
5. **Record in ADR and communicate:** decision date, included/excluded scope, acceptance and revisit trigger.

## Scope disagreement scenario (fictional)

A feature was removed from the release scope and documented by email. After launch, stakeholders say it was business-critical. Avoid arguing, "But I emailed you." Say:

> "The scope change was documented and our validation covered the reduced release. I now understand that this missing capability has a higher business impact than we captured. I will quantify who is affected, assess safe interim handling and bring options to the next decision meeting. For future releases, we will require explicit business acceptance of high-impact exclusions, not just an email acknowledgment."

Then improve the process: live review of acceptance scenarios, signed release scope, named business approver, owner of each exclusion and visible release notes. Do not assert a delivery date without an approved estimate and dependencies.

## Stakeholder tools (not software-dependent)

- A one-page **decision table** rather than a dense technical slide.
- **DACI/RACI** ownership matrix for decisions, delivery, consultation and communications.
- A **risk register** with impact and mitigation.
- A **weekly scorecard** with eligible resolution, quality, CSAT, escalation and spend.
- A **demo script** with both successful cases and failure/denial paths.

## Stakeholder communication principle

"I want stakeholders to understand the trade-off before signing off, so I explain each choice with a customer example, what we gain, what we give up, and how we will measure whether the decision worked."
