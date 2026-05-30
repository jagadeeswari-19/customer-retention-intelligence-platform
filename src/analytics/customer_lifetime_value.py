import pandas as pd


def calculate_clv(df):

    """
    Customer Lifetime Value Calculation
    CLV = Average Monthly Charges × Average Tenure
    """

    avg_monthly_revenue = df['MonthlyCharges'].mean()

    avg_tenure = df['tenure'].mean()

    clv = avg_monthly_revenue * avg_tenure

    return round(clv, 2)


def customer_revenue_segments(df):

    """
    Segment customers by revenue
    """

    conditions = [
        (df['MonthlyCharges'] < 40),
        (df['MonthlyCharges'] >= 40) &
        (df['MonthlyCharges'] < 80),
        (df['MonthlyCharges'] >= 80)
    ]

    categories = [
        'Low Value',
        'Medium Value',
        'High Value'
    ]

    df['RevenueSegment'] = pd.cut(
        df['MonthlyCharges'],
        bins=[0, 40, 80, 200],
        labels=categories
    )

    return df


def revenue_summary(df):

    """
    Revenue summary statistics
    """

    summary = {
        'Total Revenue':
            round(df['TotalCharges'].sum(), 2),

        'Average Revenue':
            round(df['MonthlyCharges'].mean(), 2),

        'Maximum Revenue':
            round(df['MonthlyCharges'].max(), 2),

        'Minimum Revenue':
            round(df['MonthlyCharges'].min(), 2)
    }

    return summary