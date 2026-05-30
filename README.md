# 📊 Funnel Analysis System

## 🚀 Live Demo

### Streamlit Application

🔗 Live App:

https://funnel-analysis-system-cyycuwn5ez8f8py2krfkyh.streamlit.app/

---

# 1. Project Overview

The **Funnel Analysis System** is an end-to-end Business Intelligence and Customer Analytics platform designed to analyze customer behavior, churn patterns, revenue trends, retention metrics, and customer segmentation.

This project combines:

* Data Engineering
* SQL Analytics
* Machine Learning
* Power BI Dashboards
* Streamlit Web Application
* ETL Pipelines
* Customer Churn Prediction

The system helps businesses monitor KPIs, identify churn risks, improve retention strategies, and make data-driven decisions.

---

# 2. Business Problem

Customer churn is one of the major challenges faced by subscription-based businesses and telecom industries.

Businesses often struggle to:

* Identify customers likely to churn
* Understand customer retention behavior
* Analyze revenue contribution
* Track funnel conversion performance
* Detect high-value customers
* Improve customer lifetime value

Without proper analytics, businesses lose revenue and customer loyalty.

This project solves these challenges using advanced analytics and interactive dashboards.

---

# 3. Objectives

The main objectives of this project are:

* Build a complete customer analytics platform
* Analyze customer funnel and retention behavior
* Predict customer churn using Machine Learning
* Create interactive dashboards using Streamlit and Power BI
* Perform SQL-based business analytics
* Generate executive business reports
* Improve decision-making using insights

---

# 4. Dataset Description

The dataset contains customer subscription and telecom-related information.

## Dataset Features

| Feature         | Description                     |
| --------------- | ------------------------------- |
| customerID      | Unique customer identifier      |
| gender          | Male/Female                     |
| SeniorCitizen   | Senior citizen status           |
| Partner         | Whether customer has a partner  |
| Dependents      | Whether customer has dependents |
| tenure          | Customer subscription duration  |
| PhoneService    | Phone service availability      |
| InternetService | Internet service type           |
| Contract        | Contract type                   |
| PaymentMethod   | Customer payment method         |
| MonthlyCharges  | Monthly subscription charges    |
| TotalCharges    | Total customer charges          |
| Churn           | Customer churn status           |

---

# 5. Architecture

```text
                ┌──────────────────┐
                │ Raw CSV Dataset  │
                └────────┬─────────┘
                         │
                         ▼
               ┌───────────────────┐
               │ Data Preprocessing│
               └────────┬──────────┘
                        │
        ┌───────────────┼────────────────┐
        ▼               ▼                ▼
┌────────────┐ ┌──────────────┐ ┌────────────────┐
│ SQL Engine │ │ ML Pipeline  │ │ ETL Pipeline   │
└─────┬──────┘ └──────┬───────┘ └────────┬───────┘
      ▼                ▼                  ▼
┌────────────┐ ┌──────────────┐ ┌────────────────┐
│ Analytics  │ │ Churn Model  │ │ Processed Data │
└─────┬──────┘ └──────┬───────┘ └────────┬───────┘
      ▼                ▼                  ▼
 ┌──────────────────────────────────────────────┐
 │ Power BI Dashboard + Streamlit Dashboard     │
 └──────────────────────────────────────────────┘
```

---

# 6. Features

## ✅ Data Processing

* Data Cleaning
* Missing Value Handling
* Feature Engineering
* Data Validation

## ✅ SQL Analytics

* Funnel Analysis
* Retention Analysis
* Cohort Analysis
* KPI Monitoring
* Advanced Joins

## ✅ Machine Learning

* Customer Churn Prediction
* Customer Segmentation
* Retention Modeling

## ✅ Dashboards

* Interactive Streamlit Dashboard
* Power BI Dashboard
* KPI Cards
* Cohort Heatmaps

## ✅ Reporting

* Executive Summary Generation
* Business Recommendations
* KPI Reporting

---

# 7. SQL Analytics

## SQL Modules

| File                  | Purpose                         |
| --------------------- | ------------------------------- |
| funnel_queries.sql    | Funnel Conversion Analysis      |
| retention_queries.sql | Customer Retention Analysis     |
| cohort_analysis.sql   | Cohort Behavior Analysis        |
| traffic_analysis.sql  | Traffic and Engagement Analysis |
| kpi_monitoring.sql    | KPI Calculations                |
| advanced_joins.sql    | Advanced Business Joins         |

### SQL Operations Performed

* GROUP BY
* CASE WHEN
* Window Functions
* Common Table Expressions (CTEs)
* Aggregate Functions
* JOIN Operations
* Ranking Functions

---

# 8. Dashboard Screenshots

## 📌 Power BI Dashboard

### Page 1 — Executive KPI Dashboard

![Executive KPI Dashboard](assets/screenshots/powerbi_page1.png)

---

### Page 2 — Customer Churn Analysis

![Customer Churn Analysis](assets/screenshots/powerbi_page2.png)

---

### Page 3 — Customer Segmentation & Revenue Analysis

![Customer Segmentation & Revenue Analysis](assets/screenshots/powerbi_page3.png)

---

### Page 4 — Retention & Cohort Analysis

![Retention & Cohort Analysis](assets/screenshots/powerbi_page4.png)

---

### Page 5 — Executive Summary Dashboard

![Executive Summary Dashboard](assets/screenshots/powerbi_page5.png)

---

# 9. Streamlit App

The project includes an interactive Streamlit dashboard.

### Features

* KPI Monitoring
* Churn Prediction
* Revenue Analysis
* Customer Segmentation
* Interactive Charts
* Heatmaps
* Executive Reporting

### Run Streamlit App

```bash
streamlit run streamlit_app/app.py
```

---

# 10. Key Insights

## 📈 Business Insights

* Month-to-month contract customers show the highest churn.
* Customers with short tenure are more likely to churn.
* Fiber optic customers contribute higher revenue.
* Long-term contracts improve customer retention.
* Higher monthly charges increase churn probability.
* Electronic check users show higher churn risk.
* Loyal customers generate higher lifetime value.

---

# 11. Business Recommendations

## ✅ Recommendations

* Introduce loyalty programs for long-term customers.
* Improve onboarding experience for new users.
* Provide discounts for high-risk customers.
* Enhance customer support quality.
* Promote yearly and long-term contracts.
* Build personalized retention campaigns.
* Improve customer engagement strategies.

---

# 12. Tech Stack

## Programming Languages

* Python
* SQL

## Libraries

* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Plotly
* Streamlit

## Database

* MySQL

## Visualization Tools

* Power BI
* Streamlit

## Deployment

* Streamlit Community Cloud
* Docker
* Render
* Railway

## Development Tools

* VS Code
* Jupyter Notebook

---

# 13. Future Improvements

## 🚀 Future Enhancements

* Real-Time Analytics Dashboard
* Cloud Deployment using AWS/GCP
* Advanced ML Models
* Recommendation System
* Automated Report Generation
* API Integration
* Real-Time Churn Monitoring
* Customer Sentiment Analysis
* Predictive Revenue Forecasting

---

# 📂 Project Structure

```text
funnel-analysis-system/
│
├── data/
├── notebooks/
├── sql/
├── src/
├── dashboard/
├── reports/
├── models/
├── streamlit_app/
├── tests/
├── main.py
├── requirements.txt
├── README.md
└── docker-compose.yml
```

---

# 🚀 Run the Project

## 1. Install Dependencies

```bash
pip install -r requirements.txt
```

## 2. Run ETL Pipeline

```bash
python main.py
```

## 3. Run Streamlit Dashboard

```bash
streamlit run streamlit_app/app.py
```

---

# 📊 Final Deliverables

✅ ETL Pipeline

✅ SQL Analytics

✅ Churn Prediction Model

✅ Power BI Dashboard

✅ Streamlit Dashboard

✅ Executive Summary Reports

✅ Customer Segmentation

✅ Retention Analysis

✅ Business Intelligence Platform
