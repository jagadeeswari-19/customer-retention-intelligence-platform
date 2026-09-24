# Customer Retention Intelligence Platform

An end-to-end **customer churn and retention analytics platform** that combines SQL, Python, machine learning, Power BI, and Streamlit to identify customers at risk of churn and support data-driven retention decisions.

The project analyzes customer behavior, predicts churn probability, identifies high-value customers at risk, and provides interactive analytics for understanding retention and revenue impact.

---

## 🚀 Live Demo

### Streamlit Application

🔗 Live App:

https://customer-retention-intelligence-platform-so9jqrreovwkbhehg65lo.streamlit.app/

---
## Live Dashboard Demo

Watch the complete dashboard walkthrough:

[▶️ View Demo Video](assets/demo_video.mp4)

----

## Project Overview

Customer churn directly affects recurring revenue and customer lifetime value.

This project was built to answer key business questions such as:

- Which customers are most likely to churn?
- Which high-value customers are at risk?
- Which customer segments require retention attention?
- How much revenue is associated with at-risk customers?
- Which factors are associated with customer churn?
- How accurately can a machine learning model identify churners?
- How can churn predictions be converted into actionable retention insights?

The platform combines:

```text
Data Cleaning
      ↓
Exploratory Data Analysis
      ↓
SQL Analysis
      ↓
Customer Segmentation
      ↓
Churn Prediction
      ↓
Model Evaluation
      ↓
Retention & Revenue Analysis
      ↓
Interactive Dashboard
Key Features
1. Customer Churn Analysis

Analyzes customer-level information to identify patterns associated with churn.

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

A model that predicts most customers as "No Churn" can still achieve relatively high accuracy while failing to identify customers who are actually going to churn.

Therefore, this project emphasizes:

ROC-AUC
Recall
Precision

in addition to accuracy.

Churn Model Evaluation

The model uses a train/test split:

Training Data → 80%
Test Data     → 20%

The test set is used to evaluate the model on unseen customer records.

The model generates:

y_pred = model.predict(X_test)

y_prob = model.predict_proba(X_test)[:, 1]

These are then used to calculate:

ROC-AUC
Accuracy
Recall
Precision
Evaluation Metrics
ROC-AUC

ROC-AUC measures the model's ability to distinguish between churners and non-churners across different classification thresholds.

Higher ROC-AUC indicates better ranking/separation of the two classes.

Recall

Recall measures the proportion of actual churners that the model successfully identifies.

Recall =
True Positives
-------------------------
True Positives + False Negatives

For retention analysis, recall is particularly useful because missing a customer who actually churns can mean missing an opportunity for intervention.

Precision

Precision measures how many customers predicted as churners were actually churners.

Precision =
True Positives
-------------------------
True Positives + False Positives
Accuracy

Accuracy measures the overall proportion of correctly classified customers.

Accuracy =
Correct Predictions
-------------------------
Total Predictions

Accuracy is reported for completeness but is not treated as the only measure of model quality.

Model Performance

Run the training script to generate the actual evaluation results.

Current Results
Metric	Test Set Result
ROC-AUC	To be generated
Recall	To be generated
Precision	To be generated
Accuracy	To be generated

The values should be updated after running the final churn model.

Portfolio Metric

After obtaining the actual results, the project can be summarized using the real ROC-AUC and recall values.

Example format:

ROC-AUC: X.XX
Recall: X.XX

Do not replace these placeholders with example values unless they are produced by the actual model run.

Customer Retention Analysis

The project goes beyond simply predicting churn.

It combines churn predictions with customer value and behavioral information to identify customers who may require retention attention.

The analysis considers:

Churn probability
Customer value
Revenue contribution
Customer segments
Service characteristics
Contract characteristics

This allows the analysis to distinguish between:

High-risk / Low-value customers
High-risk / High-value customers
Low-risk / High-value customers
Low-risk / Low-value customers

The highest-priority analytical segment is customers who combine elevated churn risk with meaningful customer value.

Customer Segmentation

Customer segmentation is used to group customers based on behavioral and value-related characteristics.

The project analyzes customer groups using variables such as:

Revenue
Tenure
Usage
Customer value
Churn behavior

Segmentation helps identify groups with different retention characteristics rather than treating every customer identically.

Revenue & Retention Analysis

The platform connects churn risk with financial impact.

This allows analysis of:

Revenue associated with at-risk customers
Customer value distribution
Potential retention opportunity
Revenue concentration
High-value customer risk

The goal is to move from:

"Who might churn?"

to:

"Which potentially valuable customers are at risk,
and where should retention analysis focus?"
SQL Analysis

SQL is used for customer-level analysis and business reporting.

Key analytical operations include:

Aggregation
GROUP BY
CASE statements
Filtering
Joins
Customer-level metrics
Revenue analysis
Churn analysis
Segment-level analysis

Example analytical questions include:

Which customer segments have the highest churn?

Which customers contribute the most revenue?

What is the distribution of customer value?

Which customer groups have elevated churn risk?
Python Analysis

Python is used for:

Data cleaning
Feature preparation
Exploratory analysis
Churn modeling
Customer segmentation
Model evaluation
Prediction generation

Main libraries include:

Pandas
NumPy
Scikit-learn
Matplotlib
Seaborn
Joblib
Power BI Dashboard

The project includes interactive Power BI reporting for customer retention analysis.

The dashboard is designed to provide visibility into:

Customer count
Churn rate
Revenue
Customer value
At-risk customers
Customer segments
Retention-related KPIs

The dashboard enables users to explore customer and retention patterns interactively.

Streamlit Application

A Streamlit application provides an interactive interface for exploring the customer retention analysis.

The application can be used to present:

Customer analytics
Churn predictions
Risk information
Customer segments
Revenue analysis
Retention insights
Project Workflow
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
      Retention & Revenue
           Analysis
               │
        ┌──────┴──────┐
        ▼             ▼
   Power BI       Streamlit
    Dashboard      Application
Model Output

The training pipeline saves customer-level prediction results.

The prediction dataset contains information that can be used to compare:

Actual Churn
Predicted Churn

and evaluate customer-level model performance.

The model also generates churn probabilities that can be used for risk analysis.

Project Structure
customer-retention-intelligence-platform/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│   └── churn_model.pkl
│
├── notebooks/
│
├── src/
│   ├── analytics/
│   │   └── churn_model.py
│   │
│   └── ...
│
├── streamlit_app/
│
├── reports/
│
├── requirements.txt
├── README.md
└── .gitignore
Technologies Used
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
Installation
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
Train the Churn Model

From the project root, run:

python -m src.analytics.churn_model

Running the module from the project root ensures imports such as:

from src.config import CLEAN_DATA_PATH

resolve correctly.

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
Example Model Output

After training, the console reports:

ROC-AUC  : X.XXX
Accuracy : X.XXX
Recall   : X.XXX
Precision: X.XXX

The actual values depend on the dataset and model configuration.

Business Applications

The platform can support retention teams with analytical questions such as:

Customer Risk Identification

Identify customers with elevated predicted churn risk.

High-Value Customer Monitoring

Combine churn risk with customer value to identify important customers requiring closer analysis.

Retention Planning

Use customer-level risk information as an input for retention strategies.

Revenue Risk Analysis

Estimate the revenue associated with customers identified as being at risk.

Customer Segmentation

Analyze differences between customer groups to support targeted retention analysis.

Key Project Outcomes

The project demonstrates an end-to-end workflow connecting:

SQL
+
Python
+
Machine Learning
+
Customer Segmentation
+
Revenue Analysis
+
Power BI
+
Streamlit

The main objective is not only to build a churn classifier, but to connect the prediction output with customer value and retention-oriented business analysis.

Future Improvements

Potential extensions include:

Hyperparameter tuning
Cross-validation
Probability calibration
Threshold optimization based on retention costs
Model comparison with XGBoost and Logistic Regression
Churn probability calibration
Customer lifetime value modeling
Retention recommendation engine
Automated model monitoring
Model drift detection
Automated dashboard refresh
API deployment
Cloud deployment
Author

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
Disclaimer

This project is intended for educational and portfolio purposes. Model performance depends on the dataset, feature preparation, train/test split, model configuration, and evaluation methodology.