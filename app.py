import streamlit as st
import numpy as np

st.set_page_config(
    page_title="KayKuks Pedics App",
    layout="centered"
)

st.title("🧒 KayKuks Pediatric Growth App")
st.caption("BMI & Pediatric Growth Assessment")

# -------------------------------
# INPUTS
# -------------------------------
sex = st.selectbox("Sex", ["Male", "Female"])
age = st.number_input("Age (years)", min_value=0.0, max_value=18.0, value=5.0)
weight = st.number_input("Weight (kg)", min_value=2.0, max_value=120.0, value=18.0)
height = st.number_input("Height (cm)", min_value=40.0, max_value=200.0, value=105.0)

# -------------------------------
# BMI CALCULATION
# -------------------------------
bmi = weight / ((height / 100) ** 2)

st.subheader("Results")
st.write(f"**BMI:** {bmi:.2f}")

if bmi < 18.5:
    st.warning("Underweight")
elif bmi < 25:
    st.success("Normal weight")
elif bmi < 30:
    st.warning("Overweight")
else:
    st.error("Obese")
