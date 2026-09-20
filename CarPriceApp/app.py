import os
import joblib
import warnings

import numpy as np
import pandas as pd
import streamlit as st

from PIL import Image

warnings.filterwarnings("ignore")


# =============================================================================
# PAGE CONFIG
# =============================================================================

st.set_page_config(
    page_title="Car Price Prediction",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =============================================================================
# CUSTOM CSS
# =============================================================================

st.markdown("""
<style>

.main {
    background-color: #f5f7fa;
}

h1, h2, h3 {
    color: #1F4E79;
}

.stButton>button {
    width: 100%;
    background-color: #1F77B4;
    color: white;
    border-radius: 8px;
    height: 3em;
    font-size: 16px;
}

.stButton>button:hover {
    background-color: #145A86;
}

.prediction-box {
    background-color: #DFF6DD;
    padding: 20px;
    border-radius: 10px;
    font-size: 24px;
    color: green;
    text-align: center;
    font-weight: bold;
}

.footer {
    text-align: center;
    color: gray;
    font-size: 14px;
    margin-top: 30px;
}

</style>
""", unsafe_allow_html=True)


# =============================================================================
# LOAD MODEL
# =============================================================================

# app.py is inside:
# CraPricePred/CarPriceApp/
#
# Model is inside:
# CraPricePred/Model/
#
# Therefore we go one folder up from CarPriceApp,
# then enter Model.

# =============================================================================
# LOAD MODEL
# =============================================================================

MODEL_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "Model",
    "Car_Price_Prediction_Model.pkl"
)

model = None

try:
    model = joblib.load(MODEL_PATH)

except Exception as e:
    st.error(f"Model could not be loaded: {e}")
    st.stop()
# =============================================================================
# SIDEBAR
# =============================================================================

st.sidebar.title("🚗 Navigation")

page = st.sidebar.radio(
    "Go To",
    [
        "Home",
        "Prediction",
        "About Project"
    ]
)

st.sidebar.markdown("---")

st.sidebar.info(
    """
    **Car Price Prediction**

    Predict the resale value of a used car
    using Machine Learning.

    Developed using:

    - Python
    - Streamlit
    - Scikit-Learn
    """
)


# =============================================================================
# HOME PAGE
# =============================================================================

if page == "Home":

    st.title("🚗 Car Price Prediction System")

    st.write("### Predict the resale value of a used car instantly.")

    st.write(
        """
        This application uses a trained Machine Learning model to estimate the
        resale price of a used car based on various specifications provided
        by the user.

        ### Features

        - Predict used car prices instantly
        - User-friendly interface
        - Trained Machine Learning model
        - Real-time prediction

        ### Required Inputs

        - Car Brand
        - Car Model
        - Manufacturing Year
        - Fuel Type
        - Seller Type
        - Transmission
        - Ownership
        - Kilometers Driven
        - Mileage
        - Engine Capacity
        - Max Power
        - Seats
        """
    )

    st.markdown("---")

    st.subheader("How It Works")

    st.write(
        """
        1. Navigate to the Prediction page.
        2. Enter all vehicle details.
        3. Click **Predict Price**.
        4. The trained model estimates the resale price.
        """
    )

    st.markdown("---")

    st.success("Select **Prediction** from the left sidebar to get started.")


# =============================================================================
# PREDICTION PAGE
# =============================================================================

elif page == "Prediction":

    st.title("🚘 Used Car Price Prediction")

    st.write("Fill all the details below.")

    col1, col2 = st.columns(2)

    with col1:

        brand = st.text_input(
            "Brand",
            placeholder="Example: Maruti"
        )

        model_name = st.text_input(
            "Model",
            placeholder="Example: Swift"
        )

        year = st.number_input(
            "Manufacturing Year",
            min_value=1990,
            max_value=2030,
            value=2018
        )

        fuel = st.selectbox(
            "Fuel Type",
            [
                "Petrol",
                "Diesel",
                "CNG",
                "LPG",
                "Electric"
            ]
        )

        seller_type = st.selectbox(
            "Seller Type",
            [
                "Dealer",
                "Individual",
                "Trustmark Dealer"
            ]
        )

        transmission = st.selectbox(
            "Transmission",
            [
                "Manual",
                "Automatic"
            ]
        )

    with col2:

        owner = st.selectbox(
            "Owner",
            [
                "First Owner",
                "Second Owner",
                "Third Owner",
                "Fourth & Above Owner",
                "Test Drive Car"
            ]
        )

        km_driven = st.number_input(
            "Kilometers Driven",
            min_value=0,
            value=50000
        )

        mileage = st.number_input(
            "Mileage (km/l)",
            min_value=0.0,
            value=18.5,
            step=0.1,
            format="%.1f"
        )

        engine = st.number_input(
            "Engine (CC)",
            min_value=500,
            max_value=6000,
            value=1197
        )

        max_power = st.number_input(
            "Max Power (bhp)",
            min_value=10.0,
            max_value=1000.0,
            value=82.0,
            step=0.1,
            format="%.1f"
        )

        seats = st.selectbox(
            "Seats",
            [2, 4, 5, 6, 7, 8, 9, 10]
        )

    st.markdown("---")

    if st.button("Predict Price"):

        input_df = pd.DataFrame({
            "name": [brand + " " + model_name],
            "year": [year],
            "km_driven": [km_driven],
            "fuel": [fuel],
            "seller_type": [seller_type],
            "transmission": [transmission],
            "owner": [owner],
            "mileage": [float(mileage)],
            "engine": [int(engine)],
            "max_power": [float(max_power)],
            "seats": [int(seats)]
        })

        try:

            # The saved model is already a complete Pipeline.
            # Therefore, no separate preprocessor is required.

            prediction = model.predict(input_df)[0]

            prediction = max(0, prediction)

            st.markdown(
                f"""
                <div class="prediction-box">
                    Estimated Car Price<br><br>
                    ₹ {prediction:,.2f}
                </div>
                """,
                unsafe_allow_html=True
            )

        except Exception as e:

            st.error("Prediction failed.")

            st.exception(e)


# =============================================================================
# ABOUT PAGE
# =============================================================================

elif page == "About Project":

    st.title("📘 About This Project")

    st.write(
        """
        ### Project Overview

        This Machine Learning application predicts the selling price of
        used cars based on vehicle specifications entered by the user.

        The model has been trained using historical used-car data and
        performs preprocessing before making predictions.
        """
    )

    st.markdown("---")

    st.subheader("Technologies Used")

    st.markdown(
        """
        - Python
        - Streamlit
        - Pandas
        - NumPy
        - Scikit-Learn
        - Pickle
        """
    )

    st.markdown("---")

    st.subheader("Model Inputs")

    st.markdown(
        """
        - Brand & Model
        - Manufacturing Year
        - Fuel Type
        - Seller Type
        - Transmission
        - Owner Type
        - Kilometers Driven
        - Mileage
        - Engine Capacity
        - Maximum Power
        - Number of Seats
        """
    )

    st.markdown("---")

    st.subheader("Model Output")

    st.write(
        """
        The model predicts the estimated resale price of the vehicle
        in Indian Rupees (₹). The prediction is generated instantly
        after processing the entered vehicle specifications.
        """
    )

    st.markdown("---")

    st.subheader("Machine Learning Workflow")

    st.markdown(
        """
        1. User enters car details.
        2. Input data is converted into a DataFrame.
        3. Data preprocessing is applied by the trained model pipeline.
        4. The processed features are passed to the trained ML model.
        5. The model predicts the estimated selling price.
        6. The predicted price is displayed on the screen.
        """
    )

    st.markdown("---")

    st.subheader("Important Notes")

    st.info(
        """
        • Predictions are estimates and may differ from actual market prices.

        • Prediction accuracy depends on the quality of the training dataset.

        • This application is intended for educational and demonstration purposes.
        """
    )

    st.markdown("---")

    st.subheader("Future Improvements")

    st.markdown(
        """
        - Upload car images for price estimation.
        - Integration with live market pricing APIs.
        - Price trend visualization.
        - Advanced feature engineering.
        - Model comparison (Random Forest, XGBoost, CatBoost).
        - Vehicle condition score input.
        - Location-based pricing.
        - Dark mode support.
        """
    )


# =============================================================================
# FOOTER
# =============================================================================

st.markdown("---")

st.markdown(
    """
    <div class="footer">
        🚗 Car Price Prediction System<br>
        Developed using Streamlit & Machine Learning
    </div>
    """,
    unsafe_allow_html=True,
)


# =============================================================================
# MODEL LOADING STATUS
# =============================================================================

if model is None:

    st.error("System not ready. Model missing.")

else:

    st.success("System Loaded Successfully 🚗 Ready for Prediction")