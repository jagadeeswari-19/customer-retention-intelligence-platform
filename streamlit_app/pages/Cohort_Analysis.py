import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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
st.title("📅 Cohort Analysis")

df = pd.read_csv("data/processed/clean_events.csv")

cohort = df.groupby("tenure").agg({
    "MonthlyCharges": "mean",
    "TotalCharges": "mean"
})

fig, ax = plt.subplots(figsize=(10,6))

sns.heatmap(cohort.corr(), annot=True)

st.pyplot(fig)