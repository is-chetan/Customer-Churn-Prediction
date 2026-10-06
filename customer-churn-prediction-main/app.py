import streamlit as st
import pandas as pd
import numpy as np
import joblib
from PIL import Image
import os

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

# =========================
# LOAD MODEL & SCALER
# =========================

model = joblib.load(
    "models/customer_churn_logistic_regression.pkl"
)

scaler = joblib.load(
    "models/customer_churn_scaler.pkl"
)

# =========================
# FEATURE LIST
# =========================

FEATURE_COLUMNS = [
    'gender',
    'SeniorCitizen',
    'Partner',
    'Dependents',
    'tenure',
    'PhoneService',
    'PaperlessBilling',
    'MonthlyCharges',
    'TotalCharges',
    'MultipleLines_No phone service',
    'MultipleLines_Yes',
    'InternetService_Fiber optic',
    'InternetService_No',
    'OnlineSecurity_No internet service',
    'OnlineSecurity_Yes',
    'OnlineBackup_No internet service',
    'OnlineBackup_Yes',
    'DeviceProtection_No internet service',
    'DeviceProtection_Yes',
    'TechSupport_No internet service',
    'TechSupport_Yes',
    'StreamingTV_No internet service',
    'StreamingTV_Yes',
    'StreamingMovies_No internet service',
    'StreamingMovies_Yes',
    'Contract_One year',
    'Contract_Two year',
    'PaymentMethod_Credit card (automatic)',
    'PaymentMethod_Electronic check',
    'PaymentMethod_Mailed check',
    'tenure_group',
    'avg_charges_per_month',
    'total_services'
]

# =========================
# SIDEBAR
# =========================

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "🔮 Churn Prediction",
        "📊 Business Insights",
        "ℹ️ About"
    ]
)

# =========================
# HOME PAGE
# =========================

if page == "🏠 Home":

    st.title("📊 Customer Churn Prediction and Retention Analysis")
    st.markdown("""
    This application predicts customer churn using a Logistic Regression model trained on the IBM Telco Customer Churn dataset.

    The goal is to identify customers likely to leave and provide retention recommendations to reduce churn.
    """)

    st.markdown("""
    ### Project Overview

    This project predicts customer churn using Machine Learning.

    Dataset:
    - IBM Telco Customer Churn Dataset

    Final Model:
    - Logistic Regression

    Performance:
    - ROC-AUC: 0.84
    - Cross Validation ROC-AUC: 0.849 ± 0.019

    Features:
    - Customer demographics
    - Contract information
    - Service subscriptions
    - Billing information
    """)

# =========================
# PREDICTION PAGE
# =========================

elif page == "🔮 Churn Prediction":

    st.title("🔮 Customer Churn Prediction")

    col1, col2 = st.columns(2)

    with col1:

        gender = st.selectbox(
            "Gender",
            ["Female", "Male"]
        )

        senior = st.selectbox(
            "Senior Citizen",
            ["No", "Yes"]
        )

        partner = st.selectbox(
            "Partner",
            ["No", "Yes"]
        )

        paperless_billing = st.selectbox(
            "Paperless Billing",
            ["No", "Yes"]
        )

        dependents = st.selectbox(
            "Dependents",
            ["No", "Yes"]
        )

        tenure = st.slider(
            "Tenure (Months)",
            0,
            72,
            12
        )

        monthly_charges = st.number_input(
            "Monthly Charges",
            min_value=0.0,
            value=70.0
        )

        contract = st.selectbox(
            "Contract",
            [
                "Month-to-month",
                "One year",
                "Two year"
            ]
        )

    with col2:

        phone_service = st.selectbox(
            "Phone Service",
            ["No", "Yes"]
        )

        multiple_lines = st.selectbox(
            "Multiple Lines",
            ["No", "Yes"]
        )

        internet_service = st.selectbox(
            "Internet Service",
            [
                "DSL",
                "Fiber optic",
                "No"
            ]
        )

        online_security = st.selectbox(
            "Online Security",
            ["No", "Yes"]
        )

        online_backup = st.selectbox(
            "Online Backup",
            ["No", "Yes"]
        )

        device_protection = st.selectbox(
            "Device Protection",
            ["No", "Yes"]
        )

        tech_support = st.selectbox(
            "Tech Support",
            ["No", "Yes"]
        )

        streaming_tv = st.selectbox(
            "Streaming TV",
            ["No", "Yes"]
        )

        streaming_movies = st.selectbox(
            "Streaming Movies",
            ["No", "Yes"]
        )

        payment_method = st.selectbox(
            "Payment Method",
            [
                "Electronic check",
                "Mailed check",
                "Credit card (automatic)",
                "Bank transfer (automatic)"
            ]
        )

    if st.button("Predict Churn"):

        total_charges = round(
            tenure * monthly_charges,
            2
        )

        avg_charges_per_month = (
            total_charges / tenure
            if tenure > 0 else 0
        )

        if tenure <= 12:
            tenure_group = 0
        elif tenure <= 24:
            tenure_group = 1
        else:
            tenure_group = 2

        total_services = sum([
            online_security == "Yes",
            online_backup == "Yes",
            device_protection == "Yes",
            tech_support == "Yes",
            streaming_tv == "Yes",
            streaming_movies == "Yes",
            phone_service == "Yes"
        ])

        row = dict.fromkeys(
            FEATURE_COLUMNS,
            0
        )

        row["gender"] = 1 if gender == "Male" else 0
        row["SeniorCitizen"] = 1 if senior == "Yes" else 0
        row["Partner"] = 1 if partner == "Yes" else 0
        row["Dependents"] = 1 if dependents == "Yes" else 0

        row["tenure"] = tenure
        row["PhoneService"] = 1 if phone_service == "Yes" else 0
        row["PaperlessBilling"] = (
            1 if paperless_billing == "Yes"
            else 0
        )

        row["MonthlyCharges"] = monthly_charges
        row["TotalCharges"] = total_charges

        if phone_service == "No":
            row["MultipleLines_No phone service"] = 1

        if multiple_lines == "Yes":
            row["MultipleLines_Yes"] = 1

        if internet_service == "Fiber optic":
            row["InternetService_Fiber optic"] = 1

        if internet_service == "No":
            row["InternetService_No"] = 1

        if online_security == "Yes":
            row["OnlineSecurity_Yes"] = 1

        if online_backup == "Yes":
            row["OnlineBackup_Yes"] = 1

        if device_protection == "Yes":
            row["DeviceProtection_Yes"] = 1

        if tech_support == "Yes":
            row["TechSupport_Yes"] = 1

        if streaming_tv == "Yes":
            row["StreamingTV_Yes"] = 1

        if streaming_movies == "Yes":
            row["StreamingMovies_Yes"] = 1

        if contract == "One year":
            row["Contract_One year"] = 1

        if contract == "Two year":
            row["Contract_Two year"] = 1

        if payment_method == "Credit card (automatic)":
            row["PaymentMethod_Credit card (automatic)"] = 1

        elif payment_method == "Electronic check":
            row["PaymentMethod_Electronic check"] = 1

        elif payment_method == "Mailed check":
            row["PaymentMethod_Mailed check"] = 1

        row["tenure_group"] = tenure_group
        row["avg_charges_per_month"] = avg_charges_per_month
        row["total_services"] = total_services

        input_df = pd.DataFrame(
            [row]
        )

        scaled_input = scaler.transform(
            input_df
        )

        probability = model.predict_proba(
            scaled_input
        )[0][1]

        if probability < 0.30:
            risk = "Low Risk"
            recommendation = "Monitor Customer"

        elif probability < 0.60:
            risk = "Medium Risk"
            recommendation = "Offer Personalized Support"

        else:
            risk = "High Risk"
            recommendation = "Priority Retention Campaign"

        st.markdown("---")

        colA, colB, colC = st.columns(3)

        with colA:
            st.metric(
                "Churn Probability",
                f"{probability:.2%}"
            )

        with colB:
            st.metric(
                "Risk Segment",
                risk
            )

        with colC:
            st.metric(
                "Recommendation",
                recommendation
            )

# =========================
# INSIGHTS PAGE
# =========================

elif page == "📊 Business Insights":

    st.title("📊 Business Insights")

    image_files = [

        "images/model-performance-comparison.png",

        "images/all-model-comparison-plot.png",

        "images/baseline-vs-tuned-comparison-plot.png",

        "images/classification-report-logistic-regression.png",

        "images/classification_report_random_forest.png"

    ]

    captions = {

        "images/model-performance-comparison.png":
            "Baseline Model Performance",

        "images/all-model-comparison-plot.png":
            "Comparison of All Models",

        "images/baseline-vs-tuned-comparison-plot.png":
            "Baseline vs Tuned Models",

        "images/classification-report-logistic-regression.png":
            "Logistic Regression Classification Report",

        "images/classification_report_random_forest.png":
            "Random Forest Classification Report"
    }

    for img_path in image_files:

        if os.path.exists(img_path):

            st.image(
                img_path,
                caption=captions.get(
                    img_path,
                    ""
                ),
                use_container_width=True
            )

# =========================
# ABOUT PAGE
# =========================

elif page == "ℹ️ About":

    st.title("ℹ️ About")

    st.markdown("""
    ### Author

    Kaustubh Mukdam

    ---

    ### Project

    Customer Churn Prediction and Retention Analysis

    ---

    ### Technologies

    - Python
    - Pandas
    - NumPy
    - Scikit-Learn
    - SHAP
    - Streamlit

    ---

    ### Model

    - Logistic Regression
    - ROC-AUC: 0.84
    - Cross Validation ROC-AUC: 0.849 ± 0.019

    ---

    ### Dataset

    IBM Telco Customer Churn Dataset

    ---

    ### Links

    GitHub:
    https://github.com/KaustubhMukdam/customer-churn-prediction
    """
    )