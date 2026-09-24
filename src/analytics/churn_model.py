import pandas as pd
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    roc_auc_score,
    recall_score,
    precision_score
)

from src.config import CLEAN_DATA_PATH
from src.config import CHURN_MODEL_PATH


def train_churn_model():

    # Load cleaned data
    df = pd.read_csv(CLEAN_DATA_PATH)

    # Features
    X = df.drop(columns=["customerID", "Churn"])

    # Target
    y = df["Churn"]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # Create model
    model = RandomForestClassifier(
        random_state=42
    )

    # Train model
    model.fit(X_train, y_train)

    # -----------------------------
    # Model Evaluation
    # -----------------------------

    # Predicted class
    y_pred = model.predict(X_test)

    # Probability of churn
    y_prob = model.predict_proba(X_test)[:, 1]

    # Evaluation metrics
    roc_auc = roc_auc_score(y_test, y_prob)
    accuracy = accuracy_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)

    print("\n===== CHURN MODEL PERFORMANCE =====")
    print("ROC-AUC  :", round(roc_auc, 3))
    print("Accuracy :", round(accuracy, 3))
    print("Recall   :", round(recall, 3))
    print("Precision:", round(precision, 3))

    # -----------------------------
    # Save trained model
    # -----------------------------

    os.makedirs(
        "models",
        exist_ok=True
    )

    joblib.dump(
        model,
        CHURN_MODEL_PATH
    )

    # -----------------------------
    # Save predictions
    # -----------------------------

    prediction_df = X_test.copy()

    prediction_df["Actual"] = y_test.values
    prediction_df["Predicted"] = y_pred
    prediction_df["Churn_Probability"] = y_prob

    os.makedirs(
        "data/processed",
        exist_ok=True
    )

    prediction_df.to_csv(
        "data/processed/churn_predictions.csv",
        index=False
    )

    print("\nChurn Predictions Saved")
    print("Model saved successfully")


if __name__ == "__main__":
    train_churn_model()