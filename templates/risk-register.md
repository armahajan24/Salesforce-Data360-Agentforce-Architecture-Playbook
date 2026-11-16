# Risk register (template)

| ID | Risk | Likelihood | Impact | Early indicator | Owner role | Mitigation | Decision date |
|---|---|---|---|---|---|---|---|
| R1 | Stale account status | Medium | High | Discrepant timestamps | Data lead | Use live authoritative status API | TBD |
| R2 | Unauthorized data disclosure | Low | Critical | Cross-account test fails | Security lead | Entitlement service and field-level controls | TBD |
| R3 | Incorrect policy answer | Medium | High | Low groundedness / superseded version | Knowledge owner | Effective-date index and escalation | TBD |
| R4 | Action claims success without writing | Medium | High | No operation receipt | Engineering | Receipt-based success; idempotency | TBD |
| R5 | Slow P95 | Medium | Medium | Token/retrieval/action trace spikes | SRE lead | SLO budgets, bounds and fallback | TBD |
