# 08 — Data spaces, governance, access policies and data protection

Data governance is layered: **identity → product permissions → data-space scope → object/field/record policies → downstream entitlement → prompt/output minimization and audit**. A data space is a logical segregation mechanism, **not a universal guarantee of access** to every underlying or external source.

## Controls to understand

- **Data spaces:** logically separate relevant Data 360 datasets by purpose, geography or business unit and associate access through permission sets.
- **Permission sets:** grant feature/data-space access appropriate for job responsibilities; avoid broad default access.
- **Data access policies:** where available, apply RBAC/ABAC controls at object, field and row levels with classification/tags.
- **Tagging/classification/masking:** protect sensitive fields and define allowed consumption patterns.
- **Source entitlements:** keep authoritative record visibility, delegated access, consent and tenancy enforced when reading from APIs or external warehouses.
- **LLM boundaries:** pass only necessary fields/grounding; mask secrets, log minimally and filter output for unauthorized disclosure.

Salesforce documentation describes an out-of-box **Allow All** policy that can grant broad access within assigned data spaces. A secure deployment must **review and scope** the default policy, rather than assuming a custom data space automatically delivers fine-grained restrictions.

### Threat-model table

| Threat | Example | Control / test |
|---|---|---|
| Cross-account leakage | Authenticated A-1001 user asks for A-2002 | Recheck account entitlement server-side; negative test |
| Prompt injection | Policy PDF says "ignore access rules" | Treat retrieved text as untrusted data, not control instructions |
| Overshared fields | LLM sees full SSN for a ticket summary | Minimize/mask upstream, redact logs |
| Stale consent | Segment sends email after opt-out | Recheck consent at activation; track suppression |
| Overbroad rep role | Support rep queries an unrelated data space | Access policy and break-glass audit |
| Debug data leakage | Tracing contains account identifiers | Restrict session tracing DMO access and retention |

## Policy governance workflow

Document every field's classification, permitted roles, purpose, region and retention. Map business requirements into enforceable product/service policies and test with real roles in a sandbox. Review a trace or query export for PII minimization before enabling observability widely.

## Practical governance principle

"We enforce data access where the data is served, not only in prompt instructions. I first define who is allowed to see which account and fields, then configure Data 360 data spaces and relevant data access policies and test negative access cases. If the source is Snowflake or a live API, its own authorization path still needs to be verified."

**Sources:** [Secure with Data Spaces](https://help.salesforce.com/s/articleView?id=sf.c360_a_data_spaces_secure_data.htm&language=en_US&type=5) · [Assign Data Access](https://help.salesforce.com/s/articleView?id=data.c360_a_dc_access.htm&language=en_US&type=5) · [Tracing governance](https://help.salesforce.com/s/articleView?id=ai.generative_ai_session_trace_data_governance.htm&language=en_US&type=5).
