# 🌌 LuminaScope Lite

**AI-based Exoplanet Detector using NASA Kepler Light Curves (Lite Version)**  
*A machine learning mission that learns to detect worlds beyond our own.*

![Typing Animation](https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=500&size=22&pause=1000&color=00BFFF&center=true&vCenter=true&width=600&lines=Detecting+Distant+Worlds+with+AI;Powered+by+SPIRAL+%7C+Kepler+Data;Exploring+the+Universe+Through+Light)

---

## 🪐 Overview

**LuminaScope Lite** is a lightweight prototype that analyzes stellar brightness data from NASA’s **Kepler mission** to detect potential **exoplanet transits** — the slight dimming of a star caused by a planet passing in front of it.  

Using a **neural network model**, it learns to identify subtle patterns in astrophysical parameters and distinguish between *confirmed exoplanets* and *false positives*.  

This *Lite version* represents the foundational phase of the larger **LuminaScope Project**, envisioned to integrate directly with **SPIRAL**, a personalized AI observatory system.

---

## 🚀 Features

- 📊 Reads and processes NASA Kepler’s cumulative dataset  
- 🧠 Trains a compact dense neural network for classification  
- 🌑 Predicts "Planet Detected" vs "False Positive"  
- 🔭 Expandable to 1D CNN models with raw light-curve data  
- 💾 Includes trained model weights (`luminascope_model_v2.h5`)  

---

## ⚙️ Tech Stack

| Layer | Tools / Libraries |
|:------|:------------------|
| **Language** | Python |
| **ML Framework** | TensorFlow / Keras |
| **Data Handling** | Pandas, NumPy, Scikit-learn |
| **Visualization** | Matplotlib |
| **Dataset** | NASA Kepler Exoplanet Search Results (Cumulative CSV) |

---

## 🧩 Folder Structure

LuminaScope-Lite/
│
├── dataset/
│ └── cumulative.csv
│
├── notebooks/
│ └── LuminaScope_Lite_Final.ipynb
│
├── luminascope_model_v2.h5
├── README.md
└── requirements.txt

yaml
Copy code

---

## 🧠 Model Information

**Model Version:** v2 (Final Release)  
**Type:** Deep Feedforward Neural Network  
**Accuracy:** ~75% (Baseline benchmark for cumulative dataset)  

**Architecture Summary:**
- Dense(128, ReLU)  
- Dropout(0.4)  
- Dense(64, ReLU)  
- Dropout(0.3)  
- Dense(1, Sigmoid)

**Optimizer:** Adam (lr = 0.0005)  
**Loss Function:** Binary Crossentropy  

📦 Saved Model File → `luminascope_model_v2.h5`

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
You can train and test the model locally or in Google Colab.

bash
Copy code
# In Colab
!git clone https://github.com/sohmxdd/LuminaScope-Lite.git
%cd LuminaScope-Lite
4️⃣ Load the Trained Model (Optional)
python
Copy code
from tensorflow.keras.models import load_model
model = load_model("luminascope_model_v2.h5")
🌠 Dataset Information
Source: NASA Kepler Exoplanet Search Results (Cumulative Dataset)
File Used: dataset/cumulative.csv

Feature	Description
koi_period	Orbital period (days)
koi_duration	Transit duration (hours)
koi_depth	Transit depth (ppm)
koi_prad	Planet radius (Earth radii)
koi_teq	Planet equilibrium temperature (K)
koi_disposition	Disposition label (CONFIRMED / FALSE POSITIVE)

🧭 Roadmap
Phase	Focus	Status
Phase 1	Data preprocessing + baseline model	✅ Complete
Phase 2	Feature engineering + tuning	✅ Complete
Phase 3	Streamlit dashboard UI	🔄 Upcoming
Phase 4	LuminaScope Pro (Raw Light Curves + CNN)	🔮 Planned

💡 Inspiration
“Somewhere, something incredible is waiting to be known.”
— Carl Sagan

LuminaScope Lite combines astronomy, AI, and design into one mission:
to make the unseen worlds beyond our solar system visible through code. ✨
