import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import streamlit as st
import pandas as pd
import plotly.express as px

from sklearn.cluster import KMeans

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
st.title("👥 Customer Segmentation")

df = pd.read_csv("data/processed/clean_events.csv")

features = df[['tenure', 'MonthlyCharges', 'TotalCharges']]

kmeans = KMeans(
    n_clusters=4,
    random_state=42
)

df['Segment'] = kmeans.fit_predict(features)

fig = px.scatter(
    df,
    x='MonthlyCharges',
    y='TotalCharges',
    color='Segment',
    title='Customer Segmentation'
)

st.plotly_chart(fig, use_container_width=True)