# JAM: Junk Accumulation Model Streamlit Tool

An interactive Streamlit application for exploring space debris dynamics using an epidemiological SIR-style framework.

🔗 **Live App:** https://jam-simulation.streamlit.app

---

## 🛰️ Overview

The Junk Accumulation Model (JAM) applies compartmental modeling concepts from epidemiology to orbital debris. Objects are grouped into:

- **Susceptible (S):** Intact spacecraft and objects at risk of fragmentation  
- **Infectious (I):** Fragmentation debris capable of generating additional debris  
- **Removed (R):** Objects removed via decay or re-entry  

The model captures nonlinear, self-reinforcing debris growth dynamics and enables exploration of how factors such as launch rates and debris removal influence long-term behavior.

---

## 🚀 Features

- Interactive sliders for model parameters:
  - Launch rate (Λ)
  - Collision rate (β)
  - Fragmentation yield (θ)
  - Natural decay rates (μₛ, μᵢ)
  - Active debris removal (γ)
- Real-time simulation of S, I, R trajectories
- Visualization of debris growth and regime behavior

---

## 🧠 Purpose

This tool is designed for:
- Conceptual exploration of orbital debris dynamics  
- Demonstrating threshold and nonlinear behavior  
- Supporting research on space traffic management and debris mitigation  

⚠️ This repository is part of academic research and is intended for exploratory and educational purposes.

---

## 📁 Repository Structure

- jam-app.py: Streamlit application
- requirements.txt: Python dependencies 

---

## 👩‍🚀 Author

Rachel Sholder, JHU Doctor of Engineering  
Johns Hopkins University Applied Physics Laboratory (JHU/APL) 

Doctoral research bridging:
**epidemiology × orbital debris dynamics**

🔴 **TEDx Talk "Epidemics in Orbit: How Space Debris is Going Viral" Here:** https://www.youtube.com/watch?v=RV6VHMmfUs8

---

## 📌 Citation

If you use this work, please cite:

> R. Sholder, “Epidemics in Orbit: Modeling Space Debris Dynamics to Alleviate the Orbital Traffic Jam,” IEEE Aerospace Conference, 2026.

---

