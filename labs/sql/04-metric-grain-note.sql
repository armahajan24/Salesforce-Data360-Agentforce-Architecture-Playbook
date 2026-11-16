-- PITFALL: joining requests to many request events before COUNT(*) duplicates requests.
-- Fix: aggregate to the intended grain before joining.
WITH requests_per_account AS (
   SELECT account_id, COUNT(DISTINCT request_id) AS request_count
   FROM service_requests
   GROUP BY account_id
)
SELECT a.account_id, COALESCE(r.request_count, 0) AS request_count
FROM accounts a
LEFT JOIN requests_per_account r ON r.account_id = a.account_id;
