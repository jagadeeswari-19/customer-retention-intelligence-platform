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
import plotly.express as px

from src.analytics.funnel_metrics import funnel_analysis

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
# PAGE TITLE
# -----------------------------------------

st.title("📈 KPI Dashboard")

# -----------------------------------------
# LOAD DATA
# -----------------------------------------

BASE_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        '../..'
    )
)

data_path = os.path.join(
    BASE_DIR,
    'data',
    'processed',
    'clean_events.csv'
)

df = pd.read_csv(data_path)

# -----------------------------------------
# KPI METRICS
# -----------------------------------------

metrics = funnel_analysis(df)

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "Total Users",
    metrics["Total Users"]
)

col2.metric(
    "Active Customers",
    metrics["Active Customers"]
)

col3.metric(
    "Churned Customers",
    metrics["Churned Customers"]
)

col4.metric(
    "Retention Rate",
    f"{metrics['Retention Rate']:.2f}%"
)

col5.metric(
    "Churn Rate",
    f"{metrics['Churn Rate']:.2f}%"
)

st.markdown("---")

# -----------------------------------------
# CHARTS
# -----------------------------------------

fig1 = px.histogram(
    df,
    x="Contract",
    color="Churn",
    title="Contract Analysis"
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

fig2 = px.box(
    df,
    x="Churn",
    y="MonthlyCharges",
    color="Churn",
    title="Monthly Charges vs Churn"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)