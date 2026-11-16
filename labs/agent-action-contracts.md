# Conceptual action contracts and pseudocode

## Read action

```text
GetRequestStatus(verified_context, account_id, request_id):
  assert verified_context.valid and !verified_context.expired
  account_scope = entitlements.allowed_accounts(verified_context.subject)
  if account_id not in account_scope: return DENIED without resource details
  result = ticket_service.get(account_id, request_id, fields=ALLOWED_FIELDS)
  if result.not_found: return NOT_FOUND_OR_DENIED
  if result.timeout: return UNAVAILABLE
  return {status: SUCCESS, ticket_status: result.status,
          as_of_utc: result.committed_at, source: "ticket-service"}
```

## Write action

```text
ChangePreference(verified_context, validated_account_id, field, value,
                 confirmed, expected_version, idem_key):
  if not confirmed: return CONFIRMATION_REQUIRED
  if field not in ["preferred_contact_channel"]: return INVALID_FIELD
  if value not in ALLOWED_VALUES: return INVALID_VALUE
  entitlements.recheck_write(verified_context.subject, validated_account_id, field)
  consent_service.check(verified_context.subject, value)
  receipt = account_service.update_atomically(
      account=validated_account_id, expected_version=expected_version,
      field=field, value=value, idempotency_key=idem_key)
  if receipt.confirmed: return {status: SUCCESS, operation_id: receipt.id}
  return {status: receipt.error_category}
```

These examples use invented service APIs and pseudo-logic **only**. They are deliberately not Salesforce Apex code, Python implementations or unapproved production auth instructions.

## JSON-schema-like tool envelope (conceptual)

```json
{
  "name": "ChangePreference",
  "input_fields": ["account_id", "field", "value", "confirmed", "expected_version", "idempotency_key"],
  "server_bound_fields": ["verified_subject", "tenant_id"],
  "result_statuses": ["SUCCESS", "DENIED", "INVALID_FIELD", "CONFLICT", "UNAVAILABLE"]
}
```

Never let the LLM set `server_bound_fields`. Review security, API ownership, rollback and observability before making an actual Salesforce tool.
