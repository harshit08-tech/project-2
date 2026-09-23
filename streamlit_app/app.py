import streamlit as st
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import DISEASES, DISCLAIMER_SHORT
from streamlit_app.utils.ui_components import load_css

st.set_page_config(
    page_title='MediPredict AI | Multi-Disease Prediction',
    page_icon='🏥',
    layout='wide',
    initial_sidebar_state='expanded'
)

# Load CSS
load_css()

# Sidebar
with st.sidebar:
    st.markdown('<h2 style="text-align: center;"><span class="gradient-text">MediPredict AI</span> 🏥</h2>', unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("### Quick Links")
    st.page_link("app.py", label="Home", icon="🏠")
    st.page_link("pages/1_🩺_Predict.py", label="Predict Disease", icon="🩺")
    st.page_link("pages/2_📊_Dashboard.py", label="Model Dashboard", icon="📊")
    st.page_link("pages/3_ℹ️_About.py", label="About Project", icon="ℹ️")

    st.markdown("---")
    st.markdown("### Disease Models")
    for key, info in DISEASES.items():
        st.markdown(f"- {info['icon']} **{info['name']}**")

    st.markdown(f'<div class="sidebar-disclaimer">{DISCLAIMER_SHORT}</div>', unsafe_allow_html=True)

# Scrolling Announcement Ticker
st.markdown("""
<div style="
    background: linear-gradient(90deg, #4F46E5, #06B6D4, #10B981, #F59E0B, #EF4444, #4F46E5);
    background-size: 300% 100%;
    animation: tickerGradient 6s linear infinite;
    padding: 10px 0;
    border-radius: 12px;
    margin-bottom: 20px;
    overflow: hidden;
    border: 1px solid rgba(255,255,255,0.15);
    box-shadow: 0 4px 20px rgba(79, 70, 229, 0.3);
">
<style>
@keyframes tickerGradient {
    0% { background-position: 0% 50%; }
    100% { background-position: 300% 50%; }
}
@keyframes scrollTicker {
    0% { transform: translateX(100%); }
    100% { transform: translateX(-100%); }
}
</style>
<div style="
    display: flex;
    white-space: nowrap;
    animation: scrollTicker 20s linear infinite;
    font-family: 'Poppins', sans-serif;
    font-size: 0.95rem;
    font-weight: 700;
    color: #FFFFFF;
    letter-spacing: 0.03em;
    text-shadow: 0 1px 3px rgba(0,0,0,0.4);
">
    🏥 MediPredict AI — 8 Disease Models &nbsp;&nbsp;|&nbsp;&nbsp;
    🎯 96%+ Average Accuracy &nbsp;&nbsp;|&nbsp;&nbsp;
    🧠 40 ML Algorithms Trained &nbsp;&nbsp;|&nbsp;&nbsp;
    ⚡ Real-time Predictions in &lt;2 seconds &nbsp;&nbsp;|&nbsp;&nbsp;
    📊 Powered by Scikit-Learn, FastAPI &amp; Streamlit &nbsp;&nbsp;|&nbsp;&nbsp;
    👥 Built by Harshit, Shorya &amp; Tanisha &nbsp;&nbsp;|&nbsp;&nbsp;
    ⚠️ AI Tool — Not a Certified Doctor &nbsp;&nbsp;|&nbsp;&nbsp;
    🏥 MediPredict AI — 8 Disease Models &nbsp;&nbsp;|&nbsp;&nbsp;
    🎯 96%+ Average Accuracy &nbsp;&nbsp;|&nbsp;&nbsp;
    🧠 40 ML Algorithms Trained
</div>
</div>
""", unsafe_allow_html=True)

# Feature Highlights Bar
st.markdown("""
<div style="
    display: flex;
    justify-content: center;
    gap: 16px;
    flex-wrap: wrap;
    margin-bottom: 24px;
">
    <div style="background: rgba(79, 70, 229, 0.15); border: 1px solid rgba(79, 70, 229, 0.4); padding: 8px 18px; border-radius: 30px; display: flex; align-items: center; gap: 8px;">
        <span style="font-size: 1.1rem;">🔬</span>
        <span style="color: #C4B5FD; font-weight: 600; font-size: 0.85rem; font-family: 'Poppins', sans-serif;">AI-Powered Diagnostics</span>
    </div>
    <div style="background: rgba(6, 182, 212, 0.15); border: 1px solid rgba(6, 182, 212, 0.4); padding: 8px 18px; border-radius: 30px; display: flex; align-items: center; gap: 8px;">
        <span style="font-size: 1.1rem;">🛡️</span>
        <span style="color: #67E8F9; font-weight: 600; font-size: 0.85rem; font-family: 'Poppins', sans-serif;">Privacy First</span>
    </div>
    <div style="background: rgba(16, 185, 129, 0.15); border: 1px solid rgba(16, 185, 129, 0.4); padding: 8px 18px; border-radius: 30px; display: flex; align-items: center; gap: 8px;">
        <span style="font-size: 1.1rem;">📋</span>
        <span style="color: #6EE7B7; font-weight: 600; font-size: 0.85rem; font-family: 'Poppins', sans-serif;">Detailed Risk Reports</span>
    </div>
    <div style="background: rgba(245, 158, 11, 0.15); border: 1px solid rgba(245, 158, 11, 0.4); padding: 8px 18px; border-radius: 30px; display: flex; align-items: center; gap: 8px;">
        <span style="font-size: 1.1rem;">⚡</span>
        <span style="color: #FCD34D; font-weight: 600; font-size: 0.85rem; font-family: 'Poppins', sans-serif;">Instant Results</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Main Content Hero Section
st.markdown('<div class="animated-bg" style="padding: 60px 20px; border-radius: 24px; text-align: center; margin-bottom: 40px; border: 1px solid rgba(255,255,255,0.15); box-shadow: 0 20px 40px rgba(0,0,0,0.5);">', unsafe_allow_html=True)
st.markdown('<h1 style="font-size: 3.5rem; margin-bottom: 20px; color: #FFFFFF;">Welcome to <span class="gradient-text">MediPredict AI</span></h1>', unsafe_allow_html=True)
st.markdown('<p style="font-size: 1.25rem; color: #E2E8F0; max-width: 820px; margin: 0 auto; line-height: 1.6; font-weight: 500;">An advanced, machine-learning powered diagnostic assistant predicting 8 different conditions with high accuracy using multi-parameter health analysis.</p>', unsafe_allow_html=True)
st.markdown('<br/><br/><a href="/Predict" target="_self" class="start-assessment-btn">Start Assessment 🚀</a>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<h3><span class="gradient-text">Supported Disease Prediction Models</span></h3>', unsafe_allow_html=True)
st.markdown('<br/>', unsafe_allow_html=True)

# Grid layout for diseases
cols = st.columns(4)
disease_items = list(DISEASES.items())

for i, (key, info) in enumerate(disease_items):
    with cols[i % 4]:
        html = f"""
        <a href="/Predict" target="_self" style="text-decoration: none;">
            <div class="disease-card" style="background: {info['gradient']}; height: 250px; margin-bottom: 20px;">
                <div class="disease-icon">{info['icon']}</div>
                <div class="disease-title">{info['name']}</div>
                <div class="disease-desc">{info['description']}</div>
            </div>
        </a>
        """
        st.markdown(html, unsafe_allow_html=True)

st.markdown('<br/>', unsafe_allow_html=True)

# Stats Section
st.markdown('<h3><span class="gradient-text">System Capabilities</span></h3>', unsafe_allow_html=True)
st.markdown('<br/>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown('<div class="glass-card" style="text-align:center;"><h2 style="font-size:2.8rem; color:#818CF8; margin:0; font-weight:800;">8</h2><p style="color:#CBD5E1; margin:5px 0 0 0; font-weight:600;">Disease Models</p></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="glass-card" style="text-align:center;"><h2 style="font-size:2.8rem; color:#22D3EE; margin:0; font-weight:800;">90+</h2><p style="color:#CBD5E1; margin:5px 0 0 0; font-weight:600;">Biomarkers Analyzed</p></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="glass-card" style="text-align:center;"><h2 style="font-size:2.8rem; color:#34D399; margin:0; font-weight:800;">High</h2><p style="color:#CBD5E1; margin:5px 0 0 0; font-weight:600;">Prediction Accuracy</p></div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div class="glass-card" style="text-align:center;"><h2 style="font-size:2.8rem; color:#FBBF24; margin:0; font-weight:800;">&lt;2s</h2><p style="color:#CBD5E1; margin:5px 0 0 0; font-weight:600;">Inference Time</p></div>', unsafe_allow_html=True)
