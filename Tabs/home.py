import streamlit as st
import PIL


def app():
    st.title("CORA")
    st.image("./images/PCOS.png/2.png")

    st.markdown("🩸 What is PCOS?")

    st.write("""
    Polycystic Ovary Syndrome (PCOS) is a common hormonal disorder that affects women during their reproductive years. 
    It occurs when an imbalance in reproductive hormones—primarily high levels of androgens ("male" hormones) and insulin—leads to problems in the ovaries.
    """)

    st.markdown("### :muscle: Managing the Condition")
    st.write("""
    There is currently no permanent cure for PCOS, but it is highly manageable. **Lifestyle modifications**, 
    such as maintaining a balanced diet, regular physical activity, and weight management, are the first line of treatment. 
    Early intervention can significantly reduce the risk of long-term complications like **Type 2 Diabetes**, **hypertension**, and **infertility**.
    """)

    st.markdown("### :computer: About This App")
    st.write("""
    This Web app helps you assess the likelihood of having PCOS by analyzing key symptoms and health metrics 
    (such as cycle regularity, BMI, and physical signs). By using a **XGBOOST** trained on clinical data, 
    the app identifies patterns that might be missed in a casual check-up, providing an early risk assessment to empower your healthcare journey.
    """)
