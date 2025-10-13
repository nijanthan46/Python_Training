import streamlit as st
import pandas as pd
import random
import time
import altair as alt

st.title("Advanced Hospital Sensor Live Monitoring")
st.write("Live simulation of Heart Rate, Temperature, and Blood Pressure with colored curves")

# Initialize data
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["Time", "Heart Rate", "Temperature", "Blood Pressure"])

chart_ph = st.empty()
status_ph = st.empty()

for _ in range(100):
    t = time.strftime("%H:%M:%S")
    hr = random.randint(60, 110)
    temp = round(random.uniform(36.0, 38.5), 1)
    bp = random.randint(110, 140)

    new = pd.DataFrame([[t, hr, temp, bp]], columns=["Time", "Heart Rate", "Temperature", "Blood Pressure"])
    st.session_state.data = pd.concat([st.session_state.data, new]).tail(30)

    # Metrics
    c1, c2, c3 = st.columns(3)
    c1.metric("Heart Rate (bpm)", hr)
    c2.metric("Temperature (°C)", temp)
    c3.metric("Blood Pressure (mmHg)", bp)

    # Melt data for colored line chart
    df_melt = st.session_state.data.melt("Time", var_name="Sensor", value_name="Value")

    chart = (
        alt.Chart(df_melt)
        .mark_line(point=True)
        .encode(
            x="Time",
            y="Value",
            color=alt.Color("Sensor", scale=alt.Scale(range=["red", "orange", "blue"])),
            strokeWidth=alt.value(3)
        )
        .properties(height=400)
    )

    chart_ph.altair_chart(chart, use_container_width=True)
    status_ph.info("Monitoring live... (updates every 2s)")
    time.sleep(1)
