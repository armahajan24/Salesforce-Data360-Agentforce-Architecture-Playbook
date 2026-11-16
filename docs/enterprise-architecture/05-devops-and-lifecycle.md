# 05 — Agentforce / Data 360 DevOps and release lifecycle

Treat definitions, metadata, test suites, data contracts, index configurations and operational runbooks as versioned deliverables. Not every Data 360 setup artifact is deployable via the same Salesforce metadata mechanism, so keep a manual validation checklist.

## Safe release flow

1. **Design:** approved ADR, source/field contract, access matrix, test cases and owner.
2. **Develop:** build metadata and declarative assets in dev/sandbox, commit to Git with peer review.
3. **Validate:** static checks, Apex/Flow tests, agent regression and retrieval cases, schema/permissions.
4. **Stage:** promote into comparable test/UAT environments, verify dependencies, activation and agent version lineage.
5. **Cutover:** change window, support contact, traffic control, rollback approach and auditability.
6. **Observe:** early-life P95, routing, unauthorized attempts, evidence defects, retries, spend and customer outcomes.

## High-risk deployment drift

- Agent Script metadata versions or dependencies differ between source and target environment.
- Agent published/activated version is not the version validated in UAT.
- Retriever index name exists but source documents, data spaces or chunk indexes differ.
- Flow or Apex action has a changed input schema while the agent still sends stale parameters.
- Test suite passes with one role but runtime users have less permission.

## Concrete validation table

| Artifact | Compare before go-live |
|---|---|
| Agent definition | Selected published version, subagents, route and action bindings |
| Action schema | Parameter names/types, required values, permission sets |
| Knowledge source | Approved inventory, indexed documents/chunks, versions, ACLs |
| Data 360 | Data streams, DLO/DMO mapping, data space policies, supported zero-copy setup |
| Credentials | Named credentials/connected app or approved integration method |
| Test evidence | UAT agent traces, negative scenarios, P95 and document retrieval |
| Fallback | Human handoff, feature switch, safe disablement |

## GitHub repository strategy

This playbook is **not** itself a Salesforce DX project. A separate implementation lab can include `sfdx-project.json`, `force-app/`, manifests, Apex and tests. Keep the educational architecture content here, and link to separately validated deployable examples rather than implying that a Markdown diagram provisions an org.

## CI recommendations

- Markdown link check, secret scan, PII-example scan, Python fixture tests.
- SFDX source validation and unit tests when a future deployable sample is added.
- Agentforce test processes depend on the org release and tooling. Confirm supported commands and Testing Center version before scripting CI.
- Require human review for access-policy and transaction-contract changes; don't auto-promote production agents based solely on aggregate model score.

**Sources:** [Agentforce DX](https://developer.salesforce.com/docs/ai/agentforce/guide/agent-dx.html) · [Agentforce Testing API](https://developer.salesforce.com/docs/ai/agentforce/guide/testing-api-get-started.html).
