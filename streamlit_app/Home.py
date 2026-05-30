import streamlit as st
import os

# -----------------------------------------
# PAGE CONFIG
# -----------------------------------------

st.set_page_config(
    page_title="Funnel Analysis System",
    layout="wide"
)

# -----------------------------------------
# LOAD CSS
# -----------------------------------------

def load_css():

    css_path = os.path.join(
        os.path.dirname(__file__),
        'assets/styles.css'
    )

    with open(css_path) as f:

        st.markdown(
            f'<style>{f.read()}</style>',
            unsafe_allow_html=True
        )

load_css()

# -----------------------------------------
# HOME PAGE
# -----------------------------------------

st.title("📊 Funnel Analysis System")

st.markdown("""
## Features

- KPI Dashboard
- Churn Prediction
- Customer Segmentation
- Cohort Analysis
- Retention Analytics
- SQL Analytics
- Reports Dashboard

Use the sidebar to navigate between modules.
""")