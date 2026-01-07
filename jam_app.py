import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import matplotlib.ticker as ticker
from scipy.integrate import odeint

st.set_page_config(layout="wide")

# --- Title ---
st.title("🛰️ Space Debris JAM: Junk Accumulation Model")
st.markdown("""
This interactive tool simulates space debris dynamics in LEO using an epidemiological SIR-compartmental model framework.


Adjust the parameters to the left to explore how various factors, including Active Debris Removal (ADR),  influence space debris proliferation.
""")

# Sidebar parameters
st.sidebar.header("JAM Inputs")

# -------------------------
st.sidebar.subheader("🎯 Initial Conditions")
S0 = st.sidebar.number_input("Initial Susceptible (S0)", value=6768.0)
I0 = st.sidebar.number_input("Initial Infectious (I0)", value=34000.0)
R0 = st.sidebar.number_input("Initial Removed (R0)", value=0.0)
y0 = [S0, I0, R0]

# --- Sidebar sliders ---
if st.sidebar.button("Reset to paper baseline"):
    st.session_state["Λ"] = 2262
    st.session_state["β"] = 9/(S0*I0)
    st.session_state["θ"] = 29
    st.session_state["γ"] = 0.0
    st.session_state["μ_S"] = 250/S0
    st.session_state["μ_I"] = 450/I0

st.sidebar.subheader("📈 Model Parameters")
Λ = st.sidebar.slider("Λ: Launch Rate", 0, 10000, 2262, key="Λ")
β = st.sidebar.slider("β", 1e-9, 1e-5, float(9/(S0*I0)), step=1e-9, format="%.1e", key="β")
θ = st.sidebar.slider("θ: Debris Fragments Generated per Collision", 0, 50, 29, key="θ")
γ = st.sidebar.slider("γ: Active Debris Removal (ADR) Rate)", 0.0, 0.1, 0.0, step=0.005, key="γ")
μ_S = st.sidebar.slider("μ$_S$: Natural Decay Rate of Intact Objects", 0.0, 0.1, float(450/(S0)), step=0.001, key="μ_S")
μ_I = st.sidebar.slider("μ$_I$: Natural Decay Rate of Fragments", 0.0, 0.1, float(250/(I0)), step=0.001, key="μ_I")

# -------------------------
st.sidebar.subheader("⏱️ Simulation Settings")
T = st.sidebar.slider("Simulation Time (years)", 1, 100, 50)

# --- JAM Model ---
def jam_model(t, y, Λ, β, θ, γ, μ_S, μ_I):
    S, I, R = y
    dSdt = Λ - β * S * I - μ_S * S
    dIdt = (1 + θ) * β * S * I - (γ + μ_I) * I
    dRdt = γ * I + μ_S * S + μ_I * I
    return [dSdt, dIdt, dRdt] 

# --- Simulation Function ---
def run_simulation(y0, Λ, β, θ, γ, μ_S, μ_I, T):
    t_span = (0, T)
    t_eval = np.linspace(0, T, 1000)
    sol = solve_ivp(jam_model, t_span, y0, args=(Λ, β, θ, γ, μ_S, μ_I), t_eval=t_eval)
    S, I, R = sol.y 
    Rt = ((1 + θ) * β * S) / (γ + μ_I)
    return t_eval, S, I, R, Rt

# --- Run model ---
t, S, I, R, Rt = run_simulation([S0, I0, R0], Λ, β, θ, γ, μ_S, μ_I, T)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

# Top plot: JAM compartments
ax1.plot(t, S, label='Susceptible (S)')
ax1.plot(t, I, label='Infectious (I)')
ax1.plot(t, R, label='Removed (R)')
ax1.set_ylabel('Number of Objects')
ax1.set_title('JAM Model Simulation')
ax1.legend(loc='upper right')
ax1.grid(True)


# Bottom plot: Rₑ(t)
ax2.plot(t, Rt, 'k--', label='Effective Reproduction Number Rₜ(t)')
ax2.axhline(y=1, color='red', linestyle=':')
ax2.set_ylabel('Rₑ(t)')
ax2.set_xlabel('Time (Years)')
ax2.legend(loc='upper right')
ax2.grid(True)



st.pyplot(fig)


# --- Summary Stats ---
st.subheader("📊 Final Statistics")
st.write(f"**Final Susceptible (S):** {S[-1]:,.0f}")
st.write(f"**Final Infectious (I):** {I[-1]:,.0f}")
st.write(f"**Final Removed (R):** {R[-1]:,.0f}")
st.write(f"**Max Rₜ(t):** {np.max(Rt):.2f} | **Final Rₜ(t):** {Rt[-1]:.2f}")


st.markdown("---")
st.markdown("Built by Rachel Sholder")