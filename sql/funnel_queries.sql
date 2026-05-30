SELECT
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 1 THEN 1 ELSE 0 END) AS churned_customers
FROM clean_events;