import pandas as pd
import os


def calculate_retention(df):

    retention = df.groupby(
        "tenure"
    ).size().reset_index(name="Customers")

    os.makedirs(
        "data/processed",
        exist_ok=True
    )

    retention.to_csv(
        "data/processed/retention_metrics.csv",
        index=False
    )

    print("Retention Metrics Saved")

    return retention