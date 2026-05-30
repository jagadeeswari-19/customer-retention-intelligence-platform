import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '../..'
        )
    )
)

import streamlit as st
import pandas as pd
import joblib

# -----------------------------------------
# LOAD CSS
# -----------------------------------------

def load_css():

    css_path = os.path.join(
        os.path.dirname(__file__),
        '../assets/styles.css'
    )

    with open(css_path) as f:

        st.markdown(
            f'<style>{f.read()}</style>',
            unsafe_allow_html=True
        )

load_css()

# -----------------------------------------
# TITLE
# -----------------------------------------

st.title("🤖 Churn Prediction")

# -----------------------------------------
# LOAD MODEL
# -----------------------------------------

model_path = os.path.join(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '../..'
        )
    ),
    'models',
    'churn_model.pkl'
)

model = joblib.load(model_path)

# -----------------------------------------
# USER INPUTS
# -----------------------------------------

gender = st.selectbox(
    "Gender",
    [0, 1]
)

SeniorCitizen = st.selectbox(
    "Senior Citizen",
    [0, 1]
)

Partner = st.selectbox(
    "Partner",
    [0, 1]
)

Dependents = st.selectbox(
    "Dependents",
    [0, 1]
)

tenure = st.slider(
    "Tenure",
    1,
    72,
    12
)

PhoneService = st.selectbox(
    "Phone Service",
    [0, 1]
)

PaperlessBilling = st.selectbox(
    "Paperless Billing",
    [0, 1]
)

MonthlyCharges = st.number_input(
    "Monthly Charges",
    0.0,
    200.0,
    70.0
)

TotalCharges = st.number_input(
    "Total Charges",
    0.0,
    10000.0,
    1500.0
)

# -----------------------------------------
# PREDICTION
# -----------------------------------------

if st.button("Predict Churn"):

    sample = pd.DataFrame({

        'gender': [gender],
        'SeniorCitizen': [SeniorCitizen],
        'Partner': [Partner],
        'Dependents': [Dependents],
        'tenure': [tenure],
        'PhoneService': [PhoneService],
        'PaperlessBilling': [PaperlessBilling],
        'MonthlyCharges': [MonthlyCharges],
        'TotalCharges': [TotalCharges]

    })

    # ADD MISSING COLUMNS

    required_columns = model.feature_names_in_

    for col in required_columns:

        if col not in sample.columns:

            sample[col] = 0

    # REORDER COLUMNS

    sample = sample[required_columns]

    prediction = model.predict(sample)

    probability = model.predict_proba(sample)

    st.subheader("Prediction Result")

    if prediction[0] == 1:

        st.error("⚠ Customer Likely to Churn")

    else:

        st.success("✅ Customer Likely to Stay")

    st.write(
        f"Churn Probability: {probability[0][1] * 100:.2f}%"
    )