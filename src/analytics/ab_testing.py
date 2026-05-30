from scipy.stats import ttest_ind
import pandas as pd
import os


def run_ab_test(group_a, group_b):

    stat, pvalue = ttest_ind(
        group_a,
        group_b
    )

    result = pd.DataFrame({

        "t_statistic": [stat],

        "p_value": [pvalue],

        "significant": [pvalue < 0.05]

    })

    os.makedirs(
        "data/processed",
        exist_ok=True
    )

    result.to_csv(
        "data/processed/ab_test_results.csv",
        index=False
    )

    print("A/B Test Results Saved")

    return result