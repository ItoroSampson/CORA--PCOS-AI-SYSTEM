import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def app():
    st.title("📊 Your Personalized Health Metrics")

    # 1. Retrieve Data from Memory (Session State)
    # Using .get() prevents the app from crashing if the user hasn't visited Tab 1 yet
    user_testo = st.session_state.get("user_testo", 30.0)
    user_afc = st.session_state.get("user_afc", 10)
    user_bmi = st.session_state.get("user_bmi", 22.0)

    plt.style.use("dark_background")
    sns.set_palette("husl")

    # --- CHART 1: Testosterone vs Clinical Threshold ---
    st.subheader("Testosterone Analysis")
    fig1, ax1 = plt.subplots(figsize=(8, 4))

    # Clinical "Normal" range for women is generally under 45-50 ng/dL
    threshold = 45.0
    categories = ["Your Level", "Clinical Threshold"]
    values = [user_testo, threshold]

    sns.barplot(
        x=categories,
        y=values,
        hue=categories,
        palette=["#00FFFF", "#FF00FF"],
        legend=False,
        ax=ax1,
    )
    ax1.axhline(threshold, ls="--", color="white", alpha=0.7)
    ax1.set_ylabel("ng/dL")
    st.pyplot(fig1)

    # --- CHART 2: Follicle Count Distribution ---
    st.subheader("Follicle Density Insight")
    # We create a distribution curve and show where the user sits
    fig2, ax2 = plt.subplots(figsize=(8, 4))

    # Simulated population data
    pop_data = np.random.normal(loc=12, scale=5, size=1000)
    sns.kdeplot(pop_data, fill=True, color="#00FF00", ax=ax2)

    # Draw a line for the user
    ax2.axvline(user_afc, color="red", lw=3, label="You")
    ax2.set_title(f"Your Follicle Count: {user_afc} (PCOS threshold is often >12)")
    ax2.legend()
    st.pyplot(fig2)

    # --- CHART 3: Metabolic Profile (BMI) ---
    st.subheader("BMI Categorization")
    fig3, ax3 = plt.subplots(figsize=(8, 2))
    # A simple horizontal gauge-style bar
    color = "#00FF00" if 18.5 <= user_bmi <= 24.9 else "#FF4500"
    ax3.barh(["BMI"], [user_bmi], color=color)
    ax3.set_xlim(0, 50)
    ax3.axvline(18.5, color="white", ls=":")
    ax3.axvline(24.9, color="white", ls=":")
    st.pyplot(fig3)

    st.write(
        f"**Quick Insight:** Based on your inputs, your testosterone is **{user_testo} ng/dL** and your BMI is **{user_bmi}**. These metrics are key drivers for the XGBoost model."
    )


if __name__ == "__main__":
    app()
