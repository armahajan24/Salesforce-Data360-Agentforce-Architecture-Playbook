# Case 07 — 8-minute stakeholder walkthrough (natural language)

**1. Business problem (45 seconds)**

"Aster Service Group wants to reduce repetitive service work and make it easier for customers to get accurate answers. Today a rep often has to look at several systems. Instead of assuming AI will reduce cost, I'd start with the top customer journeys and what success means to the business."

**2. Discovery and scope (60 seconds)**

"I'd speak with the sponsor, product owner, support manager, data owners, knowledge manager and security team. I'd ask which requests are frequent, which need current data, which are safe to automate and which need a person. I would start with three narrow read-only intents: account overview, ticket status and product or policy questions."

**3. Architecture (2 minutes)**

"The customer signs into a verified channel. Agentforce handles conversation and chooses a scoped subagent. For exact ticket or account status, I call a secure authoritative API because that information can change quickly. For policy guidance, I retrieve the currently approved document and cite it. Data 360 can bring useful unified and historical context from Snowflake where it adds value, but I would not force every live request through an asynchronous data pipeline."

"The most important boundary is access. The agent can never assume account ownership from a typed email or account number. A backend checks the user's identity and record permissions every time. If the source is unavailable or policy evidence is missing, the agent explains that it cannot verify the answer and offers human support."

**4. Technical trade-offs (90 seconds)**

"I would compare secure APIs, Data 360 ingestion and Snowflake federation based on freshness, query latency, feature support, security and cost. I would test the chosen data paths with realistic load, because Zero Copy is not automatically suitable for every search or transform. In later phases, an account preference update would use typed Flow/Apex or a domain API, explicit confirmation, idempotency and a verified success receipt."

**5. Delivery and metrics (90 seconds)**

"I'd build a synthetic proof of concept, run a golden test set including wrong-account and policy-conflict questions, then pilot with a small approved audience. Before launch I want clear baselines: eligible service volume, correct resolution, repeat contact, CSAT, policy accuracy, P95 and cost per resolved request. I would share a weekly scorecard with business and security owners and expand only when the guardrails hold."

**6. Close (45 seconds)**

"The aim is not to make an impressive chat demo. It's to make an accurate, secure and measurable servicing experience. The architecture choices follow the business need, and we adjust them based on observed results."

## Hard follow-up answers

**Why not ingest all Snowflake data?** "Not every question needs copied, transformed data. A live request may require current truth; a historical trend may benefit from Data 360. More ingestion increases lifecycle, cost and policy work."

**What if the agent makes a mistake?** "Restrict actions, use grounding, evaluate failures by severity, offer escalation and capture traces. Security and transactional safety are enforced outside the model."

**What if stakeholders want account writes immediately?** "I would offer the read-only pilot while defining a separate approved write workflow, with legal/security review, confirmation, idempotency and stronger testing."

**What if the target isn't met?** "I'd present baseline vs actual and causal hypotheses—retrieval gaps, scope, latency, handoff—along with options and a revised milestone for approval, not hide the gap."
