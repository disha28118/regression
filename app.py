# app.py – House Price Prediction App (USD Only)

import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("model/house_price_model.pkl")

# Page configuration
st.set_page_config(page_title="🏠 House Price Estimator", page_icon="💰", layout="centered")

# Custom CSS Styling
st.markdown("""
    <style>
        body {
            background-color: #f8f9fa;
        }
        .main-container {
            background-color: #ffffff;
            padding: 2rem 3rem;
            border-radius: 15px;
            box-shadow: 0px 4px 20px rgba(0,0,0,0.1);
        }
        h1, h3 {
            text-align: center;
            color: #2c3e50;
        }
        .footer {
            margin-top: 40px;
            text-align: center;
            font-size: 13px;
            color: #888;
        }
        .result-box {
            background-color: #dff0d8;
            color: #3c763d;
            padding: 1rem;
            border-radius: 10px;
            margin-top: 20px;
            text-align: center;
            font-size: 20px;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# Title Section
st.markdown("<div class='main-container'>", unsafe_allow_html=True)
st.markdown("<h1>🏡 House Price Predictor</h1>", unsafe_allow_html=True)
st.markdown("### Enter the property details to estimate its price (in USD):")

# Input Fields
col1, col2 = st.columns(2)

with col1:
    bedrooms = st.slider("🛏️ Number of Bedrooms", 1, 10, 3)
    area = st.number_input("📐 Area (in square feet)", min_value=300, max_value=10000, value=1800)

with col2:
    bathrooms = st.slider("🛁 Number of Bathrooms", 1, 10, 2)
    age = st.slider("🏗️ Age of the House (in years)", 0, 100, 20)

# Prediction Logic
if st.button("🔮 Predict House Price"):
    features = np.array([[bedrooms, bathrooms, area, age]])

    try:
        prediction = model.predict(features)[0]

        # Ensure non-negative and realistic value
        prediction_usd = max(10000, prediction)  # Floor set to $10,000

        st.markdown(
            f"<div class='result-box'>💰 Estimated Price: <strong>${prediction_usd:,.2f}</strong></div>",
            unsafe_allow_html=True
        )

    except Exception as e:
        st.error(f"Prediction failed: {str(e)}")

# Close container div
st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("<div class='footer'>✨ Designed by Disha Gupta | Streamlit App 2025</div>", unsafe_allow_html=True)
