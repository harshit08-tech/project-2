from pydantic import BaseModel, Field, create_model
from typing import Optional, List, Dict, Any
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import DISEASES

class PredictionResponse(BaseModel):
    """Unified response model for predictions"""
    disease_name: str
    prediction: int
    prediction_label: str
    confidence: float
    risk_level: str
    recommendations: List[str]

class PatientInfo(BaseModel):
    """Patient information"""
    full_name: str
    age: int
    gender: str
    blood_group: Optional[str] = None
    contact: Optional[str] = None

class FullPredictionRequest(BaseModel):
    """Combined request model"""
    patient_info: PatientInfo
    disease_data: Dict[str, Any]

# Dynamically generate schemas for each disease based on config
disease_models = {}

for disease_key, disease_info in DISEASES.items():
    model_name = ''.join(word.capitalize() for word in disease_key.split('_')) + 'Input'
    fields = {}
    example_dict = {}
    
    for feature_name, feature_data in disease_info['features'].items():
        f_type = feature_data['type']
        f_min = feature_data.get('min')
        f_max = feature_data.get('max')
        f_default = feature_data.get('default')
        f_desc = feature_data.get('description', '')
        f_label = feature_data.get('label', '')
        
        if f_type == 'select':
            # Determine if options are float or int
            option_values = list(feature_data.get('options', {}).values())
            has_float = any(isinstance(v, float) for v in option_values)
            py_type = float if has_float else int
            fields[feature_name] = (py_type, Field(default=f_default, description=f_desc, title=f_label))
            example_dict[feature_name] = f_default
        elif f_type == 'int':
            fields[feature_name] = (int, Field(default=f_default, ge=f_min, le=f_max, description=f_desc, title=f_label))
            example_dict[feature_name] = f_default
        elif f_type == 'float':
            fields[feature_name] = (float, Field(default=f_default, ge=f_min, le=f_max, description=f_desc, title=f_label))
            example_dict[feature_name] = f_default
            
    model = create_model(model_name, **fields, __base__=BaseModel)
    model.model_config = {"json_schema_extra": {"example": example_dict}}
    disease_models[disease_key] = model

# Export them explicitly for easy importing
DiabetesInput = disease_models.get("diabetes")
HeartDiseaseInput = disease_models.get("heart_disease")
LiverDiseaseInput = disease_models.get("liver_disease")
KidneyDiseaseInput = disease_models.get("kidney_disease")
BreastCancerInput = disease_models.get("breast_cancer")
ParkinsonsInput = disease_models.get("parkinsons")
StrokeInput = disease_models.get("stroke")
HepatitisInput = disease_models.get("hepatitis")
