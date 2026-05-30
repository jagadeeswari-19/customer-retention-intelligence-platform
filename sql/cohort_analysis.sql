SELECT
    tenure,
    AVG(MonthlyCharges) AS avg_monthly_charges,
    AVG(TotalCharges) AS avg_total_charges
FROM clean_events
GROUP BY tenure
ORDER BY tenure;