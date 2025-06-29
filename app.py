import streamlit as st
import numpy as np
import joblib
import pandas as pd

# Load the trained model
model = joblib.load("xgboost_model.pkl")

st.title("🦴 Osteoporosis Risk Prediction App")

st.markdown("Fill out the form below to check your risk.")

# User input form
age = st.slider("Age", 20, 100, 50)
race = st.selectbox("Race/Ethnicity", ["Other", "African American", "Caucasian"])
medical_1 = st.checkbox("Hyperthyroidism")
medical_2 = st.checkbox("Rheumatoid Arthritis")
gender = st.selectbox("Gender", ["Male", "Female"])
menopause = st.checkbox("Postmenopausal?")
family = st.checkbox("Family history of osteoporosis?")
weight = st.selectbox("Body Weight", ["Normal", "Underweight", "Overweight"])
calcium = st.selectbox("Calcium Intake", ["Sufficient", "Low"])
vitamin_d = st.selectbox("Vitamin D Intake", ["Sufficient", "Insufficient"])
activity = st.selectbox("Physical Activity", ["Active", "Sedentary"])
smoking = st.selectbox("Smoking", ["No", "Yes"])
alcohol = st.selectbox("Alcohol Consumption", ["None", "Moderate"])
medications = st.checkbox("On corticosteroid medications?")
fracture = st.checkbox("Any prior fractures?")

# Convert inputs to match model features
input_data = np.array([[
    age,
    1 if race == "African American" else 0,
    1 if race == "Caucasian" else 0,
    int(medical_1),
    int(medical_2),
    1 if gender == "Female" else 0,
    int(menopause),
    int(family),
    1 if weight == "Underweight" else 0,
    1 if calcium == "Low" else 0,
    1 if vitamin_d == "Insufficient" else 0,
    1 if activity == "Sedentary" else 0,
    1 if smoking == "Yes" else 0,
    1 if alcohol == "Moderate" else 0,
    int(medications),
    int(fracture)
]])

# Predict button
if st.button("Predict"):
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.error("⚠️ High risk of osteoporosis")
    else:
        st.success("✅ Low risk of osteoporosis")
