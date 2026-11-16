# Identity resolution: match and reconciliation

```mermaid
flowchart TD
 A[CRM Contact: C-001] --> N[Normalize identifiers]
 B[Web Profile: W-081] --> N
 C[Support Portal: P-055] --> N
 N --> M{Match rules / confidence}
 M -->|Match| U[Unified Individual U-100]
 M -->|No match| R[Separate source identity]
 U --> L[Link records to source identities]
 U --> S[Reconciliation selects attributes]
 S --> G[Authorized unified view]
```

Unified identity does **not** delete or merge the original source records. A matched identity is not itself an authorization entitlement; access must be checked separately.
