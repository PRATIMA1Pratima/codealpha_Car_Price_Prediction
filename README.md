# 🚗 Car Price Prediction using Machine Learning

## 📌 Project Overview

This project predicts the selling price of a used car based on various features such as present price, kilometers driven, fuel type, transmission, seller type, owner, and car age. The model is built using Machine Learning techniques in Python and deployed as an interactive web application using Streamlit.

This project was developed as part of the **CodeAlpha Data Science Internship**.

---

## 🎯 Objectives

- Predict the selling price of a used car.
- Perform data preprocessing and feature engineering.
- Train and evaluate multiple regression models.
- Compare model performance using evaluation metrics.
- Deploy the best-performing model using Streamlit.

---

## 📂 Dataset

The dataset contains information about used cars with the following features:

- Car_Name
- Year
- Present_Price
- Selling_Price (Target Variable)
- Driven_kms
- Fuel_Type
- Selling_type
- Transmission
- Owner

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Pickle
- Streamlit
- Jupyter Notebook

---

## 📊 Machine Learning Workflow

1. Import libraries
2. Load dataset
3. Data exploration
4. Data cleaning
5. Exploratory Data Analysis (EDA)
6. Feature Engineering
7. One-Hot Encoding
8. Train-Test Split
9. Model Training
10. Model Evaluation
11. Feature Importance Analysis
12. Save the trained model
13. Build Streamlit Web App

---

## 🤖 Models Used

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor

The **Random Forest Regressor** was selected as the final model because it achieved the best prediction performance.

---

## 📈 Evaluation Metrics

The model was evaluated using:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

---

## 🚀 Streamlit Web Application

The application allows users to enter:

- Present Price
- Kilometers Driven
- Number of Owners
- Car Age
- Fuel Type
- Seller Type
- Transmission

The application then predicts the estimated selling price of the car.

---

## 📁 Project Structure

```
Car_Price_Prediction/
│
├── app.py
├── car_price_model.pkl
├── Car Price Prediction.ipynb
├── car data.csv
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/your-username/Car-Price-Prediction.git
```

Move into the project directory

```bash
cd Car-Price-Prediction
```

Install the required libraries

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run app.py
```

---

## 📸 Project Screenshots

You can add screenshots here after running the Streamlit application.

Example:

- Home Page
- Prediction Result
- Feature Importance Graph

---

## 📌 Future Improvements

- Include more car features such as mileage, engine capacity, horsepower, and brand.
- Hyperparameter tuning for improved accuracy.
- Deploy the application on Streamlit Community Cloud.
- Add visual dashboards for better user experience.
- Integrate with real-time used car datasets.

---

## 🎓 Learning Outcomes

Through this project, I learned:

- Data preprocessing
- Feature engineering
- One-Hot Encoding
- Regression algorithms
- Model evaluation
- Model serialization using Pickle
- Building interactive applications using Streamlit
- GitHub project management

---

## 👩‍💻 Author

**Pratima**

B.Tech Computer Science Engineering (AI & Machine Learning)

Aspiring Data Scientist | Machine Learning Enthusiast

---

## 📄 License

This project is created for educational purposes as part of the Data Science Internship.