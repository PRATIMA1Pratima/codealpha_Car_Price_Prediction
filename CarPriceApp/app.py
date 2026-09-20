import os
import warnings

import joblib
import numpy as np
import pandas as pd
import streamlit as st

from datetime import datetime

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

st.markdown(
    """
    <style>

    .main {
        background-color: #f5f7fa;
    }

    h1, h2, h3 {
        color: #1F4E79;
    }

    .stButton > button {
        width: 100%;
        background-color: #1F77B4;
        color: white;
        border-radius: 8px;
        height: 3em;
        font-size: 16px;
    }

    .stButton > button:hover {
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
    """,
    unsafe_allow_html=True
)


# =============================================================================
# LOAD MODEL
# =============================================================================

# app.py is inside:
# CraPricePred/CarPriceApp/
#
# Model is inside:
# CraPricePred/Model/

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "Model",
    "Car_Price_Prediction_Model.pkl"
)

model = None

try:
    model = joblib.load(MODEL_PATH)

except Exception as e:
    st.error("Model could not be loaded.")
    st.exception(e)
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
    - Pandas
    - Scikit-Learn
    - Streamlit
    - Random Forest
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
        This application uses a trained Machine Learning model to estimate
        the resale price of a used car based on various specifications
        provided by the user.
        """
    )

    st.markdown("---")

    st.subheader("Features")

    st.markdown(
        """
        - Predict used car prices instantly
        - User-friendly interface
        - Machine Learning based prediction
        - Real-time prediction
        - Random Forest based model
        """
    )

    st.markdown("---")

    st.subheader("Required Inputs")

    st.markdown(
        """
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
        - Maximum Power
        - Torque
        - Number of Seats
        """
    )

    st.markdown("---")

    st.subheader("How It Works")

    st.write(
        """
        1. Navigate to the Prediction page.
        2. Enter the vehicle details.
        3. Click **Predict Price**.
        4. The input data is converted into the feature format
           expected by the trained model.
        5. The trained Random Forest model predicts the resale value.
        """
    )

    st.markdown("---")

    st.success(
        "Select **Prediction** from the left sidebar to get started."
    )


# =============================================================================
# PREDICTION PAGE
# =============================================================================

elif page == "Prediction":

    st.title("🚘 Used Car Price Prediction")

    st.write("Fill in the vehicle details below.")

    col1, col2 = st.columns(2)

    # -------------------------------------------------------------------------
    # LEFT COLUMN
    # -------------------------------------------------------------------------

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
            max_value=datetime.now().year,
            value=2018,
            step=1
        )

        fuel = st.selectbox(
            "Fuel Type",
            [
                "Petrol",
                "Diesel",
                "LPG",
                "CNG",
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

    # -------------------------------------------------------------------------
    # RIGHT COLUMN
    # -------------------------------------------------------------------------

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
            value=50000,
            step=1000
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
            value=1197,
            step=1
        )

        max_power = st.number_input(
            "Max Power (bhp)",
            min_value=10.0,
            max_value=1000.0,
            value=82.0,
            step=0.1,
            format="%.1f"
        )

        torque = st.number_input(
            "Torque (Nm)",
            min_value=0.0,
            max_value=2000.0,
            value=113.0,
            step=1.0,
            format="%.1f"
        )

        seats = st.selectbox(
            "Seats",
            [2, 4, 5, 6, 7, 8, 9, 10],
            index=2
        )


    # -------------------------------------------------------------------------
    # PREDICT BUTTON
    # -------------------------------------------------------------------------

    st.markdown("---")

    if st.button("Predict Price"):

        try:

            # -------------------------------------------------------------
            # BASIC VALIDATION
            # -------------------------------------------------------------

            if not brand.strip():

                st.warning("Please enter the car brand.")

                st.stop()

            if not model_name.strip():

                st.warning("Please enter the car model.")

                st.stop()


            # -------------------------------------------------------------
            # CALCULATE CAR AGE
            # -------------------------------------------------------------

            current_year = datetime.now().year

            car_age = current_year - int(year)

            if car_age < 0:
                car_age = 0


            # -------------------------------------------------------------
            # CREATE RAW INPUT DATA
            # -------------------------------------------------------------

            input_df = pd.DataFrame(
                {
                    "year": [int(year)],
                    "km_driven": [int(km_driven)],
                    "mileage": [float(mileage)],
                    "engine": [int(engine)],
                    "max_power": [float(max_power)],
                    "torque": [float(torque)],
                    "seats": [int(seats)],
                    "Car_Age": [int(car_age)],
                    "fuel": [fuel],
                    "seller_type": [seller_type],
                    "transmission": [transmission],
                    "owner": [owner],
                    "Brand": [brand.strip()]
                }
            )


            # -------------------------------------------------------------
            # ONE-HOT ENCODE CATEGORICAL FEATURES
            # -------------------------------------------------------------

            categorical_columns = [
                "fuel",
                "seller_type",
                "transmission",
                "owner",
                "Brand"
            ]

            encoded_df = pd.get_dummies(
                input_df,
                columns=categorical_columns,
                drop_first=False
            )


            # -------------------------------------------------------------
            # GET EXACT FEATURES EXPECTED BY SAVED MODEL
            # -------------------------------------------------------------

            expected_columns = list(model.feature_names_in_)


            # -------------------------------------------------------------
            # ADD MISSING COLUMNS
            #
            # Example:
            # If the user selects Petrol, the dataframe will contain
            # fuel_Petrol but may not contain fuel_Diesel or fuel_LPG.
            #
            # The trained model expects all of them, so missing columns
            # are added with value 0.
            # -------------------------------------------------------------

            for column in expected_columns:

                if column not in encoded_df.columns:

                    encoded_df[column] = 0


            # -------------------------------------------------------------
            # REMOVE UNEXPECTED COLUMNS
            # -------------------------------------------------------------

            encoded_df = encoded_df[expected_columns]


            # -------------------------------------------------------------
            # CONVERT EVERYTHING TO NUMERIC
            # -------------------------------------------------------------

            encoded_df = encoded_df.apply(
                pd.to_numeric,
                errors="coerce"
            )

            encoded_df = encoded_df.fillna(0)


            # -------------------------------------------------------------
            # MAKE PREDICTION
            # -------------------------------------------------------------

            prediction = model.predict(encoded_df)[0]


            # Prevent negative predicted price
            prediction = max(0, float(prediction))


            # -------------------------------------------------------------
            # DISPLAY RESULT
            # -------------------------------------------------------------

            st.markdown(
                f"""
                <div class="prediction-box">
                    Estimated Car Price
                    <br><br>
                    ₹ {prediction:,.2f}
                </div>
                """,
                unsafe_allow_html=True
            )


            st.success(
                "Prediction generated successfully! 🚗"
            )


            # -------------------------------------------------------------
            # SHOW INPUT SUMMARY
            # -------------------------------------------------------------

            with st.expander("View Input Details"):

                display_df = pd.DataFrame(
                    {
                        "Feature": [
                            "Brand",
                            "Model",
                            "Manufacturing Year",
                            "Car Age",
                            "Fuel Type",
                            "Seller Type",
                            "Transmission",
                            "Owner",
                            "Kilometers Driven",
                            "Mileage",
                            "Engine",
                            "Max Power",
                            "Torque",
                            "Seats"
                        ],

                        "Value": [
                            brand,
                            model_name,
                            year,
                            car_age,
                            fuel,
                            seller_type,
                            transmission,
                            owner,
                            km_driven,
                            mileage,
                            engine,
                            max_power,
                            torque,
                            seats
                        ]
                    }
                )

                st.dataframe(
                    display_df,
                    use_container_width=True,
                    hide_index=True
                )


        except Exception as e:

            st.error("Prediction failed.")

            st.exception(e)


# =============================================================================
# ABOUT PROJECT PAGE
# =============================================================================

elif page == "About Project":

    st.title("📘 About This Project")

    st.write(
        """
        ### Project Overview

        This Machine Learning application predicts the selling price of
        used cars based on vehicle specifications entered by the user.

        The model has been trained using historical used-car data and
        uses preprocessing and Random Forest regression to estimate
        the vehicle's resale price.
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
        - Joblib
        - Random Forest Regressor
        """
    )

    st.markdown("---")

    st.subheader("Model Inputs")

    st.markdown(
        """
        - Brand
        - Car Model
        - Manufacturing Year
        - Fuel Type
        - Seller Type
        - Transmission
        - Owner Type
        - Kilometers Driven
        - Mileage
        - Engine Capacity
        - Maximum Power
        - Torque
        - Number of Seats
        """
    )

    st.markdown("---")

    st.subheader("Model Output")

    st.write(
        """
        The model predicts the estimated resale price of the vehicle
        in Indian Rupees (₹).

        The prediction is generated after processing the vehicle
        specifications and converting categorical information into
        the feature structure expected by the trained model.
        """
    )

    st.markdown("---")

    st.subheader("Machine Learning Workflow")

    st.markdown(
        """
        1. User enters car details.
        2. Input data is converted into a Pandas DataFrame.
        3. Car age is calculated from the manufacturing year.
        4. Categorical features are one-hot encoded.
        5. Missing model features are added with zero values.
        6. Features are arranged according to the trained model.
        7. Random Forest predicts the estimated car price.
        8. The predicted price is displayed to the user.
        """
    )

    st.markdown("---")

    st.subheader("Important Notes")

    st.info(
        """
        • Predictions are estimates and may differ from actual market prices.

        • Prediction accuracy depends on the quality of the training dataset.

        • The application is intended for educational and demonstration purposes.
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
        - Model comparison with XGBoost and CatBoost.
        - Vehicle condition score.
        - Location-based pricing.
        - Improved UI and dark mode.
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
    unsafe_allow_html=True
)


# =============================================================================
# END OF APP
# =============================================================================