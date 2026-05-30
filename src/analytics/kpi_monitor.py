import pandas as pd

from src.config import CLEAN_DATA_PATH
from src.analytics.funnel_metrics import funnel_analysis



def generate_kpis():

    df = pd.read_csv(CLEAN_DATA_PATH)

    metrics = funnel_analysis(df)

    for key, value in metrics.items():
        print(f"{key}: {value}")