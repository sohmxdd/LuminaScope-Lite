import streamlit as st
import time
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
import os

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="LuminaScope Lite | Exoplanet Detection Console",
    page_icon=":milky_way:",
    layout="wide"
)

# ---------- CUSTOM COSMIC STYLE ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500&family=Inter:wght@400;600&display=swap');

body, .main {
    background: radial-gradient(circle at 25% 25%, #020912, #000000 85%);
    color: #E9F6FF;
    font-family: 'Inter', sans-serif;
    transition: all 0.4s ease;
}

/* STARFIELD BACKGROUND */
body::before {
    content: "";
    position: fixed;
    top:0; left:0; right:0; bottom:0;
    background: url('https://www.transparenttextures.com/patterns/stardust.png');
    opacity: 0.15;
    z-index: -1;
}

/* GLASS CARD */
.card {
    background: rgba(15, 25, 35, 0.5);
    border: 1px solid rgba(0, 255, 255, 0.2);
    border-radius: 16px;
    backdrop-filter: blur(20px);
    box-shadow: 0 0 20px rgba(0,255,255,0.05);
    padding: 1.5rem;
    transition: all 0.3s ease;
}
.card:hover {
    box-shadow: 0 0 25px rgba(0,255,255,0.2);
    transform: translateY(-4px);
}

/* HEADERS */
h1,h2,h3 {
    font-family: 'Orbitron', sans-serif;
    letter-spacing: 1px;
}
h1 {color:#00CFFF;text-shadow:0 0 18px #00CFFF;}
h2,h3 {color:#7AE6FF;text-shadow:0 0 8px #0077FF;}

/* BUTTONS */
.stButton>button {
    background: linear-gradient(90deg, #0066ff, #00ffff);
    border:none;
    border-radius:12px;
    padding:0.7em 1.5em;
    color:white;
    font-weight:600;
    box-shadow:0 0 10px #00FFFF55;
    transition:all 0.3s ease;
}
.stButton>button:hover {
    transform:scale(1.05);
    box-shadow:0 0 25px #00FFFFAA;
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown("<h1> LuminaScope Lite </h1>", unsafe_allow_html=True)
st.markdown("<h3> Advanced Exoplanet Detection Console </h3>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# ---------- SIDEBAR (GLASS PANEL) ----------
st.sidebar.markdown("<div class='card'><h3>Mission Control</h3>"
                    "<p>Upload Kepler dataset or use sample data to initiate scan.</p></div>",
                    unsafe_allow_html=True)
uploaded_file = st.sidebar.file_uploader("Upload Kepler CSV", type=["csv"])

# ---------- LOAD MODEL ----------
model_path = os.path.join(os.path.dirname(__file__), "luminascope_model.h5")
model = load_model(model_path)

# ---------- DATA LOAD ----------
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv("dataset/cumulative.csv").sample(100)

# ---------- PREPROCESS ----------
expected_shape = model.input_shape[-1]
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
features = numeric_cols[:expected_shape]
X = df[features].fillna(0)
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# ---------- DETECTION SEQUENCE ----------
placeholder = st.empty()
with placeholder.container():
    st.markdown("<div class='card'><h2>Detection Sequence</h2>", unsafe_allow_html=True)
    bar = st.progress(0)
    predictions = []
    for i, row in enumerate(X_scaled):
        pred = model.predict(np.array([row]))[0][0]
        label = "Confirmed" if pred > 0.5 else "Rejected"
        predictions.append((label, round(float(pred)*100, 2)))
        bar.progress((i+1)/len(X_scaled))
        time.sleep(0.01)
    st.markdown("</div>", unsafe_allow_html=True)

df['Prediction'], df['Confidence (%)'] = zip(*predictions)

# ---------- RESULTS (GLASS TABLE) ----------
st.markdown("<div class='card'><h2>Detection Summary</h2>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
col1.metric("Confirmed Planets", int((df['Prediction'] == "Confirmed").sum()))
col2.metric("Rejected Signals", int((df['Prediction'] == "Rejected").sum()))
col3.metric("Mean Confidence", f"{df['Confidence (%)'].mean():.1f}%")
st.dataframe(df[['koi_period','koi_prad','Prediction','Confidence (%)']])
st.markdown("</div>", unsafe_allow_html=True)

# ---------- FOOTER ----------
st.markdown("<br><p style='text-align:center;color:#7AE6FF;font-size:14px;'>"
            "Designed by Soham Mishra — LuminaScope Lite © 2025</p>",
            unsafe_allow_html=True)
