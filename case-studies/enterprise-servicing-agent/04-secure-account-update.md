# Case 04 — Secure account preference update (future phase)

## User request

"Change the preferred contact channel for my subscription account to SMS."

This is not an invitation to produce free-form SQL. The agent must collect/validate the desired value; any field not on an explicit allowlist is rejected.

## Control flow

1. **Authentication:** portal supplies verified principal; reject when session expired.
2. **Account selection:** backend gives permitted account choices; user selects one without model guessing.
3. **Field authorization:** policy service verifies that this principal can edit `preferred_contact_channel` on that account.
4. **Value validation:** only `EMAIL`, `SMS`, or `PHONE` and subject to consent/locale/business restrictions.
5. **Explicit confirmation:** show account identifier suffix, field, old value if permitted, new value and potential consequences.
6. **Fresh authorization at commit:** server rechecks membership/consent and optimistic record version.
7. **Controlled mutation:** typed Flow/Apex/domain API call with idempotency key and audit reason; never generated SOQL/SQL from utterance.
8. **Receipt:** action returns operation ID, saved value and timestamp. Only then state the change succeeded.
9. **Timeout ambiguity:** check operation receipt or query authoritative state by idempotency key; do not retry blindly.

See [secure update sequence](../../diagrams/secure-update-sequence.md).

## Example action contract (illustrative)

```json
{
  "request": {
    "account_id": "A-1001",
    "field": "preferred_contact_channel",
    "new_value": "SMS",
    "expected_version": 3,
    "confirmed": true,
    "idempotency_key": "req-ASG-0001"
  },
  "trusted_context": {
    "verified_subject_id": "bound-server-side-not-llm"
  },
  "response": {
    "status": "SUCCESS",
    "operation_id": "op-ASG-42",
    "effective_value": "SMS",
    "committed_at": "2026-01-15T10:30:00Z"
  }
}
```

The *trusted_context* section is a conceptual server-only field and **must never be model-supplied**. The idempotency key must be scoped to caller/operation and retained long enough for the retry policy. Ensure permission check and commit are coordinated; an unrelated update can cause a version conflict.

## Policy and privacy

SMS preference alone does not establish legal messaging consent. The update adapter must validate applicable opt-in and local policy before accepting the change. Some values may require separate verified consent or human processing.

## Negative test suite

| Case | Expected |
|---|---|
| Caller tries to edit another account | Denied, no update |
| Field `billing_limit` requested | Rejected (not allowlisted) |
| Missing confirmation | No update |
| Session expires after confirmation | Reauthorize or cancel |
| Duplicate key replay | Same result, no second mutation |
| Version conflict | Ask to re-review fresh value |
| API timeout after commit | Reconcile receipt; don't claim unverified success |
| Backend returns error but LLM wants to say "done" | Do not claim success |

**Release condition:** this capability remains a *design* until domain, legal, security, and product owners approve it and the acceptance suite passes in a permitted environment.
