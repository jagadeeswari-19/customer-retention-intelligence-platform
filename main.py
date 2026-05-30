import pandas as pd

from src.etl.pipeline import run_pipeline

from src.analytics.kpi_monitor import (
    generate_kpis
)

from src.analytics.churn_model import (
    train_churn_model
)

from src.analytics.segmentation import (
    customer_segmentation
)

from src.analytics.retention import (
    calculate_retention
)

from src.analytics.cohort import (
    cohort_analysis
)

from src.analytics.ab_testing import (
    run_ab_test
)

from src.analytics.executive_summary import (
    generate_executive_summary
)

print("Starting Funnel Analysis System...")

# -----------------------------------------
# RUN ETL PIPELINE
# -----------------------------------------

run_pipeline()

# -----------------------------------------
# LOAD CLEAN DATA
# -----------------------------------------

df = pd.read_csv(
    "data/processed/clean_events.csv"
)

# -----------------------------------------
# KPI MONITORING
# -----------------------------------------

generate_kpis()

# -----------------------------------------
# CUSTOMER SEGMENTATION
# -----------------------------------------

customer_segmentation(df)

# -----------------------------------------
# RETENTION ANALYSIS
# -----------------------------------------

calculate_retention(df)

# -----------------------------------------
# COHORT ANALYSIS
# -----------------------------------------

cohort_analysis(df)

# -----------------------------------------
# CHURN MODEL
# -----------------------------------------

train_churn_model()

# -----------------------------------------
# A/B TESTING
# -----------------------------------------

group_a = df[
    df["MonthlyCharges"] > 50
]["MonthlyCharges"]

group_b = df[
    df["MonthlyCharges"] <= 50
]["MonthlyCharges"]

run_ab_test(
    group_a,
    group_b
)

# -----------------------------------------
# EXECUTIVE SUMMARY
# -----------------------------------------

generate_executive_summary(df)

print("System execution completed.")