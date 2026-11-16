# 10 — Data graphs, analytical context and agent grounding

The usefulness of a customer 360 view depends on how quickly relevant entities and relationships can be retrieved without creating a sprawling, noisy prompt. Data graphs and related context features can help organize supported interconnected data, but design choices are feature-, licensing- and release-dependent.

## Context design principles

- Choose a business **anchor** (authenticated customer or account) and define permissible related entities.
- Document **relationship cardinality** and avoid multiplying rows or duplicating the same engagement.
- Prioritize the **smallest relevant context**: current permitted account, a few recent service requests and summarized history—not an indiscriminate export.
- Attribute sources, timestamps, data spaces and permissions to each field.
- Decide whether to retrieve context dynamically, precompute insights, or cache a short-lived view with strict scope.

## Fictional example

Aster Service Group wants an agent to know whether an authorized account has many recent support requests. A precomputed aggregate may return `request_count_30d=4` and `as_of=2026-01-15`. The agent may use that to offer additional help, but it **must not** use the aggregate to claim the exact current status of any specific request.

## Validation

1. Check authorized scope before constructing/retrieving the graph context.
2. Validate joins with synthetic records having one-to-many membership and multiple requests.
3. Check staleness and partial-source behavior.
4. Compare response and token cost with a direct API path.
5. Measure whether extra context improves resolution quality and not only fluent verbosity.

**Sources:** [Data 360 architecture](https://developer.salesforce.com/docs/data/data-cloud-dev/guide/dc-architecture.html) · [Data 360 limits and guidelines](https://help.salesforce.com/s/articleView?id=c360_a_limits_and_guidelines.htm&language=en_US&type=5).
