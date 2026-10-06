# 📊 Customer Churn Prediction and Retention Analysis

## 🚀 Live Demo

**Streamlit Application:**
https://customer-churn-prediction-kaustubh.streamlit.app/

**Kaggle Notebook:**
https://www.kaggle.com/code/kaustubhmukdam/customer-churn-prediction-and-retention-analysis

---

# 📌 Project Overview

Customer churn is one of the most critical challenges faced by subscription-based businesses. Losing existing customers directly impacts revenue, customer lifetime value, and long-term business growth.

This project develops an end-to-end Machine Learning solution to predict customer churn using the IBM Telco Customer Churn dataset. Beyond prediction, the project focuses on business-oriented insights through explainability, risk segmentation, and actionable retention strategies.

The final solution is deployed as an interactive Streamlit application that allows users to estimate churn probability and receive retention recommendations.

---

# 🎯 Business Problem

Customer churn occurs when existing customers stop using a company's services.

The objective of this project is to:

* Predict customers likely to churn
* Identify key churn drivers
* Segment customers based on risk levels
* Generate actionable retention recommendations
* Support business decision-making using Machine Learning

---

# 📂 Dataset

**Dataset:** IBM Telco Customer Churn Dataset

The dataset contains customer information including:

* Demographics
* Contract details
* Internet services
* Payment methods
* Billing information
* Customer tenure
* Churn status

Target Variable:

* Churn

  * Yes → Customer left
  * No → Customer retained

---

# 🛠️ Project Workflow

## 1. Exploratory Data Analysis (EDA)

Performed:

* Dataset exploration
* Missing value analysis
* Churn distribution analysis
* Service-based churn analysis
* Contract-based churn analysis
* Payment method analysis
* Correlation analysis

---

## 2. Data Cleaning

Performed:

* Removed unnecessary columns
* Converted TotalCharges to numeric
* Handled missing values
* Encoded categorical features
* Prepared model-ready dataset

---

## 3. Feature Engineering

Created additional features:

### Total Service Count

Measures the number of subscribed services.

### Tenure Group

Customer tenure categories.

### Average Charges Per Month

Average spending behavior metric.

These engineered features improved model performance and business interpretability.

---

# 🤖 Models Evaluated

The following machine learning models were trained and evaluated:

### Classical Models

* Logistic Regression
* Decision Tree
* Random Forest

### Advanced Models

* XGBoost
* LightGBM
* CatBoost

---

# 📈 Model Performance

## Baseline Models

| Model               | Accuracy | Precision | Recall | F1 Score | ROC-AUC |
| ------------------- | -------: | --------: | -----: | -------: | ------: |
| Logistic Regression |   79.89% |    64.09% | 55.35% |   59.40% |  83.75% |
| Decision Tree       |   77.83% |    58.07% | 59.63% |   58.84% |  81.95% |
| Random Forest       |   78.89% |    63.70% | 47.86% |   54.66% |  83.64% |

---

## Advanced Models

| Model    | Accuracy | Precision | Recall | F1 Score | ROC-AUC |
| -------- | -------: | --------: | -----: | -------: | ------: |
| XGBoost  |   79.18% |    62.46% | 54.28% |   58.08% |  83.10% |
| LightGBM |   79.25% |    62.65% | 54.28% |   58.17% |  83.53% |
| CatBoost |   79.03% |    63.12% | 50.80% |   56.29% |  83.64% |

---

# 🏆 Final Model Selection

After model comparison, hyperparameter tuning, threshold optimization, and cross-validation, the final model selected was:

## Logistic Regression

Reasons:

* Strong overall performance
* Highest practical business value
* High interpretability
* Stable cross-validation results
* Excellent ROC-AUC performance

---

## Final Model Metrics

### Logistic Regression (Threshold = 0.40)

| Metric    | Value |
| --------- | ----- |
| Precision | 58.5% |
| Recall    | 67.9% |
| F1 Score  | 62.9% |
| ROC-AUC   | 83.8% |

---

## Cross Validation

5-Fold Cross Validation ROC-AUC Scores:

```text
[0.8384, 0.8776, 0.8446, 0.8218, 0.8629]
```

Average ROC-AUC:

```text
0.849 ± 0.019
```

The low standard deviation indicates strong model stability and good generalization performance.

---

# 🔍 Explainable AI (SHAP)

To improve model transparency, SHAP (SHapley Additive exPlanations) was used.

Key findings:

### Factors Increasing Churn Risk

* Fiber Optic Internet
* Electronic Check Payment
* Higher Monthly Charges
* Short Customer Tenure

### Factors Reducing Churn Risk

* Long Customer Tenure
* Two-Year Contracts
* Technical Support Services
* Online Security Services

SHAP summary plots and waterfall plots were used to explain both global and individual predictions.

---

# 📊 Risk Segmentation

Customers were segmented into three categories based on churn probability.

| Segment     | Probability Range |
| ----------- | ----------------- |
| Low Risk    | < 30%             |
| Medium Risk | 30% - 60%         |
| High Risk   | > 60%             |

---

## Segment Results

| Segment     | Percentage of Customers |
| ----------- | ----------------------: |
| Low Risk    |                   61.4% |
| Medium Risk |                   24.7% |
| High Risk   |                   13.9% |

---

## Actual Churn Rates

| Segment     | Actual Churn Rate |
| ----------- | ----------------: |
| Low Risk    |             10.4% |
| Medium Risk |             43.8% |
| High Risk   |             67.3% |

The segmentation successfully separates customers according to churn risk and helps prioritize retention efforts.

---

# 💡 Retention Recommendation Engine

The deployed application provides business recommendations based on predicted churn probability.

| Risk Level  | Recommendation              |
| ----------- | --------------------------- |
| Low Risk    | Monitor Customer            |
| Medium Risk | Offer Personalized Support  |
| High Risk   | Priority Retention Campaign |

This converts machine learning predictions into actionable business decisions.

---

# 🌐 Streamlit Deployment

An interactive Streamlit application was developed and deployed.

Features:

* Customer churn prediction
* Risk segmentation
* Retention recommendations
* Business insights dashboard
* Interactive user interface

Live Demo:

https://customer-churn-prediction-kaustubh.streamlit.app/

---

# 📁 Project Structure

```text
customer-churn-prediction/
│
├── data/
├── docs/
├── images/
├── models/
│   ├── customer_churn_logistic_regression.pkl
│   └── customer_churn_scaler.pkl
│
├── notebooks/
├── app.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

# 🔑 Key Business Insights

* Fiber Optic customers exhibit higher churn risk.
* Customer tenure is one of the strongest retention indicators.
* Long-term contracts significantly reduce churn.
* Technical support services improve retention.
* High-risk customers should be prioritized for retention campaigns.

---

# 🚀 Future Improvements

Potential enhancements:

* Real-time customer monitoring
* Automated retention campaign suggestions
* Advanced ensemble modeling
* Integration with CRM systems
* Cloud deployment using AWS or Azure
* LLM-powered customer retention recommendations

---

# 🧰 Tech Stack

### Programming

* Python

### Data Analysis

* Pandas
* NumPy

### Visualization

* Matplotlib
* Seaborn

### Machine Learning

* Scikit-Learn
* XGBoost
* LightGBM
* CatBoost

### Explainability

* SHAP

### Deployment

* Streamlit

---

# 👨‍💻 Author

**Kaustubh Mukdam**

### Connect

* GitHub: https://github.com/KaustubhMukdam
* Kaggle: https://www.kaggle.com/kaustubhmukdam

---

⭐ If you found this project useful, consider starring the repository.
