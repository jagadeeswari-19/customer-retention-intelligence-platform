SELECT
    COUNT(*) AS total_customers,
    AVG(MonthlyCharges) AS avg_monthly_charges,
    AVG(tenure) AS avg_tenure
FROM clean_events;