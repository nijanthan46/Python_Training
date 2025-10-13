import streamlit as st
import random
import time

st.title("Hospital Sensor Live Monitoring")
st.write("Simulating live data for Heart Rate, Temperature, and Blood Pressure")

# --- Placeholders for live values ---
hr_placeholder = st.empty()
temp_placeholder = st.empty()
bp_placeholder = st.empty()

# --- Live simulation loop ---
while True:
    heart_rate = random.randint(60, 100)
    temperature = round(random.uniform(36.0, 38.0), 1)
    systolic = random.randint(110, 130)
    diastolic = random.randint(70, 85)

    hr_placeholder.metric("Heart Rate (bpm)", heart_rate)
    temp_placeholder.metric("Temperature (°C)", temperature)
    bp_placeholder.metric("Blood Pressure (mmHg)", f"{systolic}/{diastolic}")

    time.sleep(2)
