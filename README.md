# Churn Prediction ML Project

This project is an end-to-end ML pipeline for predicting customer churn using FastAPI, Streamlit, Docker, GitHub Actions, and AWS EC2.

## 🔧 Tech Stack
- Python (pandas, sklearn, xgboost)
- MLflow (for experiment tracking)
- FastAPI (backend REST API)
- Streamlit (frontend UI)
- Docker (containerization)
- GitHub Actions (CI/CD)
- AWS EC2 (deployment)

## 📊 MLflow Metrics
- Logged metrics: accuracy, precision, recall
- Models compared: Logistic Regression, Random Forest, XGBoost
- Best model: Random Forest
- Screenshot included in submission

## 🚀 Deployment

### DockerHub:
Image: `smk-rizvi/churn-ml-app`  
Built via GitHub Actions

### Live URLs:
- Streamlit: `http://<your-ec2-ip>:8501`
- FastAPI: `http://<your-ec2-ip>:8000/docs`

## 📁 Folder Structure
