# Runnable synthetic learning labs

These are **stdlib-only Python** examples. No Salesforce org, Snowflake connection, token, package installation or live personal data is required.

```bash
python3 labs/scripts/validate_fixture.py
python3 labs/scripts/evaluate_retrieval.py
python3 -m unittest discover -s tests -v
python3 labs/scripts/check_content.py
```

## What they do

- `validate_fixture.py`: validates CSV keys, foreign keys, duplicate statuses and source identifiers; prints aggregate counts only.
- `evaluate_retrieval.py`: calculates precision@k and recall@k from labeled synthetic passage IDs (not a live search evaluation).
- `check_content.py`: checks relative Markdown link targets and scans for accidental nonexample email patterns.
- `tests/`: regression tests including intentionally invalid fixtures.
- `labs/sql/`: Snowflake-style/ANSI illustrative queries. These **do not constitute runnable Data 360 Calculated Insight definitions**; adapt schema and syntax for the target environment.

Data is fabricated and deliberately small. Do not claim its behavior proves a production Agentforce, Salesforce org or Snowflake deployment.
