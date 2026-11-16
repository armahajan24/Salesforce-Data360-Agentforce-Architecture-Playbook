# 08 — State management, subagent transitions and bounded multi-step tasks

Agentforce agents may route across specialized subagents. State creates efficiency but also risk when variables survive longer than intended or transition parameters are ambiguous.

## Separate state by trust level

| Class | Example | Who may set it |
|---|---|---|
| Trusted session | Verified subject ID, assigned account scope | Authenticated platform/backend |
| Business state | Selected approved ticket, operation receipt | Validated service/tool response |
| Conversational slot | "third request", "SMS" | Model/user may suggest; validate |
| Derived context | Retrieved policy version, safe summary | Retriever/tool with provenance |
| Ephemeral routing | Last subagent choice, clarification needed | Agent orchestration |

A model-generated string such as `"A-1001"` must never be treated as stronger evidence than a scoped account list issued by the backend. Reset or revalidate selected account, intent and action parameters across handoff, re-authentication and new requests.

## Example: "create a child ticket for the shipping issue"

1. Identify the parent from a **server-authorized** list, not a guessed case number.
2. Ask clarification if several eligible cases exist.
3. Validate the relation, new category and mandatory fields before action execution.
4. Call typed service/Flow/Apex tool with declared inputs only.
5. Verify the new ticket ID and parent relationship from the resulting receipt.
6. Respond with the real operation result; do not infer success from the tool being selected.

## Multi-agent vs subagents

Use one bounded agent with subagents when a common business identity, shared UX and a small action catalog suffice. Introduce separate autonomous agents only when responsibility, protocol, permissions and operational ownership justify them. More agents do not intrinsically increase correctness.

## Tests

- Cross-account context should not survive a user switch.
- A stale `current_record_id` cannot authorize a new operation.
- A transition with no declared parameters cannot accept fabricated arguments.
- Ambiguous numerical references must resolve against an authorized selection list.
- A failed action cannot yield an affirmative completion message.

**Source:** [Agent Script flow of control](https://developer.salesforce.com/docs/ai/agentforce/guide/ascript-flow.html).
