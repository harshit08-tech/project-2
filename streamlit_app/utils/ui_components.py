import streamlit as st
import os
import sys
import plotly.graph_objects as go

# Add project root to sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from config import *

def load_css():
    """Loads the custom CSS file."""
    css_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "styles", "custom.css")
    with open(css_file, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def render_disclaimer():
    """Renders the AI disclaimer banner with pulsing animation."""
    html = f"""
    <div class="disclaimer-banner">
        <div class="disclaimer-icon">⚠️</div>
        <div class="disclaimer-text">
            <strong>IMPORTANT NOTICE:</strong><br/>
            {DISCLAIMER}
        </div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

def render_metric_card(title, value, icon="", color=COLORS["primary"]):
    """Renders a glassmorphism metric card."""
    html = f"""
    <div class="metric-card" style="border-top-color: {color};">
        <div class="metric-title">{icon} {title}</div>
        <div class="metric-value" style="color: #FFFFFF !important;">{value}</div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

def render_disease_card(disease_key, disease_info):
    """Renders a disease card with gradient background and hover scale transform."""
    html = f"""
    <div class="disease-card" style="background: {disease_info['gradient']};">
        <div class="disease-icon">{disease_info['icon']}</div>
        <div class="disease-title">{disease_info['name']}</div>
        <div class="disease-desc">{disease_info['description']}</div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

def render_risk_gauge(risk_level, confidence):
    """Renders a Plotly gauge chart showing risk level."""
    val = confidence if risk_level == 1 else 100 - confidence
    color = COLORS["danger"] if risk_level == 1 else COLORS["success"]
    
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = val,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "AI Risk Probability", 'font': {'color': '#FFFFFF', 'size': 20, 'family': 'Poppins'}},
        number = {'suffix': "%", 'font': {'color': color, 'family': 'Poppins', 'weight': 'bold'}},
        gauge = {
            'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': '#CBD5E1', 'tickfont': {'color': '#F1F5F9'}},
            'bar': {'color': color},
            'bgcolor': COLORS['surface'],
            'borderwidth': 2,
            'bordercolor': COLORS['border'],
            'steps': [
                {'range': [0, 30], 'color': 'rgba(16, 185, 129, 0.3)'},
                {'range': [30, 70], 'color': 'rgba(245, 158, 11, 0.3)'},
                {'range': [70, 100], 'color': 'rgba(239, 68, 68, 0.3)'}
            ],
            'threshold': {
                'line': {'color': "#FFFFFF", 'width': 4},
                'thickness': 0.75,
                'value': val
            }
        }
    ))
    
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font={'color': '#F1F5F9', 'family': 'Inter'},
        margin=dict(l=20, r=20, t=50, b=20),
        height=300
    )
    
    return fig

def render_prediction_result(result, disease_info):
    """Renders the full prediction result with risk gauge, label, recommendations."""
    risk_level = result.get('prediction', 0)
    confidence = result.get('confidence', 0.0) * 100
    
    is_high_risk = risk_level == 1
    card_class = "result-high" if is_high_risk else "result-low"
    label = disease_info['positive_label'] if is_high_risk else disease_info['negative_label']
    
    html = f"""
    <div class="glass-card result-card {card_class}">
        <div class="result-label">{label}</div>
        <div class="confidence-meter">AI Confidence Level: {confidence:.1f}%</div>
    """
    
    if is_high_risk:
        html += f"<p style='color: #CBD5E1; font-size: 1.05rem;'>Based on the parameters provided, the model has identified patterns consistent with <strong>{disease_info['name']}</strong>. Please consult a healthcare professional for a formal diagnosis and medical advice.</p>"
    else:
        html += f"<p style='color: #CBD5E1; font-size: 1.05rem;'>The parameters provided do not currently indicate a high risk for <strong>{disease_info['name']}</strong>. Maintain a healthy lifestyle and continue routine checkups.</p>"
        
    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)
    
    st.plotly_chart(render_risk_gauge(risk_level, confidence), use_container_width=True)

def render_page_header(title, subtitle, icon=""):
    """Renders a styled page header with gradient text."""
    html = f"""
    <div class="page-header">
        <h1 class="page-title">{icon} <span class="gradient-text">{title}</span></h1>
        <div class="page-subtitle">{subtitle}</div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

def render_team_member(member):
    """Renders a team member card."""
    html = f"""
    <div class="team-member">
        <div class="member-icon">{member['icon']}</div>
        <div class="member-name">{member['name']}</div>
        <div class="member-role">{member['role']}</div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)
