# -----------------------------------------
# APPLICATION CONSTANTS
# -----------------------------------------

APP_NAME = "Funnel Analysis System"

APP_VERSION = "1.0.0"

AUTHOR = "Jagadeeswari S"

# -----------------------------------------
# FILE PATHS
# -----------------------------------------

RAW_DATA_PATH = "data/raw/user_events.csv"

PROCESSED_DATA_PATH = "data/processed/clean_events.csv"

MODEL_PATH = "models/churn_model.pkl"

# -----------------------------------------
# MACHINE LEARNING
# -----------------------------------------

RANDOM_STATE = 42

TEST_SIZE = 0.2

N_CLUSTERS = 4

# -----------------------------------------
# DASHBOARD SETTINGS
# -----------------------------------------

PAGE_TITLE = "Funnel Analysis Dashboard"

LAYOUT = "wide"

# -----------------------------------------
# KPI THRESHOLDS
# -----------------------------------------

HIGH_CHURN_THRESHOLD = 25

LOW_RETENTION_THRESHOLD = 70

# -----------------------------------------
# SEGMENT LABELS
# -----------------------------------------

SEGMENTS = [
    "Low Value",
    "Medium Value",
    "High Value"
]

# -----------------------------------------
# COLORS
# -----------------------------------------

PRIMARY_COLOR = "#1f77b4"

SECONDARY_COLOR = "#ff7f0e"

SUCCESS_COLOR = "#2ca02c"

DANGER_COLOR = "#d62728"