# Data 360 + servicing agent: conceptual map

```mermaid
flowchart LR
 subgraph Sources[Source systems]
   SF[Salesforce CRM]
   SN[Snowflake account and activity]
   KB[Approved policy documents]
 end
 subgraph Data[Data 360 - optional unified/analytical context]
   DL[DLO or federated external DLO]
   DM[DMO mapping]
   IR[Identity resolution]
   CI[Insights / activation]
   DL --> DM --> IR --> CI
 end
 SF --> DL
 SN -. "Selected ingestion or federation" .-> DL
 KB --> IX[Approved search index / retriever]
 subgraph Service[Authorized servicing experience]
   USER[Authenticated caller] --> AF[Agentforce router]
   AF --> SG[Policy + entitlement checks]
   SG --> READ[Authoritative read API]
   SG --> ACT[Controlled action]
   SG --> RET[Grounded answer]
 end
 SN --> API[Read service]
 API --> READ
 RET --> IX
 CI -. "Context where useful" .-> SG
 ACT --> SYS[System of record]
 AF --> HUMAN[Human escalation]
```

**Interpretation:** dotted lines represent optional choices; these are not automatic native connectors or guarantees of zero-copy availability. Data authorization and consent are enforced before exposing data to the agent.
