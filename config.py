"""
Multi-Disease Prediction System — Central Configuration
========================================================
Single source of truth for all disease definitions, feature specifications,
and system-wide settings. All modules import from this file.

Team: Harshit, Shorya, Tanisha
Course: BCA-AI | 503 - Applied Artificial Intelligence
"""

import os

# ============================================================
# PROJECT PATHS
# ============================================================
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
DATASETS_DIR = os.path.join(PROJECT_ROOT, "datasets")
MODELS_DIR = os.path.join(PROJECT_ROOT, "models")
SCALERS_DIR = os.path.join(PROJECT_ROOT, "models", "scalers")
REPORTS_DIR = os.path.join(PROJECT_ROOT, "reports")

# ============================================================
# API CONFIGURATION
# ============================================================
API_HOST = "127.0.0.1"
API_PORT = 8000
API_BASE_URL = f"http://{API_HOST}:{API_PORT}"

# ============================================================
# TEAM MEMBERS
# ============================================================
TEAM_MEMBERS = [
    {"name": "Harshit", "role": "ML Engineer & Team Lead", "icon": "👨‍💻"},
    {"name": "Shorya", "role": "Backend Developer & Data Analyst", "icon": "🧑‍💻"},
    {"name": "Tanisha", "role": "Frontend Developer & UI/UX Designer", "icon": "👩‍💻"},
]

# ============================================================
# AI DISCLAIMER
# ============================================================
DISCLAIMER = (
    "⚠️ IMPORTANT DISCLAIMER: This system is NOT a certified medical professional. "
    "It is an AI-powered tool that provides predictions based on statistical data analysis and "
    "machine learning algorithms. These predictions should NOT be used as a substitute for "
    "professional medical advice, diagnosis, or treatment. Always consult a qualified "
    "healthcare provider for any medical decisions. The developers of this system are not "
    "responsible for any actions taken based on the predictions provided."
)

DISCLAIMER_SHORT = "🤖 AI Prediction System — Not a Certified Doctor. Always Consult a Healthcare Professional."

# ============================================================
# UI COLOR PALETTE
# ============================================================
COLORS = {
    "primary": "#4F46E5",
    "primary_light": "#6366F1",
    "secondary": "#06B6D4",
    "secondary_light": "#22D3EE",
    "accent": "#10B981",
    "accent_light": "#34D399",
    "danger": "#EF4444",
    "danger_light": "#F87171",
    "warning": "#F59E0B",
    "warning_light": "#FBBF24",
    "background": "#0F172A",
    "surface": "#1E293B",
    "surface_light": "#334155",
    "text": "#F1F5F9",
    "text_secondary": "#94A3B8",
    "text_muted": "#64748B",
    "border": "#334155",
    "success": "#10B981",
}

# ============================================================
# ML TRAINING CONFIGURATION
# ============================================================
TRAIN_TEST_SPLIT = 0.2
RANDOM_STATE = 42

ALGORITHMS = {
    "Random Forest": {
        "class": "RandomForestClassifier",
        "params": {"n_estimators": 100, "random_state": 42, "max_depth": 10}
    },
    "Logistic Regression": {
        "class": "LogisticRegression",
        "params": {"max_iter": 1000, "random_state": 42}
    },
    "SVM": {
        "class": "SVC",
        "params": {"kernel": "rbf", "probability": True, "random_state": 42}
    },
    "KNN": {
        "class": "KNeighborsClassifier",
        "params": {"n_neighbors": 5}
    },
    "Gradient Boosting": {
        "class": "GradientBoostingClassifier",
        "params": {"n_estimators": 100, "random_state": 42, "max_depth": 5}
    },
}

# ============================================================
# DISEASE CONFIGURATIONS (8 DISEASES)
# ============================================================
DISEASES = {
    # --------------------------------------------------------
    # 1. DIABETES
    # --------------------------------------------------------
    "diabetes": {
        "name": "Diabetes",
        "full_name": "Diabetes Mellitus Prediction",
        "icon": "🩸",
        "color": "#8B5CF6",
        "gradient": "linear-gradient(135deg, #8B5CF6, #A78BFA)",
        "description": "Predicts the likelihood of diabetes based on diagnostic measurements including glucose levels, BMI, and insulin.",
        "dataset_file": "diabetes.csv",
        "model_file": "diabetes_model.pkl",
        "scaler_file": "diabetes_scaler.pkl",
        "target_column": "Outcome",
        "positive_label": "Diabetic",
        "negative_label": "Not Diabetic",
        "sample_size": 768,
        "features": {
            "Pregnancies": {
                "type": "int", "min": 0, "max": 17, "default": 1,
                "label": "Number of Pregnancies",
                "description": "Total number of pregnancies",
                "normal_range": "0-5", "step": 1
            },
            "Glucose": {
                "type": "float", "min": 0.0, "max": 200.0, "default": 100.0,
                "label": "Glucose Level (mg/dL)",
                "description": "Plasma glucose concentration (2h oral glucose tolerance test)",
                "normal_range": "70-100 mg/dL", "step": 1.0
            },
            "BloodPressure": {
                "type": "float", "min": 0.0, "max": 140.0, "default": 70.0,
                "label": "Blood Pressure (mm Hg)",
                "description": "Diastolic blood pressure",
                "normal_range": "60-80 mm Hg", "step": 1.0
            },
            "SkinThickness": {
                "type": "float", "min": 0.0, "max": 100.0, "default": 20.0,
                "label": "Skin Thickness (mm)",
                "description": "Triceps skin fold thickness",
                "normal_range": "10-40 mm", "step": 1.0
            },
            "Insulin": {
                "type": "float", "min": 0.0, "max": 900.0, "default": 80.0,
                "label": "Insulin Level (μU/mL)",
                "description": "2-Hour serum insulin",
                "normal_range": "16-166 μU/mL", "step": 1.0
            },
            "BMI": {
                "type": "float", "min": 0.0, "max": 70.0, "default": 25.0,
                "label": "BMI (kg/m²)",
                "description": "Body Mass Index = weight(kg) / height(m)²",
                "normal_range": "18.5-24.9", "step": 0.1
            },
            "DiabetesPedigreeFunction": {
                "type": "float", "min": 0.0, "max": 2.5, "default": 0.5,
                "label": "Diabetes Pedigree Function",
                "description": "Likelihood score of diabetes based on family history",
                "normal_range": "0.0-1.0", "step": 0.01
            },
            "Age": {
                "type": "int", "min": 1, "max": 120, "default": 30,
                "label": "Age (years)",
                "description": "Age of the patient",
                "normal_range": "21-80", "step": 1
            },
        },
    },

    # --------------------------------------------------------
    # 2. HEART DISEASE
    # --------------------------------------------------------
    "heart_disease": {
        "name": "Heart Disease",
        "full_name": "Heart Disease Prediction",
        "icon": "❤️",
        "color": "#EF4444",
        "gradient": "linear-gradient(135deg, #EF4444, #F87171)",
        "description": "Predicts the presence of heart disease based on clinical parameters including cholesterol, blood pressure, and ECG results.",
        "dataset_file": "heart_disease.csv",
        "model_file": "heart_disease_model.pkl",
        "scaler_file": "heart_disease_scaler.pkl",
        "target_column": "HeartDisease",
        "positive_label": "Heart Disease Detected",
        "negative_label": "No Heart Disease",
        "sample_size": 920,
        "features": {
            "Age": {
                "type": "int", "min": 1, "max": 120, "default": 50,
                "label": "Age (years)", "description": "Age of the patient",
                "normal_range": "20-80", "step": 1
            },
            "Sex": {
                "type": "select", "options": {"Male": 1, "Female": 0}, "default": 1,
                "label": "Sex", "description": "Biological sex"
            },
            "ChestPainType": {
                "type": "select",
                "options": {"Typical Angina": 0, "Atypical Angina": 1, "Non-Anginal Pain": 2, "Asymptomatic": 3},
                "default": 0,
                "label": "Chest Pain Type", "description": "Type of chest pain experienced"
            },
            "RestingBP": {
                "type": "float", "min": 80.0, "max": 200.0, "default": 120.0,
                "label": "Resting Blood Pressure (mm Hg)", "description": "Resting blood pressure on admission",
                "normal_range": "90-120 mm Hg", "step": 1.0
            },
            "Cholesterol": {
                "type": "float", "min": 100.0, "max": 600.0, "default": 200.0,
                "label": "Cholesterol (mg/dL)", "description": "Serum cholesterol level",
                "normal_range": "125-200 mg/dL", "step": 1.0
            },
            "FastingBS": {
                "type": "select", "options": {"No (≤120 mg/dL)": 0, "Yes (>120 mg/dL)": 1}, "default": 0,
                "label": "Fasting Blood Sugar > 120", "description": "Is fasting blood sugar > 120 mg/dL?"
            },
            "RestingECG": {
                "type": "select",
                "options": {"Normal": 0, "ST-T Abnormality": 1, "LV Hypertrophy": 2},
                "default": 0,
                "label": "Resting ECG", "description": "Resting electrocardiographic results"
            },
            "MaxHR": {
                "type": "float", "min": 60.0, "max": 220.0, "default": 150.0,
                "label": "Max Heart Rate", "description": "Maximum heart rate achieved during exercise",
                "normal_range": "60-200 bpm", "step": 1.0
            },
            "ExerciseAngina": {
                "type": "select", "options": {"No": 0, "Yes": 1}, "default": 0,
                "label": "Exercise Angina", "description": "Does exercise induce angina?"
            },
            "Oldpeak": {
                "type": "float", "min": -5.0, "max": 10.0, "default": 0.0,
                "label": "ST Depression (Oldpeak)", "description": "ST depression induced by exercise vs rest",
                "normal_range": "0-2", "step": 0.1
            },
            "ST_Slope": {
                "type": "select",
                "options": {"Upsloping": 0, "Flat": 1, "Downsloping": 2},
                "default": 0,
                "label": "ST Slope", "description": "Slope of peak exercise ST segment"
            },
        },
    },

    # --------------------------------------------------------
    # 3. LIVER DISEASE
    # --------------------------------------------------------
    "liver_disease": {
        "name": "Liver Disease",
        "full_name": "Liver Disease Prediction",
        "icon": "🫁",
        "color": "#F59E0B",
        "gradient": "linear-gradient(135deg, #F59E0B, #FBBF24)",
        "description": "Predicts liver disease using blood test parameters including bilirubin, enzyme levels, and protein ratios.",
        "dataset_file": "liver_disease.csv",
        "model_file": "liver_disease_model.pkl",
        "scaler_file": "liver_disease_scaler.pkl",
        "target_column": "Dataset",
        "positive_label": "Liver Disease Detected",
        "negative_label": "No Liver Disease",
        "sample_size": 583,
        "features": {
            "Age": {
                "type": "int", "min": 1, "max": 120, "default": 45,
                "label": "Age (years)", "description": "Age of the patient",
                "normal_range": "18-80", "step": 1
            },
            "Gender": {
                "type": "select", "options": {"Male": 1, "Female": 0}, "default": 1,
                "label": "Gender", "description": "Biological gender"
            },
            "Total_Bilirubin": {
                "type": "float", "min": 0.0, "max": 80.0, "default": 1.0,
                "label": "Total Bilirubin (mg/dL)", "description": "Total bilirubin in blood",
                "normal_range": "0.1-1.2 mg/dL", "step": 0.1
            },
            "Direct_Bilirubin": {
                "type": "float", "min": 0.0, "max": 20.0, "default": 0.3,
                "label": "Direct Bilirubin (mg/dL)", "description": "Direct bilirubin level",
                "normal_range": "0.0-0.3 mg/dL", "step": 0.1
            },
            "Alkaline_Phosphotase": {
                "type": "float", "min": 50.0, "max": 2200.0, "default": 200.0,
                "label": "Alkaline Phosphatase (IU/L)", "description": "Alkaline phosphatase enzyme",
                "normal_range": "44-147 IU/L", "step": 1.0
            },
            "Alamine_Aminotransferase": {
                "type": "float", "min": 5.0, "max": 2000.0, "default": 25.0,
                "label": "ALT (IU/L)", "description": "Alamine aminotransferase (SGPT)",
                "normal_range": "7-56 IU/L", "step": 1.0
            },
            "Aspartate_Aminotransferase": {
                "type": "float", "min": 5.0, "max": 5000.0, "default": 30.0,
                "label": "AST (IU/L)", "description": "Aspartate aminotransferase (SGOT)",
                "normal_range": "10-40 IU/L", "step": 1.0
            },
            "Total_Protiens": {
                "type": "float", "min": 2.0, "max": 10.0, "default": 6.5,
                "label": "Total Proteins (g/dL)", "description": "Total protein in blood",
                "normal_range": "6.0-8.3 g/dL", "step": 0.1
            },
            "Albumin": {
                "type": "float", "min": 0.5, "max": 6.0, "default": 3.5,
                "label": "Albumin (g/dL)", "description": "Albumin protein level",
                "normal_range": "3.5-5.5 g/dL", "step": 0.1
            },
            "Albumin_and_Globulin_Ratio": {
                "type": "float", "min": 0.0, "max": 3.0, "default": 1.0,
                "label": "A/G Ratio", "description": "Albumin to Globulin ratio",
                "normal_range": "1.1-2.5", "step": 0.1
            },
        },
    },

    # --------------------------------------------------------
    # 4. KIDNEY DISEASE
    # --------------------------------------------------------
    "kidney_disease": {
        "name": "Kidney Disease",
        "full_name": "Chronic Kidney Disease Prediction",
        "icon": "🫘",
        "color": "#06B6D4",
        "gradient": "linear-gradient(135deg, #06B6D4, #22D3EE)",
        "description": "Predicts chronic kidney disease using blood and urine test results including creatinine, hemoglobin, and albumin.",
        "dataset_file": "kidney_disease.csv",
        "model_file": "kidney_disease_model.pkl",
        "scaler_file": "kidney_disease_scaler.pkl",
        "target_column": "Classification",
        "positive_label": "Kidney Disease Detected",
        "negative_label": "No Kidney Disease",
        "sample_size": 400,
        "features": {
            "Age": {
                "type": "int", "min": 1, "max": 120, "default": 50,
                "label": "Age (years)", "description": "Age of the patient",
                "normal_range": "18-80", "step": 1
            },
            "Blood_Pressure": {
                "type": "float", "min": 50.0, "max": 180.0, "default": 80.0,
                "label": "Blood Pressure (mm Hg)", "description": "Diastolic blood pressure",
                "normal_range": "60-80 mm Hg", "step": 1.0
            },
            "Specific_Gravity": {
                "type": "select",
                "options": {"1.005": 1.005, "1.010": 1.010, "1.015": 1.015, "1.020": 1.020, "1.025": 1.025},
                "default": 1.020,
                "label": "Specific Gravity", "description": "Urine specific gravity"
            },
            "Albumin": {
                "type": "select",
                "options": {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5},
                "default": 0,
                "label": "Albumin in Urine", "description": "Albumin level in urine (0-5)"
            },
            "Sugar": {
                "type": "select",
                "options": {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5},
                "default": 0,
                "label": "Sugar in Urine", "description": "Sugar level in urine (0-5)"
            },
            "Blood_Glucose_Random": {
                "type": "float", "min": 50.0, "max": 500.0, "default": 120.0,
                "label": "Random Blood Glucose (mg/dL)", "description": "Random blood glucose level",
                "normal_range": "70-140 mg/dL", "step": 1.0
            },
            "Blood_Urea": {
                "type": "float", "min": 1.0, "max": 400.0, "default": 40.0,
                "label": "Blood Urea (mg/dL)", "description": "Blood urea level",
                "normal_range": "7-20 mg/dL", "step": 1.0
            },
            "Serum_Creatinine": {
                "type": "float", "min": 0.4, "max": 80.0, "default": 1.2,
                "label": "Serum Creatinine (mg/dL)", "description": "Serum creatinine level",
                "normal_range": "0.7-1.3 mg/dL", "step": 0.1
            },
            "Sodium": {
                "type": "float", "min": 100.0, "max": 165.0, "default": 140.0,
                "label": "Sodium (mEq/L)", "description": "Blood sodium level",
                "normal_range": "136-145 mEq/L", "step": 1.0
            },
            "Potassium": {
                "type": "float", "min": 2.0, "max": 50.0, "default": 4.5,
                "label": "Potassium (mEq/L)", "description": "Blood potassium level",
                "normal_range": "3.5-5.0 mEq/L", "step": 0.1
            },
            "Hemoglobin": {
                "type": "float", "min": 3.0, "max": 18.0, "default": 13.0,
                "label": "Hemoglobin (g/dL)", "description": "Blood hemoglobin level",
                "normal_range": "12-17 g/dL", "step": 0.1
            },
            "Red_Blood_Cell_Count": {
                "type": "float", "min": 2.0, "max": 8.0, "default": 5.0,
                "label": "RBC Count (millions/cmm)", "description": "Red blood cell count",
                "normal_range": "4.5-5.5", "step": 0.1
            },
            "White_Blood_Cell_Count": {
                "type": "float", "min": 2000.0, "max": 25000.0, "default": 8000.0,
                "label": "WBC Count (/cmm)", "description": "White blood cell count",
                "normal_range": "4500-11000", "step": 100.0
            },
            "Hypertension": {
                "type": "select", "options": {"No": 0, "Yes": 1}, "default": 0,
                "label": "Hypertension", "description": "Does the patient have hypertension?"
            },
            "Diabetes_Mellitus": {
                "type": "select", "options": {"No": 0, "Yes": 1}, "default": 0,
                "label": "Diabetes Mellitus", "description": "Does the patient have diabetes?"
            },
            "Appetite": {
                "type": "select", "options": {"Good": 0, "Poor": 1}, "default": 0,
                "label": "Appetite", "description": "Patient's appetite level"
            },
            "Pedal_Edema": {
                "type": "select", "options": {"No": 0, "Yes": 1}, "default": 0,
                "label": "Pedal Edema", "description": "Swelling in feet?"
            },
            "Anemia": {
                "type": "select", "options": {"No": 0, "Yes": 1}, "default": 0,
                "label": "Anemia", "description": "Does the patient have anemia?"
            },
        },
    },

    # --------------------------------------------------------
    # 5. BREAST CANCER
    # --------------------------------------------------------
    "breast_cancer": {
        "name": "Breast Cancer",
        "full_name": "Breast Cancer Prediction",
        "icon": "🎗️",
        "color": "#EC4899",
        "gradient": "linear-gradient(135deg, #EC4899, #F472B6)",
        "description": "Predicts breast cancer (malignant/benign) using cell nuclei measurements from fine needle aspirate (FNA) of a breast mass.",
        "dataset_file": "breast_cancer.csv",
        "model_file": "breast_cancer_model.pkl",
        "scaler_file": "breast_cancer_scaler.pkl",
        "target_column": "diagnosis",
        "positive_label": "Malignant (Cancerous)",
        "negative_label": "Benign (Non-Cancerous)",
        "sample_size": 569,
        "features": {
            "radius_mean": {
                "type": "float", "min": 5.0, "max": 30.0, "default": 14.0,
                "label": "Mean Radius", "description": "Mean distance from center to perimeter points",
                "normal_range": "10-15", "step": 0.1
            },
            "texture_mean": {
                "type": "float", "min": 9.0, "max": 40.0, "default": 19.0,
                "label": "Mean Texture", "description": "Standard deviation of gray-scale values",
                "normal_range": "15-22", "step": 0.1
            },
            "perimeter_mean": {
                "type": "float", "min": 40.0, "max": 200.0, "default": 92.0,
                "label": "Mean Perimeter", "description": "Mean perimeter of cell nuclei",
                "normal_range": "70-100", "step": 0.1
            },
            "area_mean": {
                "type": "float", "min": 140.0, "max": 2600.0, "default": 650.0,
                "label": "Mean Area", "description": "Mean area of cell nuclei",
                "normal_range": "400-800", "step": 1.0
            },
            "smoothness_mean": {
                "type": "float", "min": 0.05, "max": 0.17, "default": 0.10,
                "label": "Mean Smoothness", "description": "Local variation in radius lengths",
                "normal_range": "0.08-0.12", "step": 0.001
            },
            "compactness_mean": {
                "type": "float", "min": 0.01, "max": 0.35, "default": 0.10,
                "label": "Mean Compactness", "description": "Perimeter² / area - 1.0",
                "normal_range": "0.05-0.15", "step": 0.001
            },
            "concavity_mean": {
                "type": "float", "min": 0.0, "max": 0.45, "default": 0.09,
                "label": "Mean Concavity", "description": "Severity of concave contour portions",
                "normal_range": "0.03-0.15", "step": 0.001
            },
            "concave_points_mean": {
                "type": "float", "min": 0.0, "max": 0.2, "default": 0.05,
                "label": "Mean Concave Points", "description": "Number of concave contour portions",
                "normal_range": "0.02-0.08", "step": 0.001
            },
            "symmetry_mean": {
                "type": "float", "min": 0.1, "max": 0.35, "default": 0.18,
                "label": "Mean Symmetry", "description": "Symmetry of cell nuclei",
                "normal_range": "0.15-0.22", "step": 0.001
            },
            "fractal_dimension_mean": {
                "type": "float", "min": 0.04, "max": 0.1, "default": 0.06,
                "label": "Mean Fractal Dimension", "description": "Coastline approximation - 1",
                "normal_range": "0.05-0.07", "step": 0.001
            },
        },
    },

    # --------------------------------------------------------
    # 6. PARKINSON'S DISEASE
    # --------------------------------------------------------
    "parkinsons": {
        "name": "Parkinson's Disease",
        "full_name": "Parkinson's Disease Prediction",
        "icon": "🧠",
        "color": "#7C3AED",
        "gradient": "linear-gradient(135deg, #7C3AED, #A78BFA)",
        "description": "Detects Parkinson's disease using biomedical voice measurements including jitter, shimmer, and harmonic-to-noise ratio.",
        "dataset_file": "parkinsons.csv",
        "model_file": "parkinsons_model.pkl",
        "scaler_file": "parkinsons_scaler.pkl",
        "target_column": "status",
        "positive_label": "Parkinson's Detected",
        "negative_label": "No Parkinson's",
        "sample_size": 195,
        "features": {
            "MDVP_Fo_Hz": {
                "type": "float", "min": 80.0, "max": 270.0, "default": 150.0,
                "label": "Avg Vocal Frequency (Hz)", "description": "Average vocal fundamental frequency",
                "normal_range": "85-255 Hz", "step": 0.1
            },
            "MDVP_Fhi_Hz": {
                "type": "float", "min": 100.0, "max": 600.0, "default": 200.0,
                "label": "Max Vocal Frequency (Hz)", "description": "Maximum vocal fundamental frequency",
                "normal_range": "100-600 Hz", "step": 0.1
            },
            "MDVP_Flo_Hz": {
                "type": "float", "min": 60.0, "max": 240.0, "default": 120.0,
                "label": "Min Vocal Frequency (Hz)", "description": "Minimum vocal fundamental frequency",
                "normal_range": "65-240 Hz", "step": 0.1
            },
            "MDVP_Jitter_Percent": {
                "type": "float", "min": 0.0, "max": 0.07, "default": 0.006,
                "label": "Jitter (%)", "description": "Variation in fundamental frequency",
                "normal_range": "0-0.02%", "step": 0.001
            },
            "MDVP_Shimmer": {
                "type": "float", "min": 0.0, "max": 0.12, "default": 0.03,
                "label": "Shimmer", "description": "Variation in amplitude",
                "normal_range": "0-0.05", "step": 0.001
            },
            "MDVP_Shimmer_dB": {
                "type": "float", "min": 0.0, "max": 1.5, "default": 0.3,
                "label": "Shimmer (dB)", "description": "Shimmer in decibels",
                "normal_range": "0-0.5 dB", "step": 0.01
            },
            "NHR": {
                "type": "float", "min": 0.0, "max": 0.35, "default": 0.02,
                "label": "Noise-to-Harmonics Ratio", "description": "Ratio of noise to tonal components",
                "normal_range": "0-0.1", "step": 0.001
            },
            "HNR": {
                "type": "float", "min": 5.0, "max": 35.0, "default": 22.0,
                "label": "Harmonics-to-Noise Ratio", "description": "Ratio of harmonics to noise",
                "normal_range": "15-30", "step": 0.1
            },
            "RPDE": {
                "type": "float", "min": 0.2, "max": 0.7, "default": 0.5,
                "label": "RPDE", "description": "Recurrence period density entropy",
                "normal_range": "0.3-0.6", "step": 0.01
            },
            "DFA": {
                "type": "float", "min": 0.5, "max": 0.85, "default": 0.7,
                "label": "DFA", "description": "Detrended fluctuation analysis",
                "normal_range": "0.55-0.80", "step": 0.01
            },
            "spread1": {
                "type": "float", "min": -8.0, "max": -2.0, "default": -5.0,
                "label": "Spread1", "description": "Nonlinear fundamental frequency variation",
                "normal_range": "-7 to -3", "step": 0.1
            },
            "spread2": {
                "type": "float", "min": 0.0, "max": 0.5, "default": 0.2,
                "label": "Spread2", "description": "Nonlinear fundamental frequency variation",
                "normal_range": "0.05-0.4", "step": 0.01
            },
            "D2": {
                "type": "float", "min": 1.0, "max": 4.0, "default": 2.5,
                "label": "D2", "description": "Correlation dimension complexity measure",
                "normal_range": "1.5-3.5", "step": 0.1
            },
            "PPE": {
                "type": "float", "min": 0.0, "max": 0.6, "default": 0.2,
                "label": "PPE", "description": "Pitch period entropy",
                "normal_range": "0.05-0.4", "step": 0.01
            },
        },
    },

    # --------------------------------------------------------
    # 7. STROKE
    # --------------------------------------------------------
    "stroke": {
        "name": "Stroke",
        "full_name": "Stroke Risk Prediction",
        "icon": "🧠",
        "color": "#DC2626",
        "gradient": "linear-gradient(135deg, #DC2626, #F87171)",
        "description": "Predicts stroke risk based on demographics, lifestyle, and health conditions including hypertension and glucose levels.",
        "dataset_file": "stroke.csv",
        "model_file": "stroke_model.pkl",
        "scaler_file": "stroke_scaler.pkl",
        "target_column": "stroke",
        "positive_label": "High Stroke Risk",
        "negative_label": "Low Stroke Risk",
        "sample_size": 5000,
        "features": {
            "Gender": {
                "type": "select", "options": {"Male": 1, "Female": 0}, "default": 1,
                "label": "Gender", "description": "Biological gender"
            },
            "Age": {
                "type": "float", "min": 0.0, "max": 120.0, "default": 50.0,
                "label": "Age (years)", "description": "Age of the patient",
                "normal_range": "18-80", "step": 1.0
            },
            "Hypertension": {
                "type": "select", "options": {"No": 0, "Yes": 1}, "default": 0,
                "label": "Hypertension", "description": "Does the patient have hypertension?"
            },
            "Heart_Disease": {
                "type": "select", "options": {"No": 0, "Yes": 1}, "default": 0,
                "label": "Heart Disease", "description": "Does the patient have heart disease?"
            },
            "Ever_Married": {
                "type": "select", "options": {"No": 0, "Yes": 1}, "default": 1,
                "label": "Ever Married", "description": "Has the patient ever been married?"
            },
            "Work_Type": {
                "type": "select",
                "options": {"Children": 0, "Govt Job": 1, "Never Worked": 2, "Private": 3, "Self-employed": 4},
                "default": 3,
                "label": "Work Type", "description": "Type of occupation"
            },
            "Residence_Type": {
                "type": "select", "options": {"Rural": 0, "Urban": 1}, "default": 1,
                "label": "Residence Type", "description": "Urban or Rural"
            },
            "Avg_Glucose_Level": {
                "type": "float", "min": 50.0, "max": 280.0, "default": 100.0,
                "label": "Avg Glucose Level (mg/dL)", "description": "Average blood glucose level",
                "normal_range": "70-140 mg/dL", "step": 1.0
            },
            "BMI": {
                "type": "float", "min": 10.0, "max": 100.0, "default": 25.0,
                "label": "BMI (kg/m²)", "description": "Body Mass Index",
                "normal_range": "18.5-24.9", "step": 0.1
            },
            "Smoking_Status": {
                "type": "select",
                "options": {"Unknown": 0, "Formerly Smoked": 1, "Never Smoked": 2, "Smokes": 3},
                "default": 2,
                "label": "Smoking Status", "description": "Patient's smoking habits"
            },
        },
    },

    # --------------------------------------------------------
    # 8. HEPATITIS
    # --------------------------------------------------------
    "hepatitis": {
        "name": "Hepatitis",
        "full_name": "Hepatitis Prediction",
        "icon": "🦠",
        "color": "#059669",
        "gradient": "linear-gradient(135deg, #059669, #34D399)",
        "description": "Predicts hepatitis outcome based on clinical findings and liver function test results.",
        "dataset_file": "hepatitis.csv",
        "model_file": "hepatitis_model.pkl",
        "scaler_file": "hepatitis_scaler.pkl",
        "target_column": "Class",
        "positive_label": "Hepatitis Detected",
        "negative_label": "No Hepatitis",
        "sample_size": 155,
        "features": {
            "Age": {
                "type": "int", "min": 1, "max": 120, "default": 40,
                "label": "Age (years)", "description": "Age of the patient",
                "normal_range": "18-80", "step": 1
            },
            "Sex": {
                "type": "select", "options": {"Male": 1, "Female": 0}, "default": 1,
                "label": "Sex", "description": "Biological sex"
            },
            "Steroid": {
                "type": "select", "options": {"No": 0, "Yes": 1}, "default": 0,
                "label": "Steroid Use", "description": "Is the patient using steroids?"
            },
            "Antivirals": {
                "type": "select", "options": {"No": 0, "Yes": 1}, "default": 0,
                "label": "Antiviral Treatment", "description": "On antiviral treatment?"
            },
            "Fatigue": {
                "type": "select", "options": {"No": 0, "Yes": 1}, "default": 0,
                "label": "Fatigue", "description": "Experiences fatigue?"
            },
            "Malaise": {
                "type": "select", "options": {"No": 0, "Yes": 1}, "default": 0,
                "label": "Malaise", "description": "General discomfort?"
            },
            "Anorexia": {
                "type": "select", "options": {"No": 0, "Yes": 1}, "default": 0,
                "label": "Anorexia", "description": "Loss of appetite?"
            },
            "Liver_Big": {
                "type": "select", "options": {"No": 0, "Yes": 1}, "default": 0,
                "label": "Enlarged Liver", "description": "Is the liver enlarged?"
            },
            "Liver_Firm": {
                "type": "select", "options": {"No": 0, "Yes": 1}, "default": 0,
                "label": "Firm Liver", "description": "Is the liver firm?"
            },
            "Spleen_Palpable": {
                "type": "select", "options": {"No": 0, "Yes": 1}, "default": 0,
                "label": "Spleen Palpable", "description": "Is the spleen palpable?"
            },
            "Spiders": {
                "type": "select", "options": {"No": 0, "Yes": 1}, "default": 0,
                "label": "Spider Angiomas", "description": "Spider angiomas on skin?"
            },
            "Ascites": {
                "type": "select", "options": {"No": 0, "Yes": 1}, "default": 0,
                "label": "Ascites", "description": "Fluid buildup in abdomen?"
            },
            "Varices": {
                "type": "select", "options": {"No": 0, "Yes": 1}, "default": 0,
                "label": "Varices", "description": "Enlarged veins?"
            },
            "Bilirubin": {
                "type": "float", "min": 0.3, "max": 8.0, "default": 1.0,
                "label": "Bilirubin (mg/dL)", "description": "Bilirubin level",
                "normal_range": "0.1-1.2 mg/dL", "step": 0.1
            },
            "Alk_Phosphate": {
                "type": "float", "min": 30.0, "max": 300.0, "default": 85.0,
                "label": "Alkaline Phosphatase (IU/L)", "description": "Alkaline phosphatase level",
                "normal_range": "44-147 IU/L", "step": 1.0
            },
            "Sgot": {
                "type": "float", "min": 10.0, "max": 650.0, "default": 30.0,
                "label": "SGOT / AST (IU/L)", "description": "SGOT enzyme level",
                "normal_range": "10-40 IU/L", "step": 1.0
            },
            "Albumin": {
                "type": "float", "min": 2.0, "max": 6.0, "default": 4.0,
                "label": "Albumin (g/dL)", "description": "Albumin level in blood",
                "normal_range": "3.5-5.5 g/dL", "step": 0.1
            },
            "Protime": {
                "type": "float", "min": 0.0, "max": 100.0, "default": 60.0,
                "label": "Prothrombin Time (%)", "description": "Prothrombin time",
                "normal_range": "70-100%", "step": 1.0
            },
            "Histology": {
                "type": "select", "options": {"No": 0, "Yes": 1}, "default": 0,
                "label": "Histology Done", "description": "Was histological exam done?"
            },
        },
    },
}


def get_feature_names(disease_key):
    """Get ordered list of feature names for a disease."""
    return list(DISEASES[disease_key]["features"].keys())


def get_numeric_features(disease_key):
    """Get feature names that are numeric (int or float) for a disease."""
    feats = DISEASES[disease_key]["features"]
    return [k for k, v in feats.items() if v["type"] in ("int", "float")]


def get_categorical_features(disease_key):
    """Get feature names that are categorical (select) for a disease."""
    feats = DISEASES[disease_key]["features"]
    return [k for k, v in feats.items() if v["type"] == "select"]
