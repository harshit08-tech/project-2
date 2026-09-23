import streamlit as st
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from config import DISEASES
from streamlit_app.utils.ui_components import load_css, render_disclaimer, render_page_header, render_prediction_result
from streamlit_app.utils.api_client import predict_disease

st.set_page_config(page_title='Predict | MediPredict AI', page_icon='🩺', layout='wide')
load_css()
render_disclaimer()
render_page_header("Medical Prediction", "Select a condition and enter patient data to get an AI-powered risk assessment.", "🩺")

# Initialize session state variables
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'selected_disease' not in st.session_state:
    st.session_state.selected_disease = None
if 'patient_info' not in st.session_state:
    st.session_state.patient_info = {}

# Layout: Sidebar for progress
with st.sidebar:
    st.markdown("### Assessment Progress")
    st.markdown(f"{'✅' if st.session_state.step > 1 else '🔵'} **Step 1:** Select Disease")
    st.markdown(f"{'✅' if st.session_state.step > 2 else '🔵' if st.session_state.step == 2 else '⚪'} **Step 2:** Patient Details")
    st.markdown(f"{'✅' if st.session_state.step > 3 else '🔵' if st.session_state.step == 3 else '⚪'} **Step 3:** Medical Parameters")
    st.markdown(f"{'✅' if st.session_state.step > 4 else '🔵' if st.session_state.step == 4 else '⚪'} **Step 4:** Results")
    
    if st.session_state.step > 1:
        st.markdown("---")
        if st.button("🔄 Start Over", use_container_width=True):
            st.session_state.step = 1
            st.session_state.selected_disease = None
            st.rerun()

# STEP 1: Disease Selection
if st.session_state.step == 1:
    st.markdown('<h3><span class="gradient-text">Step 1: Select Condition</span></h3>', unsafe_allow_html=True)
    st.markdown("<p style='color: #CBD5E1; font-size: 1.05rem; font-weight: 500; margin-bottom: 20px;'>Choose the specific medical condition for risk assessment.</p>", unsafe_allow_html=True)
    
    cols = st.columns(4)
    for i, (key, info) in enumerate(DISEASES.items()):
        with cols[i % 4]:
            if st.button(f"{info['icon']} Select {info['name']}", key=f"btn_{key}", use_container_width=True):
                st.session_state.selected_disease = key
                st.session_state.step = 2
                st.rerun()
            
            html = f"""
            <div class="disease-card" style="background: {info['gradient']}; height: 180px; margin-bottom: 25px; margin-top: 10px; cursor: default;">
                <div class="disease-icon" style="font-size: 2.5rem;">{info['icon']}</div>
                <div class="disease-title" style="font-size: 1.15rem;">{info['name']}</div>
                <div class="disease-desc" style="font-size: 0.82rem; color: #FFFFFF !important;">{info['description'][:75]}...</div>
            </div>
            """
            st.markdown(html, unsafe_allow_html=True)

# STEP 2: Patient Details Form
elif st.session_state.step == 2:
    disease_key = st.session_state.selected_disease
    disease_name = DISEASES[disease_key]["name"] if disease_key else "Condition"
    
    st.markdown(f'<h3><span class="gradient-text">Step 2: Patient Details ({disease_name})</span></h3>', unsafe_allow_html=True)
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    
    with st.form("patient_details_form"):
        col1, col2 = st.columns(2)
        with col1:
            full_name = st.text_input("Full Name", placeholder="e.g. John Doe")
            age = st.number_input("Age (Years)", min_value=1, max_value=120, value=30)
            contact = st.text_input("Contact Number (Optional)", placeholder="+1 234 567 8900")
            smoking = st.selectbox("Smoking Status", ["Never", "Former", "Current"])
            
        with col2:
            gender = st.selectbox("Gender", ["Male", "Female", "Other"])
            blood_group = st.selectbox("Blood Group", ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"])
            medical_history = st.text_area("Medical History (Optional)", placeholder="Any existing conditions...")
            exercise = st.selectbox("Exercise Frequency", ["Rarely", "1-2 times/week", "3-4 times/week", "5+ times/week"])
            
        st.markdown("<br/>", unsafe_allow_html=True)
        submit_details = st.form_submit_button("Continue to Parameters ➡️")
        if submit_details:
            if not full_name:
                st.error("Please enter the patient's full name.")
            else:
                st.session_state.patient_info = {
                    "Name": full_name, "Age": age, "Gender": gender, "Blood Group": blood_group,
                    "Contact": contact, "Medical History": medical_history,
                    "Smoking": smoking, "Exercise": exercise
                }
                st.session_state.step = 3
                st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# STEP 3: Disease Specific Parameters
elif st.session_state.step == 3:
    disease_key = st.session_state.selected_disease
    disease_info = DISEASES[disease_key]
    features = disease_info["features"]
    
    st.markdown(f'<h3><span class="gradient-text">Step 3: Clinical Parameters for {disease_info["name"]}</span></h3>', unsafe_allow_html=True)
    st.markdown("<p style='color: #CBD5E1; font-size: 1.05rem; font-weight: 500;'>Enter the specific biomarker readings. Hover over input field labels for descriptions and normal ranges.</p>", unsafe_allow_html=True)
    
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    
    with st.form("clinical_parameters_form"):
        feature_keys = list(features.keys())
        cols = st.columns(3)
        input_data = {}
        
        for i, key in enumerate(feature_keys):
            feat = features[key]
            with cols[i % 3]:
                help_text = f"Normal Range: {feat.get('normal_range', 'N/A')}\n\n{feat['description']}"
                
                if feat["type"] == "int":
                    input_data[key] = st.number_input(
                        feat["label"], 
                        min_value=int(feat["min"]), max_value=int(feat["max"]), 
                        value=int(feat["default"]), step=int(feat.get("step", 1)),
                        help=help_text
                    )
                elif feat["type"] == "float":
                    input_data[key] = st.number_input(
                        feat["label"], 
                        min_value=float(feat["min"]), max_value=float(feat["max"]), 
                        value=float(feat["default"]), step=float(feat.get("step", 0.1)),
                        help=help_text
                    )
                elif feat["type"] == "select":
                    options_list = list(feat["options"].keys())
                    default_idx = 0
                    for idx, (k, v) in enumerate(feat["options"].items()):
                        if v == feat["default"]:
                            default_idx = idx
                            break
                    
                    selected_opt = st.selectbox(feat["label"], options=options_list, index=default_idx, help=feat["description"])
                    input_data[key] = feat["options"][selected_opt]
                    
        st.markdown("<br/>", unsafe_allow_html=True)
        submit_predict = st.form_submit_button("Run AI Prediction 🚀", use_container_width=True)
        
        if submit_predict:
            st.session_state.input_data = input_data
            st.session_state.step = 4
            st.rerun()
            
    st.markdown('</div>', unsafe_allow_html=True)

# STEP 4: Results
elif st.session_state.step == 4:
    disease_key = st.session_state.selected_disease
    disease_info = DISEASES[disease_key]
    
    st.markdown(f'<h3><span class="gradient-text">Step 4: AI Risk Assessment Results ({disease_info["name"]})</span></h3>', unsafe_allow_html=True)
    
    with st.expander("Patient Summary (Click to expand)"):
        p_info = st.session_state.patient_info
        st.write(f"**Name:** {p_info.get('Name', 'N/A')} | **Age:** {p_info.get('Age', 'N/A')} | **Gender:** {p_info.get('Gender', 'N/A')} | **Blood Group:** {p_info.get('Blood Group', 'N/A')}")
    
    with st.spinner("Analyzing parameters with machine learning models..."):
        result = predict_disease(disease_key, st.session_state.input_data)
        
        if "error" in result:
            st.error(result["error"])
            st.info("Ensure the FastAPI backend is running via `python -m uvicorn api.main:app --host 127.0.0.1 --port 8000`")
        else:
            render_prediction_result(result, disease_info)
            
    st.markdown("<br/>", unsafe_allow_html=True)
    if st.button("🔄 Start New Assessment", use_container_width=True):
        st.session_state.step = 1
        st.session_state.selected_disease = None
        st.rerun()
