import os
import sys
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict, Any

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import DISEASES, ALGORITHMS, DISCLAIMER
from api.schemas import PredictionResponse, disease_models
from api.predictor import load_model, load_scaler, predict, get_recommendations

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Pre-load all models on startup
    for disease_key in DISEASES.keys():
        try:
            load_model(disease_key)
            load_scaler(disease_key)
        except Exception as e:
            print(f"Warning: Failed to load model/scaler for {disease_key}: {e}")
    yield

app = FastAPI(
    title='Multi-Disease Prediction System API',
    description=f"API for Multi-Disease Prediction System.\n\n{DISCLAIMER}",
    lifespan=lifespan
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def add_disclaimer_header(request, call_next):
    response = await call_next(request)
    response.headers["X-AI-Disclaimer"] = "This is an AI prediction, not medical advice. Consult a doctor."
    return response

@app.get("/")
def read_root():
    """Root endpoint returning welcome message"""
    return {"message": "Welcome to the Multi-Disease Prediction System API"}

@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

@app.get("/diseases")
def get_diseases():
    """Returns list of all supported diseases with their info"""
    return [{"id": k, **v} for k, v in DISEASES.items()]

@app.get("/diseases/{disease_key}")
def get_disease(disease_key: str):
    """Returns info about a specific disease including its features"""
    if disease_key not in DISEASES:
        raise HTTPException(status_code=404, detail="Disease not found")
    return DISEASES[disease_key]

@app.post("/predict/{disease_key}", response_model=PredictionResponse)
def run_prediction(disease_key: str, input_data: Dict[str, Any] = Body(...)):
    """Accepts disease-specific input data, runs prediction, returns response"""
    if disease_key not in DISEASES:
        raise HTTPException(status_code=404, detail="Disease not found")
        
    try:
        # Validate data using dynamically generated Pydantic model
        disease_model = disease_models[disease_key]
        validated_data = disease_model(**input_data)
        
        # Run prediction
        result = predict(disease_key, validated_data.model_dump())
        prediction = result["prediction"]
        risk_level = result["risk_level"]
        
        disease_info = DISEASES[disease_key]
        pred_label = disease_info["positive_label"] if prediction == 1 else disease_info["negative_label"]
        
        recs = get_recommendations(disease_key, prediction, risk_level)
        
        return PredictionResponse(
            disease_name=disease_info["name"],
            prediction=prediction,
            prediction_label=pred_label,
            confidence=result["confidence"],
            risk_level=risk_level,
            recommendations=recs
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Validation Error: {str(e)}")
    except FileNotFoundError as e:
        raise HTTPException(status_code=500, detail=f"Model Error: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction Error: {str(e)}")

@app.get("/models/info")
def get_models_info():
    """Returns info about trained models"""
    return {"algorithms": ALGORITHMS}
