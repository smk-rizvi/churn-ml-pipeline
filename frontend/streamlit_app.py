import streamlit as st
import requests

st.title("Bank Customer Churn Prediction")

st.markdown("Enter customer information below:")

# Input fields
credit_score = st.number_input("Credit Score", min_value=300, max_value=850, value=650)
age = st.number_input("Age", min_value=18, max_value=100, value=35)
tenure = st.slider("Tenure", 0, 10, 3)
balance = st.number_input("Balance", min_value=0.0, value=50000.0)
products_number = st.slider("Number of Products", 1, 4, 2)
credit_card = st.selectbox("Has Credit Card?", [0, 1])
active_member = st.selectbox("Active Member?", [0, 1])
estimated_salary = st.number_input("Estimated Salary", min_value=0.0, value=70000.0)
country = st.selectbox("Country", ["France", "Germany", "Spain"])
gender = st.selectbox("Gender", ["Female", "Male"])

# One-hot encoding
country_Germany = 1 if country == "Germany" else 0
country_Spain = 1 if country == "Spain" else 0
gender_Male = 1 if gender == "Male" else 0

# On click
if st.button("Predict Churn"):
    input_data = {
        "credit_score": credit_score,
        "age": age,
        "tenure": tenure,
        "balance": balance,
        "products_number": products_number,
        "credit_card": credit_card,
        "active_member": active_member,
        "estimated_salary": estimated_salary,
        "country_Germany": country_Germany,
        "country_Spain": country_Spain,
        "gender_Male": gender_Male
    }

    response = requests.post("http://127.0.0.1:8000/predict", json=input_data)

    if response.status_code == 200:
        prediction = response.json()["churn_prediction"]
        if prediction == 1:
            st.error("⚠️ This customer is likely to churn.")
        else:
            st.success("✅ This customer is likely to stay.")
    else:
        st.error("❌ Failed to get prediction.")
