# 💊 Drug Prediction System

A Machine Learning web application built using **Python**, **Scikit-learn**, and **Streamlit** to predict the most suitable drug based on patient medical details.

---

## 📌 Project Overview

This project predicts the appropriate **drug type** for a patient using health-related attributes such as:

- **Age**
- **Sex**
- **Blood Pressure (BP)**
- **Cholesterol Level**
- **Na_to_K Ratio**

The model is trained on the **Drug200 dataset** and deployed using **Streamlit** for an interactive web interface.

---

## 🎯 Objective

The main objective of this project is to:

- Apply **machine learning classification**
- Build a predictive model using patient data
- Create a user-friendly **web app**
- Demonstrate a complete ML workflow from **data preprocessing to deployment**

---

## 📂 Dataset Used

**Dataset Name:** `drug200.csv`

### Features:
- `Age` → Patient age
- `Sex` → Male / Female
- `BP` → Blood Pressure (LOW / NORMAL / HIGH)
- `Cholesterol` → Cholesterol level (NORMAL / HIGH)
- `Na_to_K` → Sodium to Potassium ratio

### Target:
- `Drug` → Predicted drug class

---

## ⚙️ Technologies Used

- **Python**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **Seaborn**
- **Scikit-learn**
- **Joblib**
- **Streamlit**

---

## 🧠 Machine Learning Workflow

This project follows a complete machine learning pipeline:

1. **Data Collection**
2. **Exploratory Data Analysis (EDA)**
3. **Data Preprocessing**
4. **Feature Engineering**
5. **Model Building**
6. **Model Evaluation**
7. **Model Comparison**
8. **Hyperparameter Tuning**
9. **Final Model Selection**
10. **Deployment using Streamlit**

---

## 📊 Models Used

Multiple classification models were tested:

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier
- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)
- Naive Bayes

### ✅ Final Selected Model:
**Random Forest Classifier**

Reason:
- High accuracy
- Better performance compared to other models
- Good generalization ability

---

## 🏗️ Project Structure

```bash
Drug-Prediction-Project/
│
├── app.py
├── train_model.py
├── requirements.txt
├── README.md
├── drug200.csv
├── model.pkl
├── sex_encoder.pkl
├── bp_encoder.pkl
├── chol_encoder.pkl
└── drug_encoder.pkl
