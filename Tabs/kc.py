import streamlit as st
import os

IMAGE_DIR = os.path.join("images", "PCOS.png")


def app():
    st.markdown(
        """<h1 style="text-align: center; color: #008080;">Knowledge Centre</h1>""",
        unsafe_allow_html=True,
    )

    # Paragraph 1: PCOS Detection using XGBoost
    col1, col2 = st.columns([1, 2])
    with col1:
        img1 = os.path.join(IMAGE_DIR, "1.png")
        # Note: Ensure you have a relevant image in your /images/ folder
        st.image(img1, caption="PCOS Risk Assessment", width=200)
    with col2:
        st.markdown("""
            ### Advanced Risk Detection
            Our PCOS assessment system is powered by **XGBoost**, a state-of-the-art gradient boosting algorithm known for its precision in medical data analysis. By evaluating key biomarkers—such as cycle regularity, BMI, and physical indicators like hirsutism and acne—the system identifies subtle patterns indicative of hormonal imbalances. Unlike traditional methods, this data-driven approach allows for an objective risk score, helping users identify potential issues before they escalate.
        """)

    # Paragraph 2: Holistic Recommendations
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
            ### Personalised Wellness Paths
            Beyond detection, the platform offers guidance tailored to the metabolic and hormonal profile of the user. This includes insulin-sensitising dietary suggestions, anti-inflammatory lifestyle habits, and targeted exercise routines. The system focuses on **root-cause management**, empowering users to take charge of their endocrine health through actionable, science-based insights.
        """)
    with col2:
        img2 = os.path.join(IMAGE_DIR, "2.png")
        st.image(img2, caption="Lifestyle Guidance", width=200)

    # Paragraph 3: Cora Chatbot (Formerly Capsule)
    col1, col2 = st.columns([1, 2])
    with col1:
        img3 = os.path.join(IMAGE_DIR, "3.png")
        st.image(img3, caption="Cora: Your AI Companion", width=200)
    with col2:
        st.markdown("""
            ### Meet Cora
            **Cora** is your intelligent health companion. Equipped with a deep understanding of Polycystic Ovary Syndrome, Cora uses Natural Language Processing (NLP) to answer questions about symptoms, lab results, and emotional well-being. Whether you’re curious about the 'Rotterdam Criteria' or need tips for managing hormonal breakouts, Cora is available 24/7 to provide supportive, easy-to-understand information.
        """)

    # Paragraph 4: Reproductive Health Trends
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
            ### Global Health Insights
            The **Trend** module provides a birds-eye view of reproductive health data worldwide. By visualizing the prevalence of PCOS across different demographics and regions, users and researchers can see the broader impact of this condition. Through interactive charts and heatmaps, Trend highlights how lifestyle factors and environmental variables correlate with hormonal health trends in 2026.
        """)
    with col2:
        img4 = os.path.join(IMAGE_DIR, "4.png")
        st.image(img4, caption="Hormonal Trends", width=200)

    # Paragraph 5: Modern Architecture
    col1, col2 = st.columns([1, 2])
    with col1:
        img5 = os.path.join(IMAGE_DIR, "5.png")
        st.image(img5, caption="Streamlit Power", width=200)
    with col2:
        st.markdown("""
            ### Seamless Experience
            Built on the **Streamlit** framework, this application merges high-performance Python backends with an intuitive interface. By integrating the speed of **XGBoost** with the conversational power of AI, we’ve created a seamless bridge between complex medical data and user-friendly health management. This platform is designed to be accessible, secure, and responsive across all devices.
        """)


if __name__ == "__main__":
    app()
