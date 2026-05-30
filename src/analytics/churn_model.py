import pandas as pd
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

from src.config import CLEAN_DATA_PATH
from src.config import CHURN_MODEL_PATH


def train_churn_model():

    df = pd.read_csv(CLEAN_DATA_PATH)

    X = df.drop(columns=["customerID", "Churn"])

    y = df["Churn"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = RandomForestClassifier()

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(
        y_test,
        predictions
    )

    print(f"Model Accuracy: {accuracy}")

    os.makedirs(
        "models",
        exist_ok=True
    )

    joblib.dump(
        model,
        CHURN_MODEL_PATH
    )

    prediction_df = X_test.copy()

    prediction_df["Actual"] = y_test.values

    prediction_df["Predicted"] = predictions

    os.makedirs(
        "data/processed",
        exist_ok=True
    )

    prediction_df.to_csv(
        "data/processed/churn_predictions.csv",
        index=False
    )

    print("Churn Predictions Saved")

    print("Model saved successfully")