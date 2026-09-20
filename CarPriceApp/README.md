# 🚗 Car Price Prediction using Machine Learning

A professional Machine Learning project that predicts the selling price of used cars based on various features such as brand, fuel type, transmission, engine capacity, mileage, ownership, and more. The project includes data preprocessing, exploratory data analysis (EDA), feature engineering, model training, hyperparameter tuning, and deployment using Streamlit.

---

## 📌 Project Overview

The objective of this project is to build an accurate machine learning model capable of predicting the resale value of used cars. Multiple regression algorithms were trained and evaluated, and the best-performing model was optimized using Randomized Search CV.

---

## 🎯 Objectives

- Predict the selling price of a used car.
- Perform data cleaning and preprocessing.
- Conduct Exploratory Data Analysis (EDA).
- Compare multiple regression models.
- Optimize the best model using hyperparameter tuning.
- Deploy the trained model using Streamlit.

---

## 📂 Project Structure

```
CarPricePrediction/
│
├── app.py
├── style.css
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   ├── car_data.csv
│   └── cleaned_car_data.csv
│
├── models/
│   └── car_price_prediction_model.pkl
│
├── notebooks/
│   └── Car_Price_Prediction.ipynb
│
├── images/
│
└── screenshots/
```

---

## 📊 Dataset Information

The dataset contains information about used cars with the following features:

- Brand
- Year
- Selling Price (Target Variable)
- Kilometers Driven
- Fuel Type
- Seller Type
- Transmission
- Owner
- Mileage
- Engine Capacity
- Maximum Power
- Torque
- Number of Seats

---

## 🛠️ Data Preprocessing

The following preprocessing steps were performed:

- Removed duplicate records
- Handled missing values
- Converted text columns into numerical values
- Extracted Brand from Car Name
- Converted Mileage to float
- Converted Engine to integer
- Converted Max Power to float
- Converted Torque to numerical format
- Created Car Age feature
- Feature Engineering
- One-Hot Encoding using ColumnTransformer
- Pipeline implementation

---

## 📈 Exploratory Data Analysis (EDA)

Performed various visualizations including:

- Selling Price Distribution
- Fuel Type Distribution
- Transmission Analysis
- Seller Type Analysis
- Owner Analysis
- Correlation Heatmap
- Brand-wise Price Comparison
- Mileage vs Selling Price
- Engine vs Selling Price
- Year vs Selling Price

---

## 🤖 Machine Learning Models Used

The following regression algorithms were trained and compared:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor

---

## ⚙️ Hyperparameter Tuning

Random Forest Regressor was optimized using **RandomizedSearchCV**.

Best Parameters:

```
{
'model__n_estimators':100,
'model__min_samples_split':5,
'model__min_samples_leaf':1,
'model__max_depth':20
}
```

---

## 📊 Model Performance

| Metric | Value |
|---------|--------|
| R² Score | **93.19%** |
| MAE | 70,774 |
| RMSE | 122,190 |

Random Forest Regressor achieved the highest accuracy among all models.

---

## 📌 Feature Importance

The trained model identified the following features as highly influential:

- Car Age
- Engine Capacity
- Maximum Power
- Mileage
- Brand
- Fuel Type
- Owner
- Transmission

---

## 🚀 Streamlit Web Application

The project includes an interactive Streamlit application where users can:

- Select Car Brand
- Select Fuel Type
- Select Seller Type
- Select Transmission
- Select Owner
- Enter Mileage
- Enter Engine Capacity
- Enter Maximum Power
- Enter Torque
- Enter Number of Seats
- Enter Car Age
- Predict the Estimated Selling Price

---

## 💻 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Scikit-learn
- Joblib
- Streamlit

---

## 📦 Python Libraries

```
pandas
numpy
matplotlib
seaborn
plotly
streamlit
scikit-learn
joblib
```

---

## ▶️ How to Run the Project

### Clone Repository

```bash
git clone <repository-link>
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Streamlit

```bash
streamlit run app.py
```

---

## 📸 Project Screenshots

Add screenshots of the following pages after deployment:

- Home Page
- Prediction Page
- Dataset Overview
- Model Performance
- Feature Importance

---

## 📈 Future Enhancements

- XGBoost Model
- LightGBM Integration
- CatBoost Model
- Deep Learning Model
- Vehicle Image Upload
- Cloud Deployment
- User Authentication
- Price Trend Analysis
- Recommendation System

---

## 💡 Business Applications

- Used Car Dealerships
- Automobile Market Analysis
- Online Car Selling Platforms
- Vehicle Valuation Systems
- Insurance Companies
- Financial Institutions

---

## 📚 Learning Outcomes

Through this project, the following concepts were learned:

- Data Cleaning
- Data Preprocessing
- Feature Engineering
- Exploratory Data Analysis
- Regression Algorithms
- Hyperparameter Tuning
- Machine Learning Pipelines
- Model Evaluation
- Feature Importance
- Model Deployment using Streamlit

---

## 👩‍💻 Developed By

**Pratima**

B.Tech Computer Science Engineering (AI & Machine Learning)

Sandip University

Machine Learning | Data Science | Artificial Intelligence

---

## ⭐ If you found this project helpful, please consider giving it a Star on GitHub.
