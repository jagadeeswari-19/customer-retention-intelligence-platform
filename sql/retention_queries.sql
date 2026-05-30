SELECT
    ROUND(
        SUM(CASE WHEN Churn = 0 THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*),
        2
    ) AS retention_rate
FROM clean_events;