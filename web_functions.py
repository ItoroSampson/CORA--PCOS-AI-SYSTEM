import numpy as np
import pandas as pd
import xgboost as xgb
import streamlit as st
import joblib
from pathlib import Path


@st.cache_data()
def load_data():

    df = pd.read_csv("PCOS.csv")
    X = df[
        [
            "Age",
            "Menstrual_Irregularity",
            "Testosterone_Level(ng/dL)",
            "Antral_Follicle_Count",
        ]
    ]
    y = df["PCOS_Diagnosis"]
    return df, X, y


@st.cache_resource()
def train_model(X, y):
    model = xgb.XGBClassifier(
        n_estimators=100,
        max_depth=4,
        learning_rate=0.1,
        random_state=42,
        objective="binary:logistic",
        eval_metric="logloss",
    )
    model.fit(X, y)
    score = model.score(X, y)

    # Save the model to file for future use
    model_dir = Path("Models")
    model_dir.mkdir(exist_ok=True)
    joblib.dump(model, model_dir / "pcos_model.pkl")

    return model, score


def predict_pcos(model, features):
    prediction = model.predict(features)
    score = model.predict_proba(features)[:, 1]
    return prediction, score
