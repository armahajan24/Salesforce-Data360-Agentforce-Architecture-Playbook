# 06 — MCP, agent-to-agent orchestration and interoperability (conceptual)

**Do not use a fashionable integration protocol without a bounded business reason.** For a simple status lookup, an approved action to an authoritative service may be sufficient. MCP and agent-to-agent (A2A) are integration choices with distinct identity, tool-discovery and governance consequences.

## Mental model

- **Action/Tool contract:** one controlled capability (e.g., get ticket status) with named parameters and return values.
- **MCP — Model Context Protocol:** an interoperability protocol for exposing tools/resources to clients and agents. It does not itself replace business-level authorization, safe tool contracts or data governance.
- **A2A — Agent-to-Agent:** an agent collaboration protocol/pattern for delegating tasks across different agents/services. Multiple agents need explicit trust and task-completion boundaries.
- **Traditional REST/Flow/Apex integration:** often simplest for internal transactional operations with well-known schemas.

## Selection table

| Need | Option to investigate | Controls |
|---|---|---|
| Agent calls a first-party CRM workflow | Flow/Apex action | Permissions, typed input, receipts |
| Agent accesses an approved tool catalog across systems | MCP-based tool integration (if supported) | AuthN/Z, tool allowlist, context minimization |
| Two autonomous services coordinate a bounded task | A2A / task orchestration | Delegation auth, trace chain, error/timeout, escalation |
| Need guaranteed multi-step business transaction | Domain workflow/saga | Durable state, idempotency, compensation |

## Cross-agent failure modes

- One agent delegates more privileges than the caller has.
- The downstream agent claims completion without a system-of-record receipt.
- Sensitive conversation state or raw credentials are forwarded to another model.
- Recursive delegation inflates token cost and P95 latency.
- A receiving agent treats external content as authoritative instructions.

## Review checklist

Document capability owner, supported protocol/version, principal propagation and audience, allowed tools, data residency, audit trail, retry/idempotency, cancellation semantics and failure-to-human path. Validate available product support and deployment requirements against current documentation before giving specific Salesforce MCP/A2A implementation steps.

**Why this is conceptual:** platform support and authentication mechanisms evolve quickly. This playbook intentionally avoids claiming a specific universal Salesforce MCP/A2A setup sequence without org/release confirmation.
