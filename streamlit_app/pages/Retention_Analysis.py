import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🔄 Retention Analysis")

df = pd.read_csv("data/processed/clean_events.csv")

retention = df.groupby("tenure").size().reset_index(name="Customers")

fig = px.line(
    retention,
    x="tenure",
    y="Customers",
    title="Retention Curve"
)

st.plotly_chart(fig, use_container_width=True)