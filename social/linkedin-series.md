# LinkedIn series — drafts for approval (not scheduled)

> **Publishing rule:** replace `[REPO_URL]` with a real public URL after review. These posts discuss educational examples, not private production implementations or proprietary materials. Do not say the Agentforce case study is deployed or tested in a Salesforce org.

## Post 1 — Launch

I’ve been organizing my learning around **Salesforce Data 360, Agentforce and enterprise AI architecture** into a public, decision-first playbook.

The big lesson: building an agent demo is not the same as designing a trusted servicing experience. You have to choose where data lives, how fresh it must be, who can access it, how actions are controlled and how outcomes will be measured.

The playbook covers Data 360 modeling, Snowflake/Zero Copy trade-offs, identity resolution, grounded RAG, Agentforce action design, observability, CI/CD and stakeholder delivery. It also includes a fully fictional servicing-agent case study, architecture diagrams, synthetic data and small validation exercises.

Explore it here: [REPO_URL]

Which trade-off comes up most often in your architecture discussions: data freshness, security, cost or reliability?

#Salesforce #Data360 #Agentforce #EnterpriseAI #SalesforceArchitect

## Post 2 — Zero Copy is an architecture choice

When an agent needs current account information, my first question is not “Can we ingest it into Data 360?” It is **“Which system is authoritative, and how fresh must this answer be?”**

I compare three options: secure live API for exact operational state; selective Data 360 ingestion when reusable/unified data is valuable; and federation when the supported zero-copy features fit the workload. Each has different freshness, latency, cost and governance implications.

I documented the decision tree with a fictional Snowflake servicing scenario: [REPO_URL]

#Salesforce #Data360 #Snowflake #Architecture

## Post 3 — Trustworthy servicing agents

A customer asks, “What is my ticket status?” The agent shouldn’t guess an account identifier from conversation text or bypass normal record access just because it has a retriever.

A safer design: authenticated session → server-side entitlements → authoritative read action → formatted answer with a timestamp. For updates, add typed inputs, explicit confirmation, reauthorization, idempotency and a verified receipt before saying “done.”

The public fictional case study includes a sequence diagram and action contract: [REPO_URL]

#Agentforce #Salesforce #AIEngineering

## Post 4 — RAG quality beyond a nice demo

A fluent answer is not evidence of a good retrieval system. I measure **retrieval recall@k**, **precision@k**, source freshness, groundedness, refusal quality and citation correctness, using golden questions and negative cases.

In the playbook I show how policy versioning, hybrid search, chunk boundaries and scope filters affect answers—plus a small synthetic evaluation fixture: [REPO_URL]

#RAG #Agentforce #Data360 #AIQuality

## Post 5 — The business outcome matters

If an AI servicing agent has no agreed eligibility rules or baseline, a “containment rate” can be misleading. I would ask business and operations teams to define successful resolution, repeat contact, CSAT, policy accuracy, cost per eligible resolved request and human escalation reasons *before* a pilot.

My playbook includes a fictional KPI scorecard, phased rollout and stakeholder decision template: [REPO_URL]

#SalesforceArchitecture #Agentforce #DigitalTransformation
