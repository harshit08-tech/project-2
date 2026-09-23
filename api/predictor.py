import os
import joblib
import numpy as np
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import DISEASES, MODELS_DIR, SCALERS_DIR, get_feature_names

# In-memory cache for models and scalers
_models = {}
_scalers = {}

def load_model(disease_key: str):
    """Loads the trained model from models/ directory using joblib"""
    if disease_key in _models:
        return _models[disease_key]
        
    model_path = os.path.join(MODELS_DIR, DISEASES[disease_key]['model_file'])
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found: {model_path}")
        
    model = joblib.load(model_path)
    _models[disease_key] = model
    return model

def load_scaler(disease_key: str):
    """Loads the fitted scaler from models/scalers/"""
    if disease_key in _scalers:
        return _scalers[disease_key]
        
    scaler_path = os.path.join(SCALERS_DIR, DISEASES[disease_key]['scaler_file'])
    if not os.path.exists(scaler_path):
        raise FileNotFoundError(f"Scaler file not found: {scaler_path}")
        
    scaler = joblib.load(scaler_path)
    _scalers[disease_key] = scaler
    return scaler

def predict(disease_key: str, input_data: dict) -> dict:
    """Preprocesses input, runs prediction, and returns results dict"""
    model = load_model(disease_key)
    scaler = load_scaler(disease_key)
    
    feature_names = get_feature_names(disease_key)
    # Extract features in the correct order
    features = [input_data[f] for f in feature_names]
    features_array = np.array([features])
    
    scaled_features = scaler.transform(features_array)
    prediction = int(model.predict(scaled_features)[0])
    
    # Calculate confidence
    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba(scaled_features)[0]
        confidence = float(probabilities[prediction])
    else:
        confidence = 1.0
        
    # Determine risk level based on confidence
    if confidence < 0.4:
        risk_level = 'Low'
    elif confidence <= 0.7:
        risk_level = 'Medium'
    else:
        risk_level = 'High'
        
    return {
        "prediction": prediction,
        "confidence": confidence,
        "risk_level": risk_level
    }

def get_recommendations(disease_key: str, prediction: int, risk_level: str) -> list[str]:
    """Returns list of health recommendations based on disease and risk level"""
    if prediction == 0:
        return [
            "Maintain your current healthy lifestyle.",
            "Continue with regular checkups.",
            "Ensure a balanced diet and regular physical activity."
        ]
        
    if risk_level == 'Low':
        return [
            "Monitor your symptoms closely.",
            "Consult a doctor for a routine evaluation.",
            "Consider lifestyle and dietary improvements."
        ]
    elif risk_level == 'Medium':
        return [
            "Schedule an appointment with a specialist soon.",
            "Follow strict dietary and health guidelines.",
            "Avoid stress and overexertion."
        ]
    else:
        return [
            "Seek immediate medical consultation.",
            "Follow any prescribed medication or treatments strictly.",
            "Undergo comprehensive medical testing as advised by a doctor."
        ]
