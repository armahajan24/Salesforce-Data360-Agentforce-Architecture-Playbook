# 01 — Agentforce architecture: scope, subagents and routing

An agent should have a narrow, auditable job description and a finite set of tools. The model can interpret intent and formulate helpful language, but **identity checks, permissions, deterministic business rules and transaction execution belong in enforced components**.

## Agent responsibilities

For fictional Aster Service Group:

- **Account Info subagent:** explain non-sensitive account overview after server-side authorization.
- **Ticket Status subagent:** retrieve exact current status through a scoped read API; include as-of timestamp.
- **Policy Guidance subagent:** retrieve approved policy versions and cite sources; abstain when evidence is missing.
- **Human Handoff subagent:** preserve safe context and escalate missing evidence, unverified caller, sensitive issues, or repeated failures.
- **Profile Change subagent (phase two):** collect an allowed value, confirm it, call a strongly typed update action, and verify its receipt.

## Router trade-offs

| Choice | When it helps | Failure mode |
|---|---|---|
| Single specialized agent | Narrow first deployment, limited intents | Broad instructions and overlapping tools |
| Multiple subagents | Distinct access scopes and workflows | Incorrect transitions; duplicated tools/variables |
| Deterministic state machine | Hard-gated action flows and confirmations | Fragility if state is not persisted correctly |
| LLM classification | Natural-language intent flexibility | Misroute when intents overlap or prompts are overloaded |

Choose a **single parent agent with scoped subagents** for the case study, but keep confirmation/authorization paths deterministic. Avoid expanding into specialized multi-agent systems until routing metrics and workflow ownership justify the complexity.

## Agent Script concepts (not deployment code)

Salesforce's current Agent Script reference uses the **`subagent`** term (formerly `topic`) and separates programmatic logic (`->`) from prompt-oriented instruction (`|`). Routing starts with `start_agent`. The following is **conceptual pseudocode**, not a validated `.agent` file:

```text
ROUTER (conceptual):
  if !session.verified:
      route AUTHENTICATION_OR_HUMAN
  else if intent == "ticket_status":
      route TICKET_STATUS
  else if intent == "policy_question":
      route POLICY_GUIDANCE
  else if intent == "profile_update":
      route PROFILE_CHANGE_WITH_CONFIRMATION
  else:
      clarify_or_escalate()
```

For actual syntax and supported expressions, use the official [Agent Script reference](https://developer.salesforce.com/docs/ai/agentforce/guide/ascript-reference.html), then validate in a licensed development org.

## Conversation state

Separate **verified session values** (server-issued subject, authorized accounts, locale) from **untrusted natural-language slots** (user-provided names, guessed account IDs). Do not let the model rewrite the verified subject. Explicitly reset mutable variables on handoff and escalation; avoid a prior-account value leaking into the next customer journey.

## What success looks like

Route accuracy on a labeled intent dataset; unauthorized attempts denied; no unsupported tool calls; no false success; safe escalation; reasonable P95. See [agent evaluation](06-testing-and-evaluation.md) and [case study acceptance gates](../../case-studies/enterprise-servicing-agent/05-tests-and-acceptance.md).

**Sources:** [Agent Script](https://developer.salesforce.com/docs/ai/agentforce/guide/agent-script.html) · [Flow of control](https://developer.salesforce.com/docs/ai/agentforce/guide/ascript-flow.html).
