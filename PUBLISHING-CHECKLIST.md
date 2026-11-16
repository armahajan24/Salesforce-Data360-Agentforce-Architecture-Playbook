# Publication checklist

## Before pushing to GitHub

- [ ] Confirm no real customer/employer names, internal IDs, ticket numbers, prompts, transcripts, logs, usernames, endpoints or secrets remain.
- [ ] Run `python3 labs/scripts/validate_fixture.py` and `python3 -m unittest discover -s tests -v`.
- [ ] Run `python3 labs/scripts/check_content.py` to check internal Markdown links, accidental nonexample email addresses and broken relative paths.
- [ ] Review `REFERENCES.md` against current Salesforce release notes; all evolving features are marked as edition/release-specific.
- [ ] Review all Mermaid diagrams on GitHub or a previewer; ensure they do not imply unsupported live product behavior.
- [ ] Confirm SQL and pseudocode are labelled illustrative (not deployable Salesforce configuration).
- [ ] Review MIT license, copyright treatment and contributor policy.
- [ ] Create a **new** GitHub repository, push this package, verify default branch and rendered README, then enable basic branch protection.
- [ ] Paste actual repository URL into social draft and read post in LinkedIn preview.
- [ ] Approve each post before publishing/scheduling with Buffer.

## Release notes

Release v0.1: initial educational content, synthetic case study, decision records, fixture validator, and tests. No actual Agentforce org deployment was performed.
