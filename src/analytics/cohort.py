import pandas as pd
import os
def cohort_analysis(df):

    cohort = df.groupby("tenure").agg({
        "MonthlyCharges": "mean",
        "TotalCharges": "mean"
    })

    os.makedirs(
        "data/processed",
        exist_ok=True
    )

    cohort.to_csv(
        "data/processed/cohort_analysis.csv"
    )

    print("Cohort Analysis Saved")

    return cohort