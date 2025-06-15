from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import os

app = FastAPI()

# Load trained model
print("Current directory:", os.getcwd())

try:
    print("Loading model...")
    model = joblib.load("../model.pkl")  # Adjust path if needed
    print("Model loaded successfully.")
except Exception as e:
    print("Error loading model:", e)

# Define input schema
class CustomerInput(BaseModel):
    credit_score: float
    age: float
    tenure: int
    balance: float
    products_number: int
    credit_card: int
    active_member: int
    estimated_salary: float
    country_Germany: int
    country_Spain: int
    gender_Male: int

@app.get("/")
def read_root():
    return {"message": "Bank Churn Prediction API is live!"}

@app.post("/predict")
def predict_churn(data: CustomerInput):
    input_data = np.array([[
        data.credit_score,
        data.age,
        data.tenure,
        data.balance,
        data.products_number,
        data.credit_card,
        data.active_member,
        data.estimated_salary,
        data.country_Germany,
        data.country_Spain,
        data.gender_Male
    ]])

    prediction = model.predict(input_data)[0]
    return {"churn_prediction": int(prediction)}