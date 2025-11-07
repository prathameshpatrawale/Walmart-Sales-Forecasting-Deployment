import streamlit as st
import pandas as pd
import numpy as np
import pickle


# Load model and label encoder

model = pickle.load(open("models/rf_model_light.pkl", "rb"))
le = pickle.load(open("models/le.pkl", "rb"))

st.set_page_config(page_title="Walmart Sales Forecasting", layout="wide")
st.title("📊 Walmart Sales Forecasting App")
st.markdown("Predict weekly sales using the trained Random Forest model.")


# Sidebar inputs

st.sidebar.header("🔧 Input Parameters")

store = st.sidebar.number_input("Store ID", min_value=1, max_value=50, value=1)
dept = st.sidebar.number_input("Department ID", min_value=1, max_value=99, value=1)
is_holiday = st.sidebar.selectbox("Is Holiday?", ["No", "Yes"])
temperature = st.sidebar.number_input("Temperature (°F)", min_value=-10.0, max_value=120.0, value=75.0)
fuel_price = st.sidebar.number_input("Fuel Price ($)", min_value=1.0, max_value=5.0, value=2.5)
cpi = st.sidebar.number_input("CPI", min_value=100.0, max_value=300.0, value=210.0)
unemployment = st.sidebar.number_input("Unemployment Rate (%)", min_value=1.0, max_value=15.0, value=7.5)

# Encode categorical column
is_holiday_encoded = le.transform([is_holiday])[0] if is_holiday in le.classes_ else 0

# Create dataframe for model input
input_data = pd.DataFrame({
    "Store": [store],
    "Dept": [dept],
    "IsHoliday": [is_holiday_encoded],
    "Temperature": [temperature],
    "Fuel_Price": [fuel_price],
    "CPI": [cpi],
    "Unemployment": [unemployment]
})


# Prediction

if st.button("Predict Weekly Sales"):
    prediction = model.predict(input_data)[0]
    st.success(f"🛒 Predicted Weekly Sales: **${prediction:,.2f}**")


# CSV Upload

st.markdown("---")
st.subheader("📤 Upload a CSV File for Batch Prediction")
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Uploaded Data Preview:", df.head())

    # Encode categorical column
    if "IsHoliday" in df.columns:
        df["IsHoliday"] = df["IsHoliday"].apply(lambda x: le.transform([x])[0] if x in le.classes_ else 0)

    preds = model.predict(df)
    df["Predicted_Weekly_Sales"] = preds

    st.write("✅ Predictions:", df.head())
    st.download_button(
        label="📥 Download Predictions as CSV",
        data=df.to_csv(index=False).encode("utf-8"),
        file_name="predicted_sales.csv"
    )
