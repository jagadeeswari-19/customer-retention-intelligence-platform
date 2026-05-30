CREATE DATABASE funnel_analysis_system;
USE funnel_analysis_system;
SELECT * FROM customer_data LIMIT 10;
SELECT
    COUNT(*) AS total_customers,
    AVG(MonthlyCharges) AS avg_monthly_charges,
    AVG(tenure) AS avg_tenure
FROM clean_events;

SELECT
    Contract,
    COUNT(*) AS customers
FROM clean_events
GROUP BY Contract;

SELECT
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 1 THEN 1 ELSE 0 END) AS churned_customers
FROM clean_events;

SELECT
    tenure,
    AVG(MonthlyCharges) AS avg_monthly_charges,
    AVG(TotalCharges) AS avg_total_charges
FROM clean_events
GROUP BY tenure
ORDER BY tenure;

SELECT
    a.customerID,
    a.MonthlyCharges,
    b.tenure
FROM clean_events a
INNER JOIN clean_events b
ON a.customerID = b.customerID;

