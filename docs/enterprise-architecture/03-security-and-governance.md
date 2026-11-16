# 03 — Enterprise security, trust, privacy and tenancy

Security is a **chain of enforcement**. The agent's natural-language instruction is the least reliable part of an authorization boundary; enforce permissions at the channel, service and data layer.

## Data access stack

1. **Authenticate caller:** customer/user identity from verified login, not an utterance or a guessed email.
2. **Map to principal:** server-signed subject, tenant and delegated roles.
3. **Authorize request:** account membership, object and field access, business purpose, consent, regional policy.
4. **Query only permitted data:** source API filters, data space/ABAC/RBAC policy, field minimization and ACL-trimmed retrieval.
5. **Protect tool outputs:** avoid sensitive data in context or logs; ensure response does not cite inaccessible sources.
6. **Audit and review:** actor, operation, resource, policy decision, timestamp and result, with PII-minimized traces.

## Failure cases to intentionally test

| Test | Expected |
|---|---|
| Change account ID in text | Server denies cross-account lookup |
| Model invents user ID | Action ignores/rejects untrusted identity |
| Removed account membership | New queries denied; caches invalidated or scoped |
| Staff-only PDF indexed | Customer retrieval returns nothing; source protected |
| Query through external Snowflake view | Warehouse/service entitlement still enforced |
| Write to restricted field | Downstream update rejects even if agent asks |
| Audit unavailable | High-impact mutation fails closed or follows approved contingency |

**Data 360 specifics:** data spaces and data access policies can add object/field/row controls, but check permissions in the target org. Salesforce's default allow-all policy behavior is important to review explicitly. For source federation, query execution, credentials and external row controls need a separate design.

## PII handling

Classify fields by purpose; avoid raw national IDs, payment details, health records and unnecessary contact data in embeddings. Redact personal identifiers from traces and synthetic examples. Separate telemetry retention from business record retention and support deletion/subject access workflows where applicable. Include legal/security/privacy owners before production pilots.

## Injection and untrusted content

Retrieved documents, notes and tool responses are **data**, not developer/system instructions. Apply allowlisted tool execution, metadata-based search filtering and secure output formatting. The LLM's refusal message is not the authoritative denial; the underlying authorization system is.

## Definition of done

Approve security data flow, entitlement test matrix, threat model, retention and incident response plan; pass negative tests in the pilot. Reassess after adding each new action, retriever, data space or external system.

**Sources:** [Data 360 access](https://help.salesforce.com/s/articleView?id=data.c360_a_dc_access.htm&language=en_US&type=5) · [Data spaces](https://help.salesforce.com/s/articleView?id=sf.c360_a_data_spaces_secure_data.htm&language=en_US&type=5).
