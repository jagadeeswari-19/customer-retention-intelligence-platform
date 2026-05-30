SELECT
    Contract,
    COUNT(*) AS customers
FROM clean_events
GROUP BY Contract;