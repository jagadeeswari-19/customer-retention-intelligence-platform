import os
import sys

# -----------------------------------------
# ADD ROOT DIRECTORY TO PYTHON PATH
# -----------------------------------------

ROOT_DIR = os.path.abspath(
    os.path.dirname(__file__)
)

sys.path.insert(0, ROOT_DIR)

# -----------------------------------------
# IMPORTS
# -----------------------------------------

import pandas as pd

from src.analytics.executive_summary import (
    generate_executive_summary
)

# -----------------------------------------
# LOAD DATA
# -----------------------------------------

data_path = os.path.join(
    ROOT_DIR,
    "data",
    "processed",
    "clean_events.csv"
)

df = pd.read_csv(data_path)

# -----------------------------------------
# GENERATE REPORT
# -----------------------------------------

generate_executive_summary(df)

print("Executive Summary PDF Created Successfully")