-- EDUCATIONAL EXAMPLE: find orphaned service requests.
-- Join on the appropriate source-qualified relationship in real systems.
SELECT r.request_id, r.account_id
FROM service_requests AS r
LEFT JOIN accounts AS a ON r.account_id = a.account_id
WHERE a.account_id IS NULL;
