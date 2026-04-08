# ==========================================
# STREAMLIT APP FOR DRUG PREDICTION
# ==========================================

import streamlit as st
import pandas as pd
import joblib 

# ------------------------------------------
# LOAD SAVED MODEL AND ENCODERS
# ------------------------------------------
model = joblib.load("model.pkl")
sex_encoder = joblib.load("sex_encoder.pkl")
bp_encoder = joblib.load("bp_encoder.pkl")
chol_encoder = joblib.load("chol_encoder.pkl")
drug_encoder = joblib.load("drug_encoder.pkl")

# ------------------------------------------
# PAGE TITLE
# ------------------------------------------
st.set_page_config(page_title="Drug Prediction App", page_icon="💊", layout="centered")

st.title("💊 Drug Prediction System")
st.write("Enter patient details below to predict the suitable drug.")

st.markdown("---")

# ------------------------------------------
# USER INPUTS
# ------------------------------------------
age = st.number_input("Enter Age", min_value=1, max_value=100, value=30)

sex = st.selectbox("Select Sex", ["F", "M"])

bp = st.selectbox("Select Blood Pressure", ["LOW", "NORMAL", "HIGH"])

cholesterol = st.selectbox("Select Cholesterol Level", ["NORMAL", "HIGH"])

na_to_k = st.number_input("Enter Na_to_K Ratio", min_value=0.0, value=10.0, format="%.2f")

# ------------------------------------------
# FEATURE ENGINEERING
# ------------------------------------------
if age <= 30:
    age_group = 0
elif age <= 50:
    age_group = 1
else:
    age_group = 2

# ------------------------------------------
# PREDICTION BUTTON
# ------------------------------------------
if st.button("Predict Drug"):

    # Encode categorical inputs
    sex_encoded = sex_encoder.transform([sex])[0]
    bp_encoded = bp_encoder.transform([bp])[0]
    chol_encoded = chol_encoder.transform([cholesterol])[0]

    # Create input dataframe
    input_data = pd.DataFrame({
        "Age": [age],
        "Sex": [sex_encoded],
        "BP": [bp_encoded],
        "Cholesterol": [chol_encoded],
        "Na_to_K": [na_to_k],
        "Age_Group": [age_group]
    })

    # Predict
    prediction = model.predict(input_data)

    # Decode output
    predicted_drug = drug_encoder.inverse_transform(prediction)[0]

    # Display result
    st.success(f"Predicted Drug: **{predicted_drug}**")