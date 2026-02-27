import streamlit as st
from web_functions import load_data, train_model
from Tabs import diagnosis, home, result, kc, talk2doc
import joblib
from pathlib import Path

st.set_page_config(
    page_title="CORA",
    page_icon="🌸",
    layout="wide",
)

# --- 1. DATA & MODEL LOADING ---
df, X, y = load_data()


@st.cache_resource
def get_model():
    model_path = Path("Models/pcos_model.pkl")
    if model_path.exists():
        return joblib.load(model_path), 0.95  # Mock score for loaded model
    else:
        return train_model(X, y)


model, model_score = get_model()

# --- 2. NAVIGATION ---
Tabs = {
    "Home": home,
    "Ask Queries": talk2doc,
    "Diagnosis": diagnosis,
    "Result": result,
    "Knowledge Center": kc,
}

st.sidebar.title("Navigation")
page = st.sidebar.radio("Page", list(Tabs.keys()))
st.sidebar.info("Made by Itoro Sampson")

# --- 3. RENDERING ---
if page == "Diagnosis":
    Tabs[page].app(df, X, y, model, model_score)
elif page == "Result":
    # Pass necessary data to result if needed
    Tabs[page].app()
else:
    Tabs[page].app()
