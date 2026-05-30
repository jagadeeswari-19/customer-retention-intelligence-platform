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

st.title("📑 Reports")

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
# DATA PREVIEW
# -----------------------------------------

st.subheader("Dataset Preview")

st.dataframe(df.head(20))

# -----------------------------------------
# DOWNLOAD CSV
# -----------------------------------------

csv = df.to_csv(index=False).encode('utf-8')

st.download_button(
    label="Download Processed Dataset",
    data=csv,
    file_name='clean_events.csv',
    mime='text/csv'
)

# -----------------------------------------
# DOWNLOAD PDF
# -----------------------------------------

pdf_path = os.path.join(
    BASE_DIR,
    'reports',
    'executive_summary.pdf'
)

if os.path.exists(pdf_path):

    with open(pdf_path, "rb") as pdf_file:

        st.download_button(
            label="Download Executive Summary PDF",
            data=pdf_file,
            file_name="executive_summary.pdf",
            mime="application/pdf"
        )