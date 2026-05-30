import pandas as pd


def dashboard_summary(df):

    summary = {
        "Total Customers": len(df),
        "Average Monthly Charges": df["MonthlyCharges"].mean(),
        "Average Tenure": df["tenure"].mean()
    }

    return summary