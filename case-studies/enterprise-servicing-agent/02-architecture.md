# Case 02 — Reference architecture with data and control boundaries

## Proposed architecture (illustrative)

**Channel:** authenticated customer portal or authenticated human-support console. The channel issues a verified session principal and allowed account context; the agent never trusts a name or an account ID supplied only in free text.

**Conversation:** Agentforce orchestrates scoped subagents for account, status, policy and handoff. Tool definitions are typed and limited. Model instructions optimize language and routing, but cannot override server-side policy.

**Authorization gateway:** a backend service validates current principal and account membership and returns only the permitted record IDs and field scopes. Re-check on every sensitive read/write, especially after account switching.

**Operational source:** a versioned authoritative account/ticket service responds to exact current status. If Snowflake is not authoritative, a warehouse copy must not be presented as live state.

**Knowledge:** approved policies are extracted, indexed, permission-filtered and cited. Internal-only docs must not be retrieved by customer-facing subagents.

**Data 360 (selective):** optional mapped DLOs/DMOs, identity resolution, support-history insights or allowed context from Snowflake via supported federation/ingestion. It should not be a required dependency for simple operational reads unless measured benefits justify it.

**Observability:** policy decision code, trace ID, selected route, retrieval source IDs, action receipt, per-stage duration, cost and escalation cause—without raw secrets or unnecessary customer content.

## Mermaid view

See [architecture map](../../diagrams/end-to-end-architecture.md) or [sequence diagram](../../diagrams/servicing-agent-sequence.md).

## Primary keys and record relationships

```
accounts:         (source_system, account_id) unique
customers:        (source_system, customer_id) unique
account_members:  (account_id, customer_id, role, valid_from, valid_to)
service_requests: (source_system, request_id) unique; account_id FK
policy_documents: (document_id, version) unique; effective_from, audience
```

The `account_members` relationship (or delegated entitlement service) determines access. Identity resolution can unify customer profiles for analytic context but **not** grant account membership.

## Data movement decision

- **Ticket status:** authoritative read, synchronously, per request with allowed field list and `as_of` timestamp.
- **Policy answer:** retrieve by purpose, user audience and effective version; answer with citation or abstain.
- **Cross-channel analysis:** historical Snowflake/Data 360 through a governed, potentially asynchronous path; labeled freshness.
- **Write:** phase two only, with confirmation, server-side authorization, idempotency and transaction receipt.

## Trust boundaries

| Boundary | Must verify | Safe default |
|---|---|---|
| Channel → Agent | Authenticated session and intended account | Clarify / no protected data |
| Agent → Action | Typed input and bound trusted principal | Reject invented parameters |
| Action → Data source | Row and field entitlement at read time | Deny without existence disclosure |
| Retriever → Model | Current approved evidence and ACL | Abstain if insufficient |
| Update → CRM | Confirmation and final permission | No mutation on uncertainty |
| Telemetry → Analytics | PII minimization and authorized access | Redacted scoped logs |

## Failure handling

If one dependency fails, don't fake success: ticket status becomes temporarily unavailable with escalation; policy answer requires evidence; account updates remain disabled on auth errors; human support remains available. A broader service can still operate in read-only mode if the update API is down and that mode is explicitly approved.

## What we would demo in a workshop

1. Authorized customer retrieves a known ticket (timestamp shown).
2. Customer requests a ticket from a different account (denial without leak).
3. Customer asks a policy question (versioned citation).
4. Policy is missing or conflicting (abstention and handoff).
5. Admin shows trace and source IDs without revealing PII.
