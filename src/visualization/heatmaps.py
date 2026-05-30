import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def correlation_heatmap(df):

    plt.figure(figsize=(18, 10))

    correlation = df.corr(numeric_only=True)

    sns.heatmap(
        correlation,
        annot=True,
        cmap="coolwarm",
        linewidths=0.5
    )

    plt.title("Correlation Heatmap")

    plt.tight_layout()

    plt.show()


def churn_heatmap(df):

    churn_data = pd.crosstab(
        df['Contract'],
        df['Churn']
    )

    plt.figure(figsize=(8, 5))

    sns.heatmap(
        churn_data,
        annot=True,
        fmt='d',
        cmap='Blues'
    )

    plt.title("Contract vs Churn Heatmap")

    plt.tight_layout()

    plt.show()


def retention_heatmap(df):

    retention = df.groupby('tenure').agg({
        'MonthlyCharges': 'mean',
        'TotalCharges': 'mean'
    })

    plt.figure(figsize=(8, 5))

    sns.heatmap(
        retention.corr(),
        annot=True,
        cmap='viridis'
    )

    plt.title("Retention Heatmap")

    plt.tight_layout()

    plt.show()