import streamlit as st
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from config import TEAM_MEMBERS, DISCLAIMER, COLORS
from streamlit_app.utils.ui_components import load_css, render_page_header, render_team_member

st.set_page_config(page_title='About | MediPredict AI', page_icon='ℹ️', layout='wide')
load_css()
render_page_header("About Project", "Discover the technology and team behind MediPredict AI.", "ℹ️")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown('<h3><span class="gradient-text">Project Overview</span></h3>', unsafe_allow_html=True)
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("""
    <p style="color: #F1F5F9; font-size: 1.05rem; line-height: 1.6;">
    <strong style="color: #6366F1;">MediPredict AI</strong> is a comprehensive Multi-Disease Prediction System developed for the course <strong>BCA-AI | 503 - Applied Artificial Intelligence</strong>.
    </p>
    <p style="color: #CBD5E1; font-size: 1rem; line-height: 1.6;">
    The system utilizes state-of-the-art machine learning algorithms (including Random Forest, SVM, Logistic Regression, KNN, and Gradient Boosting) trained on thousands of clinical dataset records to evaluate risk across 8 major medical conditions:
    </p>
    <ul style="color: #F1F5F9; font-size: 1rem; line-height: 1.8;">
        <li>🩸 <strong>Diabetes Mellitus</strong></li>
        <li>❤️ <strong>Heart Disease</strong></li>
        <li>🫁 <strong>Liver Disease</strong></li>
        <li>🫘 <strong>Chronic Kidney Disease</strong></li>
        <li>🎗️ <strong>Breast Cancer</strong></li>
        <li>🧠 <strong>Parkinson's Disease</strong></li>
        <li>🧠 <strong>Stroke Risk</strong></li>
        <li>🦠 <strong>Hepatitis</strong></li>
    </ul>
    <p style="color: #CBD5E1; font-size: 1rem; line-height: 1.6;">
    The system features a decoupled architecture with a modern Streamlit frontend and high-performance FastAPI microservice backend.
    </p>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<h3><span class="gradient-text">System Architecture</span></h3>', unsafe_allow_html=True)
    st.markdown('<div class="glass-card" style="text-align: center;">', unsafe_allow_html=True)
    
    arch_html = f"""
    <div style="display: flex; flex-direction: column; gap: 20px; align-items: center; padding: 20px;">
        <div style="background: linear-gradient(135deg, #4F46E5, #6366F1); color: white; padding: 16px 32px; border-radius: 12px; font-weight: 700; font-size: 1.1rem; width: 340px; box-shadow: 0 4px 14px rgba(79, 70, 229, 0.4);">
            🧑‍⚕️ User Interface (Streamlit)
        </div>
        <div style="font-size: 26px; color: #22D3EE; font-weight: bold;">⬇️ HTTP JSON REST API</div>
        <div style="background: #334155; border: 2px solid #06B6D4; color: white; padding: 16px 32px; border-radius: 12px; font-weight: 700; font-size: 1.1rem; width: 340px; box-shadow: 0 4px 14px rgba(6, 182, 212, 0.3);">
            🚀 API Microservice (FastAPI)
        </div>
        <div style="font-size: 26px; color: #34D399; font-weight: bold;">⬇️ Preprocessing & Inference</div>
        <div style="background: linear-gradient(135deg, #059669, #10B981); color: white; padding: 16px 32px; border-radius: 12px; font-weight: 700; font-size: 1.1rem; width: 340px; box-shadow: 0 4px 14px rgba(16, 185, 129, 0.4);">
            🧠 ML Models (Scikit-Learn Pickles)
        </div>
    </div>
    """
    st.markdown(arch_html, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<h3><span class="gradient-text">Project Team</span></h3>', unsafe_allow_html=True)
    for member in TEAM_MEMBERS:
        render_team_member(member)
        
    st.markdown('<br/>', unsafe_allow_html=True)
    st.markdown('<h3><span class="gradient-text">Tech Stack</span></h3>', unsafe_allow_html=True)
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("""
    <ul style="color: #F1F5F9; font-size: 1.05rem; line-height: 2.0; list-style: none; padding-left: 0;">
        <li>🐍 <strong style="color:#6366F1;">Python 3.10+</strong></li>
        <li>🤖 <strong style="color:#22D3EE;">Scikit-Learn</strong> (ML Models)</li>
        <li>⚡ <strong style="color:#34D399;">FastAPI & Uvicorn</strong> (Backend)</li>
        <li>🎨 <strong style="color:#FBBF24;">Streamlit</strong> (Frontend UI)</li>
        <li>📊 <strong style="color:#F87171;">Plotly & Pandas</strong> (Data Vis)</li>
        <li>🗃️ <strong style="color:#A78BFA;">Pickle & Joblib</strong> (Serialization)</li>
    </ul>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Full Disclaimer at the bottom
st.markdown("---")
st.markdown('<h3><span style="color: #F87171;">Legal & Medical Notice</span></h3>', unsafe_allow_html=True)
st.warning(DISCLAIMER)
