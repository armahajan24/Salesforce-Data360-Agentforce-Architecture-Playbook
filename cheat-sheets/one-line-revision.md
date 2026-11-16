# One-line architecture revision sheet

| Concept | One-line mental model | Watch for |
|---|---|---|
| Data stream | Define a source and how data arrives | Freshness and schema drift |
| DLO | Store the ingested or federated source-shape data | Retain source keys |
| DMO | Standardize and relate source data into a shared model | Do not confuse with a CRM record |
| Fully qualified source key | Pair the source namespace with source record identity | Cross-system collisions |
| Identity resolution | Match and reconcile linked identities | Not authorization and not deletion |
| Unified DMO | Unified view from rulesets | Match quality and explainability |
| Data transform | Prepare reusable clean/derived data | Batch vs streaming support |
| Calculated insight | Reusable aggregated metric | Dimensions, grain, frequency |
| Segment/activation | Define an audience, send to a target | Consent and destination permissions |
| Zero Copy | Access external data through federation | Not zero latency/cost; feature limits |
| Live API | Read current authoritative account/ticket status | Timeout, entitlement and availability |
| CDC | Event for data changes | Replay and deduplication |
| Platform Event | Business event | Consumer retries and DLQ |
| Pub/Sub API | Subscribe/publish events through event bus | 72-hour retention for relevant events |
| RAG | Retrieve evidence before answer generation | Stale index and missing citations |
| Chunking | Partition documents into retrievable units | Context loss and overlong chunks |
| Hybrid search | Mix keyword and semantic retrieval | Tune for identifiers and semantics |
| Precision@k | Portion of returned chunks that are relevant | Noise |
| Recall@k | Portion of relevant chunks returned | Missing critical evidence |
| Groundedness | Claim support by retrieved evidence | Hallucination |
| Agent Script | Mix deterministic control with LLM instructions | Model/metadata version changes |
| Subagent | Specialized agent scope | Routing and action ownership |
| Tool contract | Validated inputs, outputs, authorization and errors | Invented args, false success |
| Data space | Logical Data 360 data separation | Object and policy entitlements too |
| P50 / P95 latency | Median vs tail response time | Tail regressions |
| Solution discovery | Convert vague outcomes to measurable workflows | Premature architecture commitment |
| Automated resolution | Eligible requests resolved correctly without human action | Unsafe containment |
| ADR | Document choice, alternatives and rationale | Forgotten trade-offs |
