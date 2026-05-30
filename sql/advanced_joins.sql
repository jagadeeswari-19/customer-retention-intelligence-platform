SELECT
    a.customerID,
    a.MonthlyCharges,
    b.tenure
FROM clean_events a
INNER JOIN clean_events b
ON a.customerID = b.customerID;