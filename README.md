# Customer Retention Intelligence Platform

An end-to-end **customer churn and retention analytics platform** built with SQL, Python, Random Forest, Power BI, and Streamlit.

The project combines customer-level analytics, churn prediction, customer segmentation, cohort analysis, and revenue analysis to identify at-risk customer groups and support retention-focused decision making.

---

## 🚀 Live Demo

### Streamlit Application

🔗 **Live App:**

https://customer-retention-intelligence-platform-so9jqrreovwkbhehg65lo.streamlit.app/

---

## 📌 Key Findings

- **Dataset:** 7,032 customers
- **Total Revenue:** 16.06M
- **Churn Rate:** 26.58% (1,869 customers churned)
- **Higher-risk groups:** Month-to-month contract customers, short-tenure customers, and electronic-check payment customers
- **Customer Segmentation:** 1,135 high-value customers and 2,303 loyal customers
- **Long-term contracts:** Show stronger retention patterns and higher customer value
- **Churn Model:** Random Forest
- **ROC-AUC:** 0.813
- **Recall:** 0.489
- **Precision:** 0.644
- **Accuracy:** 0.792

---

## 📊 Project Overview

Customer churn can directly affect recurring revenue and customer lifetime value.

This project was built to answer key business questions such as:

- Which customers are most likely to churn?
- Which high-value customers are at risk?
- Which customer segments require retention attention?
- How much revenue is associated with at-risk customers?
- Which customer characteristics are associated with churn?
- How accurately can a machine learning model identify churners?
- How can churn predictions be connected with customer value and retention analysis?

### Project Pipeline

```text
Data Cleaning
      ↓
Exploratory Data Analysis
      ↓
SQL Analysis
      ↓
Customer Segmentation
      ↓
Cohort Analysis
      ↓
Churn Prediction
      ↓
Model Evaluation
      ↓
Retention & Revenue Analysis
      ↓
Power BI Dashboard
      ↓
Interactive Streamlit Application
🔑 Key Features
1. Customer Churn Analysis

The project analyzes customer-level information to identify patterns associated with churn.

The analysis covers:

Customer demographics
Service usage
Contract information
Payment information
Tenure
Revenue-related metrics
Churn behavior
2. Churn Prediction

A Random Forest classification model is used to predict whether a customer is likely to churn.

The model generates:

Churn predictions
Churn probabilities
Model performance metrics
Customer-level prediction outputs
3. Model Evaluation

The churn model is evaluated using:

ROC-AUC
Recall
Precision
Accuracy
Why Recall Matters

For churn prediction, accuracy alone can be misleading because the dataset contains more non-churners than churners.

A model can achieve relatively high accuracy while still failing to identify a significant proportion of customers who actually churn.

Therefore, this project evaluates ROC-AUC, recall, precision, and accuracy together.

🤖 Churn Model Evaluation

The model uses an 80/20 train-test split.

Training Data → 80%
Test Data     → 20%

The test set is used to evaluate model performance on unseen customer records.

The model generates:

y_pred = model.predict(X_test)

y_prob = model.predict_proba(X_test)[:, 1]

These outputs are used to calculate the evaluation metrics.

Evaluation Metrics
ROC-AUC

ROC-AUC measures the model's ability to distinguish between churners and non-churners across different classification thresholds.

Result: 0.813

Recall

Recall measures the proportion of actual churners successfully identified by the model.

Recall =
True Positives
-------------------------
True Positives + False Negatives

Result: 0.489

The current model identifies approximately 48.9% of the actual churners at the current classification threshold.

Precision

Precision measures the proportion of customers predicted as churners who were actually churners.

Precision =
True Positives
-------------------------
True Positives + False Positives

Result: 0.644

Accuracy

Accuracy measures the overall proportion of correctly classified customers.

Accuracy =
Correct Predictions
-------------------------
Total Predictions

Result: 0.792

Accuracy is reported for completeness and is not treated as the only measure of model performance.

📈 Model Performance
Metric	Test Set Result
ROC-AUC	0.813
Recall	0.489
Precision	0.644
Accuracy	0.792

These results were generated from the current Random Forest model training run.

Model performance depends on the dataset, feature preparation, train/test split, model configuration, and classification threshold.

🎯 Classification Threshold

The reported classification metrics are calculated using the model's current classification threshold.

For a customer retention use case, different thresholds can produce different precision-recall trade-offs.

A future improvement is to evaluate alternative thresholds based on the relative business cost of:

Missing a customer who eventually churns
Contacting a customer who would not have churned
👥 Customer Retention Analysis

The project goes beyond simply predicting churn.

Churn predictions are combined with customer value and behavioral information to identify customers who may require retention attention.

The analysis considers:

Churn probability
Customer value
Revenue contribution
Customer segments
Service characteristics
Contract characteristics
Tenure

This allows customers to be analyzed across combinations such as:

High-risk / Low-value customers
High-risk / High-value customers
Low-risk / High-value customers
Low-risk / Low-value customers

A key analytical focus is identifying customers who combine elevated churn risk with meaningful customer value.

👥 Customer Segmentation

Customer segmentation is used to group customers based on behavioral and value-related characteristics.

The project analyzes variables such as:

Revenue
Tenure
Usage
Customer value
Churn behavior
Key Segments
1,135 high-value customers
2,303 loyal customers

Segmentation helps identify groups with different retention characteristics rather than treating every customer identically.

📅 Cohort Analysis

Tenure-based cohort analysis is used to compare customer retention patterns across different customer tenure groups.

The analysis provides additional customer lifecycle context and helps examine how retention behavior varies between newer and longer-tenured customers.

The Power BI cohort dashboard provides a visual view of customer distribution across tenure groups and retention-related patterns.

💰 Revenue & Retention Analysis

The platform connects churn risk with financial impact.

This allows analysis of:

Revenue associated with at-risk customers
Customer value distribution
Potential retention opportunities
Revenue concentration
High-value customer risk

The objective is to move from:

"Who might churn?"

to:

"Which potentially valuable customers are at risk, and where should retention analysis focus?"

🗄️ SQL Analysis

SQL is used for customer-level analysis, business reporting, churn analysis, segmentation, and revenue analysis.

SQL Techniques

The project uses analytical SQL techniques including:

SELECT
WHERE and filtering
GROUP BY
Aggregations
CASE WHEN
JOINs
Common Table Expressions (CTEs)
Window functions
Customer-level metrics
Revenue analysis
Churn analysis
Segment-level analysis

SQL scripts are available in the sql/ directory.

Analytical Questions

The SQL analysis is designed to answer questions such as:

Which customer segments have the highest churn?
Which customers contribute the most revenue?
What is the distribution of customer value?
Which customer groups have elevated churn risk?
How does churn vary across contract types?
How does customer behavior vary across tenure groups?
🐍 Python Analysis

Python is used for:

Data cleaning
Feature preparation
Exploratory analysis
Churn modeling
Customer segmentation
Model evaluation
Prediction generation
Main Libraries
Pandas
NumPy
Scikit-learn
Matplotlib
Seaborn
Joblib
📊 Power BI Dashboards

The project includes three Power BI dashboards covering different aspects of customer churn, retention, cohort behavior, segmentation, and revenue.

1. Customer Churn Analysis Dashboard

This dashboard focuses on:

Churned customers
Churn rate
Revenue loss
Churn by contract type
Churn by internet service
Payment method vs churn
Customer tenure vs churn
Monthly charges vs churn
Interactive filtering

2. Customer Retention & Cohort Analysis Dashboard

This dashboard focuses on:

Retention rate
Average tenure
Loyal customers
Retained customers
Customer retention curve
Customer cohort analysis
Customer tenure distribution
Contract-based retention analysis
Churn by tenure group

3. Customer Segmentation & Revenue Analysis Dashboard

This dashboard focuses on:

Total revenue
Average revenue
Average monthly charges
High-value customers
Revenue by contract type
Revenue by internet service
Customer segmentation
Customer lifetime value by contract type
Monthly revenue distribution

🖥️ Streamlit Application

A Streamlit application provides an interactive interface for exploring the customer retention analysis.

The application can be used to present:

Customer analytics
Churn predictions
Risk information
Customer segments
Revenue analysis
Retention insights

🔗 Live Application:

https://customer-retention-intelligence-platform-so9jqrreovwkbhehg65lo.streamlit.app/

🔄 Project Workflow
Customer Dataset
       │
       ▼
Data Cleaning
       │
       ▼
Feature Preparation
       │
       ├───────────────┐
       ▼               ▼
   SQL Analysis    Python Analysis
       │               │
       │               ▼
       │        Churn Model
       │               │
       │               ▼
       │        Model Evaluation
       │               │
       └───────┬───────┘
               ▼
      Customer Segmentation
               │
               ▼
      Cohort Analysis
               │
               ▼
      Retention & Revenue
           Analysis
               │
        ┌──────┴──────┐
        ▼             ▼
   Power BI       Streamlit
    Dashboards     Application
📦 Dataset

The project uses a customer churn dataset containing 7,032 customer records.

Dataset Characteristics

The dataset contains customer-level information related to:

Customer demographics
Services
Contracts
Payment methods
Tenure
Revenue-related information
Churn status
📁 Project Structure
customer-retention-intelligence-platform/
│
├── assets/
│   ├── dashboard_1.png
│   ├── dashboard_2.png
│   └── dashboard_3.png
│
├── data/
│   ├── raw/
│   └── processed/
│
├── dashboard/
│   └── PowerBI_dashboard.pdf
│
├── models/
│   └── churn_model.pkl
│
├── notebooks/
│
├── sql/
│   └── executed_sql.sql
│
├── src/
│   ├── analytics/
│   │   └── churn_model.py
│   └── ...
│
├── streamlit_app/
│
├── tests/
│   └── test_mysql.py
│
├── reports/
│
├── main.py
├── generate_report.py
├── requirements.txt
├── README.md
└── .gitignore
Important Files

src/analytics/churn_model.py
Trains and evaluates the Random Forest churn model.

sql/executed_sql.sql
Contains SQL-based customer, churn, revenue, and segmentation analysis.

main.py
Main application or pipeline entry point.

generate_report.py
Generates project analysis/report outputs.

tests/test_mysql.py
Contains database-related testing functionality.

requirements.txt
Contains the Python dependencies required to run the project.

🛠️ Technologies Used
Programming
Python
Data Analysis
Pandas
NumPy
Machine Learning
Scikit-learn
Random Forest
Database / SQL
MySQL
SQL
Visualization
Power BI
Matplotlib
Seaborn
Application
Streamlit
Model Persistence
Joblib
Version Control
Git
GitHub
⚙️ Installation
1. Clone the Repository
git clone https://github.com/jagadeeswari-19/customer-retention-intelligence-platform.git
cd customer-retention-intelligence-platform
2. Create a Virtual Environment
Windows
python -m venv venv

Activate:

venv\Scripts\activate
macOS/Linux
python3 -m venv venv

Activate:

source venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
🧠 Train the Churn Model

From the project root, run:

python -m src.analytics.churn_model

Running the module from the project root ensures imports such as:

from src.config import CLEAN_DATA_PATH

resolve correctly.

Training Pipeline

The training pipeline:

Loads the cleaned customer dataset
Separates features and churn target
Creates the train/test split
Trains the Random Forest model
Generates predictions
Calculates ROC-AUC
Calculates accuracy
Calculates recall
Calculates precision
Saves the trained model
Saves customer-level predictions
Current Model Output
ROC-AUC  : 0.813
Accuracy : 0.792
Recall   : 0.489
Precision: 0.644
📤 Model Output

The training pipeline saves customer-level prediction results.

The prediction dataset can be used to compare:

Actual Churn
Predicted Churn
Churn Probability

The churn probability can also be used as an input for customer risk analysis and retention-oriented segmentation.

💼 Business Applications
Customer Risk Identification

Identify customers with elevated predicted churn risk.

High-Value Customer Monitoring

Combine churn risk with customer value to identify customers requiring closer analysis.

Retention Planning

Use customer-level risk information as an analytical input for retention planning.

Revenue Risk Analysis

Analyze revenue associated with customers identified as being at risk.

Customer Segmentation

Analyze differences between customer groups to support targeted retention analysis.

🎯 Key Project Outcomes

The project demonstrates an end-to-end workflow connecting:

SQL
 +
Python
 +
Machine Learning
 +
Customer Segmentation
 +
Cohort Analysis
 +
Revenue Analysis
 +
Power BI
 +
Streamlit

The main objective is not only to build a churn classifier, but to connect prediction outputs with customer value and retention-oriented business analysis.

🚀 Future Improvements

Potential extensions include:

Hyperparameter tuning
Cross-validation
Probability calibration
Classification threshold optimization
Optimization based on retention costs
Model comparison with Logistic Regression and XGBoost
Customer lifetime value modeling
Retention recommendation engine
Automated model monitoring
Model drift detection
Automated dashboard refresh
API deployment
Cloud deployment
🔐 Security & Configuration

Database credentials and other secrets should not be hard-coded in the source code.

Use environment variables for sensitive configuration such as:

MYSQL_HOST
MYSQL_USER
MYSQL_PASSWORD
MYSQL_DATABASE

A local .env file can be used during development and should be excluded from Git using .gitignore.

Never commit passwords, API keys, tokens, or other credentials to the repository.

👤 Author

Jagadeeswari S.

B.Tech — Artificial Intelligence & Data Science

Areas of Interest
Data Analytics
Business Intelligence
Machine Learning
Customer Analytics
Predictive Analytics
SQL
Python
Power BI
⚠️ Disclaimer

This project is intended for educational and portfolio purposes.

Model performance depends on the dataset, feature preparation, train/test split, model configuration, and classification threshold.

The current model achieves a ROC-AUC of 0.813, while its recall of 0.489 indicates that there is room to improve the identification of actual churners. Future threshold optimization and model tuning can be evaluated based on the business cost of missed churners versus unnecessary retention interventions.
