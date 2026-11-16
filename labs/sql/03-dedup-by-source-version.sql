-- EDUCATIONAL EXAMPLE: deduplicate an append-only change feed by durable key.
-- Requires a source_version field with trustworthy monotonic semantics.
WITH ranked AS (
    SELECT source_system, request_id, status, source_version,
           ROW_NUMBER() OVER (
              PARTITION BY source_system, request_id
              ORDER BY source_version DESC
           ) AS rn
    FROM request_events
)
SELECT source_system, request_id, status, source_version
FROM ranked
WHERE rn = 1;
