import streamlit as st

# Page configuration
st.set_page_config(page_title="Chemical Analysis Calculator", layout="wide")

# Title
st.title ("🔬 Chemical Analysis Calculator")
st.markdown ("Automatically calculate **moisture content, ash content, sulfate, Fe, and Ba** from lab data.")

# Sidebar input
st.sidebar.header ("📥 Sample Data Input")
sample_name = st.sidebar.text_input ("Sample Name", "Sample A")
weight_initial = st.sidebar.number_input ("Initial Sample Weight (g)", min_value=0.0, value=5.0, step=0.01)
weight_dry = st.sidebar.number_input ("Weight After Drying (g)", min_value=0.0, value=4.5, step=0.01)
weight_ash = st.sidebar.number_input ("Ash Weight (g)", min_value=0.0, value=0.2, step=0.01)
weight_baso4 = st.sidebar.number_input ("BaSO₄ Precipitate Weight (g)", min_value=0.0, value=0.5, step=0.01)
weight_fe2o3 = st.sidebar.number_input ("Fe₂O₃ Precipitate Weight (g)", min_value=0.0, value=0.3, step=0.01)

# Calculations
if weight_initial > 0:
    # Perform calculations
    moisture = ((weight_initial - weight_dry) / weight_initial) * 100
    ash = (weight_ash / weight_initial) * 100
    sulfate = (weight_baso4 * 96.06 / 233.39 / weight_initial) * 100   # M(SO4)=96.06, M(BaSO4)=233.39
    iron
