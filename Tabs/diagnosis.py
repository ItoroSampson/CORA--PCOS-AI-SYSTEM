import streamlit as st
import numpy as np
from web_functions import predict_pcos
from fpdf import FPDF
from datetime import datetime
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# API Setup
GROQ_API_KEY = st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")

if GROQ_API_KEY:
    groq_client = OpenAI(
        base_url="https://api.groq.com/openai/v1", api_key=GROQ_API_KEY
    )
else:
    groq_client = None


def app(df, X, y, model, model_score):
    st.markdown(
        """
        <style>
        .stTabs [data-baseweb="tab-list"] button p { font-size: 20px; color: #008080; }
        </style>
    """,
        unsafe_allow_html=True,
    )

    tab1, tab2, tab3 = st.tabs(["Diagnosis 🩺", "Medication 💊", "Data Source 🛢️"])

    with tab1:
        st.title("PCOS Risk Assessment")
        col1, col2 = st.columns(2)
        with col1:
            age = st.slider("Age", 15, 50, 25)
            bmi = st.slider("BMI", 10.0, 50.0, 22.0)
            menstrual_irregularity = st.selectbox(
                "Menstrual Irregularity (0=No, 1=Yes)", [0, 1]
            )
        with col2:
            testosterone = st.slider("Testosterone (ng/dL)", 5.0, 100.0, 35.0)
            follicle_count = st.slider("Antral Follicle Count", 0, 40, 10)

        features = np.array(
            [[age, menstrual_irregularity, testosterone, follicle_count]]
        )

        if st.button("Run Diagnostic"):
            prediction, prob_score = predict_pcos(model, features)
            final_score = min(
                prob_score[0] + 0.15, 1.0
            )  # Ensure it doesn't exceed 100%

            if final_score > 0.7:
                pcos_risk_label = "HIGH PROBABILITY OF PCOS"
                st.error(f"Assessment: {pcos_risk_label}")
            elif final_score > 0.4:
                pcos_risk_label = "MODERATE PROBABILITY OF PCOS"
                st.warning(f"Assessment: {pcos_risk_label}")
            else:
                pcos_risk_label = "LOW PROBABILITY"
                st.success(f"Assessment: {pcos_risk_label}")

            # Store in session state
            st.session_state["prediction_result"] = pcos_risk_label
            st.session_state["user_age"] = age
            st.session_state["user_bmi"] = bmi

    with tab2:
        st.title("Supportive Recommendations")

        if "prediction_result" in st.session_state:
            if st.button("Get Personalized Advice from Cora"):
                if not groq_client:
                    st.error(
                        "API Key missing! Please add GROQ_API_KEY to secrets.toml or .env"
                    )
                else:
                    with st.spinner("Cora is thinking..."):
                        prompt = f"""
                        You are 'Cora', a specialized medical AI assistant for PCOS (Polycystic Ovary Syndrome).
                        
                        Patient Information:
                        - Risk Level: {st.session_state["prediction_result"]}
                        - Age: {st.session_state["user_age"]}
                        - BMI: {st.session_state["user_bmi"]}
                        
                        Provide personalized recommendations including:
                        1. Lifestyle modifications
                        2. Dietary suggestions  
                        3. When to consult a doctor
                        4. Follow-up tests to consider
                        
                        Keep recommendations practical, supportive, and medically sound.
                        Always include a brief disclaimer.
                        """
                        try:
                            response = groq_client.chat.completions.create(
                                model="llama-3.1-8b",
                                messages=[
                                    {
                                        "role": "system",
                                        "content": "You are Cora, a PCOS medical assistant.",
                                    },
                                    {"role": "user", "content": prompt},
                                ],
                                temperature=0.7,
                                max_tokens=1000,
                            )
                            st.markdown(response.choices[0].message.content)

                            st.caption(
                                "⚠️ This information is for educational purposes only. Always consult with a healthcare provider."
                            )

                        except Exception as e:
                            st.error(f"AI Error: {str(e)}")
        else:
            st.info("Run Diagnosis in Tab 1 first.")

    with tab3:
        st.title("Data Insights")
        st.dataframe(df.head())
