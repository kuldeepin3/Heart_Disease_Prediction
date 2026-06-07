# run this on terminal python -m streamlit run app.py

import streamlit as st
import pickle
import numpy as np

# Load model and scaler
model = pickle.load(open('heart_disease_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

st.title("Heart Disease Prediction")

patient_id = st.number_input("Patient ID", min_value=1)

age = st.number_input("Age", min_value=1, max_value=120)

gender = st.selectbox("Gender", ["Male", "Female"])

glucose = st.number_input("Glucose (mg/dL)")
cholesterol = st.number_input("Cholesterol (mg/dL)")
systolic_bp = st.number_input("Systolic BP")
diastolic_bp = st.number_input("Diastolic BP")
bmi = st.number_input("BMI")
heart_rate = st.number_input("Heart Rate")

smoking = st.selectbox("Smoking", ["Yes", "No"])
alcohol = st.selectbox("Alcohol Consumption", ["Yes", "No"])
family_history = st.selectbox("Family History", ["Yes", "No"])

activity = st.selectbox(
    "Physical Activity",
    ["High", "Low", "Medium"]
)

if st.button("Predict"):

    # Encode binary features
    gender = 1 if gender == "Male" else 0
    smoking = 1 if smoking == "Yes" else 0
    alcohol = 1 if alcohol == "Yes" else 0
    family_history = 1 if family_history == "Yes" else 0

    # One-hot encoding for physical activity
    physical_high = 1 if activity == "High" else 0
    physical_low = 1 if activity == "Low" else 0
    physical_medium = 1 if activity == "Medium" else 0

    features = np.array([[
        patient_id,
        age,
        gender,
        glucose,
        cholesterol,
        systolic_bp,
        diastolic_bp,
        bmi,
        heart_rate,
        smoking,
        alcohol,
        family_history,
        physical_high,
        physical_low,
        physical_medium
    ]])

    features = scaler.transform(features)

    prediction = model.predict(features)

    if prediction[0] == 1:
        st.error("⚠ Heart Disease Detected")
    else:
        st.success("✅ No Heart Disease Detected")