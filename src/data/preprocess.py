import pandas as pd
from sklearn.preprocessing import LabelEncoder


class DataPreprocessor:

    def clean_data(self, df):
        df = df.copy()

        df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
        df.dropna(inplace=True)

        binary_cols = [
            "Partner",
            "Dependents",
            "PhoneService",
            "PaperlessBilling",
            "Churn"
        ]

        for col in binary_cols:
            df[col] = df[col].map({"Yes": 1, "No": 0})

        object_cols = df.select_dtypes(include="object").columns

        le = LabelEncoder()

        for col in object_cols:
            if col != "customerID":
                 df[col] = le.fit_transform(df[col])

        return df