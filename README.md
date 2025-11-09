<div align="center">

# 🌌 LuminaScope Lite

**AI-based Exoplanet Detector using NASA Kepler Light Curves (Lite Version)**  
*A machine learning mission that learns to detect worlds beyond our own.*

<img src="https://user-images.githubusercontent.com/00000000/placeholder-banner.png" width="800" alt="LuminaScope Lite Banner">

</div>

---

## 🪐 Overview

**LuminaScope Lite** is a lightweight prototype that analyzes stellar light curves — subtle variations in brightness recorded by NASA’s **Kepler** mission — to detect potential **exoplanet transits**.

Using a **Convolutional Neural Network (CNN)**, LuminaScope Lite learns to recognize the small, periodic dips in starlight that occur when a planet passes in front of its star.  
This *Lite version* lays the foundation for a full-scale project that could evolve into an intelligent observatory module within **SPIRAL**, your future AI assistant.

---

## 🚀 Features

- 📊 Reads and visualizes Kepler light-curve data  
- 🧠 Trains a compact 1D CNN to detect planetary transits  
- 🌑 Predicts “Planet Detected / No Planet” from unseen light curves  
- 🎨 (Optional) Interactive Streamlit dashboard for visual exploration  
- 🔭 Designed for expandability — integrates easily with NASA APIs

---

## ⚙️ Tech Stack

| Layer | Tools / Libraries |
|-------|--------------------|
| **Language** | Python |
| **ML Framework** | TensorFlow / Keras |
| **Data Handling** | NumPy, Pandas, Scikit-Learn |
| **Visualization** | Matplotlib / Plotly |
| **Frontend (Optional)** | Streamlit |
| **Dataset** | NASA Kepler Exoplanet Search Dataset (via Kaggle) |

---

## 🧩 Folder Structure

LuminaScope-Lite/
│
├── dataset/
│ └── kepler_exoplanet_search_results.csv
│
├── notebooks/
│ └── LuminaScope_Lite.ipynb
│
├── app.py # Streamlit interface (optional)
├── model.h5 # Saved model weights
├── README.md
└── requirements.txt

yaml
Copy code

---

## 🧠 Getting Started

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/sohmxdd/LuminaScope-Lite.git
cd LuminaScope-Lite
2️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
3️⃣ Run the Notebook
You can train and test the model locally or use Google Colab for GPU acceleration.

bash
Copy code
# In Colab
!git clone https://github.com/sohmxdd/LuminaScope-Lite.git
%cd LuminaScope-Lite
4️⃣ Launch the Streamlit App (optional)
bash
Copy code
streamlit run app.py
🌠 Project Goals
Build a CNN-based pipeline for exoplanet transit detection

Visualize light curves and AI predictions

Create an accessible interface for researchers and enthusiasts

Serve as the Lite base for LuminaScope Pro — a future module under SPIRAL

🧭 Roadmap
Phase	Focus	Status
Phase 1	Data collection & preprocessing	✅ In progress
Phase 2	CNN model training	⏳ Upcoming
Phase 3	Visualization & evaluation	⏳ Upcoming
Phase 4	Streamlit integration	⏳ Optional
Phase 5	NASA API extension & deployment	🔮 Future

💡 Inspiration
“Somewhere, something incredible is waiting to be known.”
— Carl Sagan

LuminaScope Lite merges that curiosity with code — blending astronomy, machine learning, and design into one unified mission.
