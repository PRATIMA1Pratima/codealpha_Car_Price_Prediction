import streamlit as st
import pickle
import pandas as pd

# Load trained model
model = pickle.load(open("car_price_model.pkl", "rb"))

st.set_page_config(page_title="Car Price Prediction", page_icon="🚗")

st.title("🚗 Car Price Prediction")
st.write("Enter the car details below to predict its selling price.")

# User Inputs
present_price = st.number_input(
    "Present Price (in Lakhs)",
    min_value=0.0,
    value=5.59,
    step=0.1
)

driven_kms = st.number_input(
    "Kilometers Driven",
    min_value=0,
    value=27000,
    step=1000
)

owner = st.selectbox(
    "Number of Previous Owners",
    [0, 1, 2, 3]
)

car_age = st.number_input(
    "Car Age (Years)",
    min_value=0,
    value=5
)

fuel = st.selectbox(
    "Fuel Type",
    ["Petrol", "Diesel", "CNG"]
)

seller = st.selectbox(
    "Seller Type",
    ["Dealer", "Individual"]
)

transmission = st.selectbox(
    "Transmission",
    ["Manual", "Automatic"]
)

# One-Hot Encoding
fuel_diesel = 1 if fuel == "Diesel" else 0
fuel_petrol = 1 if fuel == "Petrol" else 0

seller_individual = 1 if seller == "Individual" else 0

transmission_manual = 1 if transmission == "Manual" else 0

# Prediction
if st.button("Predict Price"):

    input_data = pd.DataFrame({
        'Present_Price': [present_price],
        'Driven_kms': [driven_kms],
        'Owner': [owner],
        'Car_Age': [car_age],
        'Fuel_Type_Diesel': [fuel_diesel],
        'Fuel_Type_Petrol': [fuel_petrol],
        'Selling_type_Individual': [seller_individual],
        'Transmission_Manual': [transmission_manual]
    })

    prediction = model.predict(input_data)[0]

    st.success(f"Estimated Selling Price: ₹ {prediction:.2f} Lakhs")