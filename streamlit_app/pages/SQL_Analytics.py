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

st.title("🗄 SQL Analytics")

st.markdown("""

# SQL Analytics Included

### Queries Available

- Funnel Queries
- Retention Queries
- Cohort Queries
- KPI Monitoring Queries
- Advanced Join Queries

### SQL Folder

sql/

""")