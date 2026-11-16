# Learning pathways

**Path A — Salesforce developer (6 sessions)**

1. [Data 360 foundations](docs/data-360/01-foundations-and-object-model.md), [keys and data quality](docs/data-360/03-primary-keys-and-quality.md).
2. [Data ingestion](docs/data-360/02-ingestion-and-freshness.md), [transforms](docs/data-360/05-transforms-and-sql.md).
3. [Agentforce building blocks](docs/agentforce/01-agent-architecture.md) and [action design](docs/agentforce/04-actions-and-tool-contracts.md).
4. [Retrieval architecture](docs/agentforce/02-knowledge-and-retrieval.md) and [evaluation](docs/agentforce/03-rag-evaluation.md).
5. [Integration patterns](docs/enterprise-architecture/02-integration-and-eda.md), [security](docs/enterprise-architecture/03-security-and-governance.md).
6. [Case study](case-studies/enterprise-servicing-agent/README.md), [test plan](case-studies/enterprise-servicing-agent/05-tests-and-acceptance.md).

**Path B — Solution architect (4 workshops)**

1. Draw boundaries and decide on [Data 360 vs live services](docs/enterprise-architecture/01-decision-matrix.md).
2. Workshop identity, [unification](docs/data-360/04-identity-resolution.md), [federation](docs/data-360/07-zero-copy-snowflake.md) and data contracts.
3. Threat-model [entitlements](docs/enterprise-architecture/03-security-and-governance.md), [transactions](case-studies/enterprise-servicing-agent/04-secure-account-update.md), and [availability](docs/enterprise-architecture/04-nfrs-and-observability.md).
4. Create an [ADR](templates/architecture-decision-record.md), [pilot scorecard](case-studies/enterprise-servicing-agent/06-kpis-and-rollout.md), and [risk register](templates/risk-register.md).

**Path C — Solution delivery lead (3 workshops)**

1. Facilitate [discovery](docs/solution-delivery/01-discovery-and-scope.md) and capture the [requirements questions](case-studies/enterprise-servicing-agent/01-discovery.md).
2. Explain options and success criteria with [simple trade-offs](docs/solution-delivery/02-stakeholders-and-tradeoffs.md).
3. Conduct a [pilot and steering review](docs/solution-delivery/03-kpi-delivery-and-change.md), presenting guardrails, decisions, and results as evidence, never as invented success claims.

**Learning technique:** for each topic say (1) what it solves, (2) when *not* to use it, (3) a counterexample, (4) one failure mode, (5) one metric. Use the [short revision sheet](cheat-sheets/one-line-revision.md) at the end.
