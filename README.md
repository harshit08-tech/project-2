# MediPredict AI 🏥

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange?style=for-the-badge&logo=scikit-learn)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?style=for-the-badge&logo=streamlit)

**MediPredict AI** is a professional-grade, multi-disease prediction system built using machine learning. It provides predictive analytics for 8 major medical conditions using user-inputted clinical and demographic data.

Designed for the **BCA-AI | 503 - Applied Artificial Intelligence** course.

---

## 🎯 Features

*   **8 Distinct Disease Models:** Predicts Diabetes, Heart Disease, Liver Disease, Kidney Disease, Breast Cancer, Parkinson's, Stroke, and Hepatitis.
*   **Stunning UI/UX:** Built with Streamlit, customized heavily with Glassmorphism, animations, CSS Grid, and custom color palettes for a premium SaaS feel.
*   **Robust Backend:** FastAPI serving serialized (pickle) scikit-learn models.
*   **Performance Dashboards:** Interactive Plotly charts evaluating model metrics across the board.
*   **Comprehensive Diagnostics:** Detailed feature descriptions and normal ranges to guide data entry.

---

## 🏗️ Architecture

```text
MediPredict AI Platform
│
├── Frontend (Streamlit)
│   ├── User Interface & Data Entry
│   ├── Beautiful Visualizations & Dashboards
│   └── API Client HTTP Handler
│
└── Backend (FastAPI)
    ├── REST API Endpoints (/predict/{disease})
    ├── Scikit-Learn Model Loading (Pickle)
    └── Data Scaling & Inference Engine
```

---

## 💻 Tech Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Language** | Python | Core programming language |
| **Frontend** | Streamlit + Custom CSS | UI components, pages, dashboard |
| **Backend** | FastAPI, Uvicorn | RESTful API server |
| **Machine Learning** | Scikit-Learn | Training Random Forest, SVM, etc. |
| **Data Processing** | Pandas, NumPy | Data manipulation and scaling |
| **Visualizations** | Plotly | Radar charts, gauge meters |

---

## 🚀 Installation & Usage

1. **Clone & Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Generate Datasets** (If not already present)
   ```bash
   python src/data_generator.py
   ```

3. **Train Machine Learning Models**
   ```bash
   python src/train_models.py
   ```

4. **Start the FastAPI Backend**
   ```bash
   uvicorn api.main:app --reload
   ```

5. **Launch the Streamlit Frontend** (Open a new terminal)
   ```bash
   streamlit run streamlit_app/app.py
   ```

---

## 🩺 Supported Diseases

1. **Diabetes Mellitus**: Analyzes glucose, BMI, insulin, etc.
2. **Heart Disease**: Analyzes cholesterol, ECG, resting BP.
3. **Liver Disease**: Analyzes bilirubin, AST, ALT, albumin.
4. **Chronic Kidney Disease**: Analyzes creatinine, hemoglobin, specific gravity.
5. **Breast Cancer**: Analyzes FNA cell nuclei geometry (radius, texture, concavity).
6. **Parkinson's Disease**: Analyzes biomedical voice measurements (jitter, shimmer, HNR).
7. **Stroke Risk**: Analyzes lifestyle, age, hypertension, glucose.
8. **Hepatitis**: Analyzes liver function and clinical findings.

---

## 👨‍💻 Team

*   **Harshit** - ML Engineer & Team Lead
*   **Shorya** - Backend Developer & Data Analyst
*   **Tanisha** - Frontend Developer & UI/UX Designer

---

## ⚠️ AI Disclaimer

**IMPORTANT NOTICE:** This system is NOT a certified medical professional. It is an AI-powered tool that provides predictions based on statistical data analysis and machine learning algorithms. These predictions should NOT be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare provider for any medical decisions. The developers of this system are not responsible for any actions taken based on the predictions provided.

---

## 📄 License
MIT License. Copyright (c) 2026 MediPredict AI Team.
