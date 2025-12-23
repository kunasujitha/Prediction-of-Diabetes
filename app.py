import streamlit as st
import numpy as np
import joblib
import pandas as pd

# Load model and scaler
model = joblib.load("diabetes_model.pkl")
scaler = joblib.load("scaler.pkl")

st.set_page_config(page_title="Diabetes Prediction App", layout="centered")

# Title
st.title("🩺 Diabetes Prediction App")
st.write("Enter patient details to predict diabetes risk")

# Sidebar inputs
st.sidebar.header("Patient Input Features")

def user_input():
    pregnancies = st.sidebar.number_input("Pregnancies", 0, 20, 1)
    glucose = st.sidebar.number_input("Glucose (mg/dL)", 0, 300, 120)
    blood_pressure = st.sidebar.number_input("Blood Pressure (mm Hg)", 0, 200, 70)
    skin_thickness = st.sidebar.number_input("Skin Thickness (mm)", 0, 100, 20)
    insulin = st.sidebar.number_input("Insulin (µU/mL)", 0, 900, 80)
    bmi = st.sidebar.number_input("BMI (kg/m²)", 0.0, 70.0, 25.0)
    dpf = st.sidebar.number_input("Diabetes Pedigree Function", 0.0, 3.0, 0.5)
    age = st.sidebar.number_input("Age (years)", 1, 120, 33)
    

    return np.array([[pregnancies, glucose, blood_pressure,
                      skin_thickness, insulin, bmi, dpf, age]])
    
input_data = user_input()


#Scale input (same columns used during training)


feature_names = [
    "Pregnancies",
    "Glucose",
    "BloodPressure",
    "SkinThickness",
    "Insulin",
    "BMI",
    "DiabetesPedigreeFunction",
    "Age"
]

input_data = pd.DataFrame(input_data,columns = feature_names)


scaled_cols = ["Glucose",
    "BloodPressure",
    "SkinThickness",
    "Insulin",
    "BMI",
    "DiabetesPedigreeFunction",
    "Age"]
input_data[scaled_cols] = scaler.transform(input_data[scaled_cols])
print(input_data)

# Prediction
if st.button("🔍 Predict Diabetes"):
    prediction = model.predict(input_data)
    prob = model.predict_proba(input_data)

    if prediction[0] == 1:
        st.error(f"⚠️ Diabetic Risk Detected\n\nProbability: {prob[0][1]:.2f}")
    else:
        st.success(f"✅ No Diabetes Detected\n\nProbability: {prob[0][0]:.2f}")
