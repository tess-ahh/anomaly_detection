import streamlit as st
import numpy as np
import joblib

# Load trained model and scaler
model = joblib.load("best_model.pkl")
scaler = joblib.load("scaler.pkl")

# Page title
st.title("🚨 Credit Card Fraud Detection System")

st.write(
    "Enter transaction details below to predict whether "
    "the transaction is fraudulent or normal."
)

# Input fields
time = st.number_input("Time", value=0.0)

features = []

# V1 to V28 inputs
for i in range(1, 29):

    value = st.number_input(
        f"V{i}",
        value=0.0
    )

    features.append(value)

# Amount input
amount = st.number_input(
    "Amount",
    value=0.0
)

# Predict button
if st.button("Predict Transaction"):

    # Combine all inputs
    input_data = [[
        time,
        *features,
        amount
    ]]

    # Scale input
    input_scaled = scaler.transform(input_data)

    # Predict
    prediction = model.predict(input_scaled)

    # Display result
    if prediction[0] == 1:

        st.error(
            "⚠️ Fraudulent Transaction Detected"
        )

    else:

        st.success(
            "✅ Normal Transaction"
        )