#!/bin/sh

# Start FastAPI in background
uvicorn backend.main:app --host 0.0.0.0 --port 8000 &

# Start Streamlit in foreground
streamlit run frontend/streamlit_app.py --server.port 8501 --server.address=0.0.0.0