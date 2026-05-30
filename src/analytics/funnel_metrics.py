import pandas as pd


def funnel_analysis(df):

    total_users = len(df)

    active_customers = df[df["Churn"] == 0].shape[0]

    churned_customers = df[df["Churn"] == 1].shape[0]

    retention_rate = (active_customers / total_users) * 100

    churn_rate = (churned_customers / total_users) * 100

    metrics = {
        "Total Users": total_users,
        "Active Customers": active_customers,
        "Churned Customers": churned_customers,
        "Retention Rate": retention_rate,
        "Churn Rate": churn_rate
    }

    return metrics