# 04 — Agentforce actions: Flow, Apex, API and deterministic execution

Actions turn an answer engine into a transactional system. Design each action as a **typed, auditable contract** with documented ownership, permissions, input validation, idempotency, explicit errors and trustworthy completion receipts.

## Tool contract: `GetTicketStatus` (read-only)

```json
{
  "name": "GetTicketStatus",
  "inputs": {
    "verifiedSubjectId": "SERVER_ISSUED_CONTEXT_ONLY",
    "accountId": "A-1001",
    "requestId": "R-5001"
  },
  "output": {
    "authorized": true,
    "status": "IN_PROGRESS",
    "asOfUtc": "2026-01-15T10:30:00Z",
    "source": "authoritative-ticket-service"
  }
}
```

This schema is conceptual. **Do not let the LLM supply `verifiedSubjectId`**; the adapter binds it from authenticated context. Require entitlement checks on `accountId` and `requestId` in the downstream service.

## Read vs write

| Concern | Read action | Write action |
|---|---|---|
| Authentication | Required | Required |
| Authorization | Per record/field | Recheck at commit |
| Confirmation | Usually not needed for non-sensitive read | Required for meaningful changes |
| Idempotency | Helpful for retries | Required for safe retry behavior |
| Success | Valid response with source/as-of | Persisted receipt, not tool invocation |
| Auditing | Access event | Before/after or appropriate event, actor, reason |
| Failure handling | Honest unavailable state | No false success; reconcile uncertain outcomes |

## When Flow, Apex or external service?

- **Flow:** explicit declarative workflow, supported record/API actions and validation; good when admins can own the workflow.
- **Apex:** complex validations, reusable code, typed interfaces, platform transaction patterns, tests; watch limits and error exposure.
- **External service/MuleSoft/API:** authoritative system outside Salesforce, cross-system orchestration or established domain API; never put source-system secrets in a prompt.

## Failure mode: model invents tool inputs

The user asks "Create a follow-up for request three." If an action declares no input named `request_type`, the orchestrator must **not** fabricate that parameter or claim a ticket was created. Bind IDs and enums from validated records in a selection step; reject ambiguous references and produce structured errors.

### Action implementation checklist

- [ ] Stable action API name, version and owner.
- [ ] Typed enums/IDs, required/optional fields and length limits.
- [ ] Authenticated context, per-object/field entitlements, no model-supplied identity.
- [ ] Deterministic validation and confirmation for mutations.
- [ ] Timeout, retry/backoff policy, idempotency key and correlation ID.
- [ ] Result classification: `SUCCESS`, `DENIED`, `NOT_FOUND`, `CONFLICT`, `RETRYABLE_ERROR`.
- [ ] Audit and PII-minimized telemetry.
- [ ] Tests for duplicates, retries, wrong account, null fields and partial failure.

**Source:** [Agent Script actions](https://developer.salesforce.com/docs/ai/agentforce/guide/ascript-ref-actions.html).
