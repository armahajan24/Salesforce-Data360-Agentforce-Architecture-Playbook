# 04 — Identity resolution and reconciliation

**Goal:** create a usable cross-source view of the same individual while preserving original records and avoiding false matches. Identity resolution is **probabilistic and rule-driven data engineering**, not automatic authorization.

## Understand the two responsibilities

1. **Match rules:** determine whether two records refer to the same real-world subject using trusted identifiers and normalized/fuzzy comparisons.
2. **Reconciliation rules:** choose which source's field to expose in the unified view—most recent, most complete or most trusted—without deleting source values.

Aster Service Group (fictional): CRM Contact `crm:C-1001` and Portal User `portal:P-8001` share verified contact points. A third record `external:E-9003` shares only a common name. A safe design should match the first two based on higher-confidence identifiers, but **not** auto-match the third just because both people are named Jordan.

## Design rules before turning them on

- **Strong signal:** a trustworthy common enterprise identity or validated identifier tied to the same individual.
- **Weak signal:** name, unverified email, phone potentially shared by a household, or approximate location.
- **Normalization:** consistent casing, whitespace, phone format, Unicode handling and null semantics.
- **Reconciliation:** set source priority *per field*: legal name vs notification address may have different owners.
- **Unmatch / split:** plan for false positives, stewardship and historical correction.
- **Transparent provenance:** keep source IDs, rule/ruleset version, merge evidence and matched-record lineage.

## Quality measures

- **False match rate (FMR):** incorrectly unified pairs / evaluated unified pairs.
- **Missed match rate:** same-person pairs left unlinked / evaluated same-person pairs.
- **Profile coverage:** eligible source profiles linked to at least one intended cross-source identity.
- **Steward review rate:** share of auto-matches requiring manual investigation.

Use labeled samples including same-name different people, changed phone numbers, recycled email addresses and shared household contacts. Avoid claiming an arbitrary rule threshold is universally correct.

## The critical separation: identity vs access

The system may correctly unify an individual with multiple account relationships, but the signed-in person might be permitted to view only **one** of them. Entitlement must be enforced by an authoritative service and/or applicable data access policy for each requested account or field.

**Example:** A service rep asks for account `A-2002` that belongs to a unified profile. The rep's permission is scoped to `A-1001`. The match is valid; the read must still be denied for `A-2002`.

## Troubleshooting

1. Confirm source records and identifiers exist and are in the correct data space.
2. Inspect DLO→DMO mappings and relationship fields.
3. Compare rule version, match evidence and reconciliation priorities.
4. Check affected link/unified records and processing completion.
5. Sample impacted records before broad rule changes, then re-run evaluation.

**Source:** [Data 360 architecture and identity resolution](https://developer.salesforce.com/docs/data/data-cloud-dev/guide/dc-architecture.html).
