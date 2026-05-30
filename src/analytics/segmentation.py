from sklearn.cluster import KMeans
import os


def customer_segmentation(df):

    features = df[[
        "tenure",
        "MonthlyCharges",
        "TotalCharges"
    ]]

    model = KMeans(
        n_clusters=4,
        random_state=42
    )

    df["Segment"] = model.fit_predict(features)

    os.makedirs(
        "data/processed",
        exist_ok=True
    )

    df.to_csv(
        "data/processed/customer_segments.csv",
        index=False
    )

    print("Customer Segments Saved")

    return df