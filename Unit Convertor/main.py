import streamlit as st

# Set page title
st.set_page_config(page_title="Unit Converter App", page_icon="🔄")

# Conversion Logic
conversion_data = {
    "Length": {
        ("Metre", "Centimetre"): (lambda x: x * 100, "multiply the length value by 100"),
        ("Centimetre", "Metre"): (lambda x: x / 100, "divide the length value by 100"),
        ("Kilometers", "Miles"): (lambda x: x * 0.621371, "multiply the length by 0.621371"),
        ("Miles", "Kilometers"): (lambda x: x / 0.621371, "divide the length by 0.621371"),
    },
    "Weight": {
        ("Kilograms", "Pounds"): (lambda x: x * 2.20462, "multiply the weight by 2.20462"),
        ("Pounds", "Kilograms"): (lambda x: x / 2.20462, "divide the weight by 2.20462"),
    },
    "Time": {
        ("Seconds", "Minutes"): (lambda x: x / 60, "divide seconds by 60"),
        ("Minutes", "Seconds"): (lambda x: x * 60, "multiply minutes by 60"),
        ("Minutes", "Hours"): (lambda x: x / 60, "divide minutes by 60"),
        ("Hours", "Minutes"): (lambda x: x * 60, "multiply hours by 60"),
        ("Hours", "Days"): (lambda x: x / 24, "divide hours by 24"),
        ("Days", "Hours"): (lambda x: x * 24, "multiply days by 24"),
    }
}

# UI Layout
st.title("🔄 Unit Converter App")
category = st.selectbox("Choose a category", list(conversion_data.keys()))

# Build available conversions dynamically
unit_pairs = list(conversion_data[category].keys())
unit_labels = [f"{from_unit} to {to_unit}" for from_unit, to_unit in unit_pairs]
selected = st.selectbox("Choose a conversion", unit_labels)
selected_pair = unit_pairs[unit_labels.index(selected)]
convert_fn, formula_text = conversion_data[category][selected_pair]

# Inputs Layout
from_unit, to_unit = selected_pair

col1, col2, col3 = st.columns([1.5, 0.5, 1.5])

with col1:
    value = st.number_input("", value=1.0, key="input_val")
    st.caption(from_unit)

with col2:
    st.markdown("<div style='text-align:center; font-size: 2rem;'>=</div>", unsafe_allow_html=True)

with col3:
    result = convert_fn(value)
    st.number_input("", value=result, disabled=True, key="output_val")
    st.caption(to_unit)

# Formula
st.markdown(f"🟡 **Formula** &nbsp;&nbsp;&nbsp; {formula_text}")
