import requests
import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from config import API_BASE_URL

TIMEOUT = 10

def check_health():
    """Check if the API is running."""
    try:
        response = requests.get(f"{API_BASE_URL}/health", timeout=TIMEOUT)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

def get_diseases():
    """Get list of supported diseases."""
    try:
        response = requests.get(f"{API_BASE_URL}/diseases", timeout=TIMEOUT)
        if response.status_code == 200:
            return response.json()
        return None
    except requests.exceptions.RequestException:
        return None

def get_model_info():
    """Get info about loaded models."""
    try:
        response = requests.get(f"{API_BASE_URL}/models/info", timeout=TIMEOUT)
        if response.status_code == 200:
            return response.json()
        return None
    except requests.exceptions.RequestException:
        return None

def predict_disease(disease_key, input_data):
    """Make a prediction for a specific disease."""
    try:
        headers = {'Content-Type': 'application/json'}
        
        # Add a slight delay for realistic UX animation
        time.sleep(1.0)
        
        response = requests.post(
            f"{API_BASE_URL}/predict/{disease_key}", 
            headers=headers,
            json=input_data,
            timeout=TIMEOUT
        )
        
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return {"error": f"Model for {disease_key} not found. Please train the model first."}
        elif response.status_code == 400:
            return {"error": f"Invalid input data: {response.text}"}
        else:
            return {"error": f"API Error ({response.status_code}): {response.text}"}
            
    except requests.exceptions.ConnectionError:
        return {"error": "Connection to the API failed. Please ensure the backend server is running."}
    except requests.exceptions.Timeout:
        return {"error": "The request timed out. The server might be overloaded."}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {str(e)}"}
