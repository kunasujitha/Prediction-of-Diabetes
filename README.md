# 🩺 Diabetes Prediction App

An end-to-end machine learning project that predicts the likelihood of diabetes based on patient health parameters.  
The project includes data preprocessing, class imbalance handling, model training, and a Streamlit web application for real-time predictions.

---

## 🚀 Features

- Data preprocessing and cleaning
- Handling class imbalance using SMOTE
- Feature scaling with StandardScaler
- Machine learning model training (XGBClassifier)
- Streamlit-based web application for predictions
- Displays diabetes risk probability

---

## 🧠 Machine Learning Workflow

1. Data Loading (PIMA Indians Diabetes Dataset)
2. Handling missing values
3. Outlier detection and removal
4. Feature scaling
5. Train-test split
6. Class imbalance handling using SMOTE
7. Model training and evaluation
8. Model deployment using Streamlit

---

## 📊 Input Features

| Feature | Description | Unit |
|------|------------|------|
| Pregnancies | Number of pregnancies | Count |
| Glucose | Plasma glucose concentration | mg/dL |
| BloodPressure | Diastolic blood pressure | mm Hg |
| SkinThickness | Triceps skin fold thickness | mm |
| Insulin | 2-hour serum insulin | µU/mL |
| BMI | Body Mass Index | kg/m² |
| DiabetesPedigreeFunction | Genetic risk factor | Unitless |
| Age | Age of the patient | Years |

---

## 🖥️ Web Application

The Streamlit app allows users to:
- Enter patient health details
- Predict whether the patient is diabetic or not
- View the probability of diabetes risk

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Imbalanced-learn (SMOTE)
- Streamlit
- Joblib

---

## ▶️ How to Run the Project Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/diabetes-prediction.git
cd diabetes-prediction
