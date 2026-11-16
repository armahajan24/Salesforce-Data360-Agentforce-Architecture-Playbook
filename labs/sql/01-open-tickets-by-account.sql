-- EDUCATIONAL EXAMPLE: Snowflake-like SQL using fictional table names.
-- Not a Data 360 Calculated Insight deployment definition.
SELECT
    account_id,
    COUNT(DISTINCT request_id) AS open_request_count,
    MAX(updated_at_utc) AS latest_request_change
FROM service_requests
WHERE status IN ('OPEN', 'IN_PROGRESS')
GROUP BY account_id
ORDER BY open_request_count DESC, account_id;
