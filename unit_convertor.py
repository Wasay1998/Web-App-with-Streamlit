import streamlit as st
from pint import UnitRegistry 

def convert_units(value, from_unit, to_unit):
    ureg = UnitRegistry()
    try:
        result = ureg.Quantity(value, from_unit).to(to_unit)
        return f"{result:.2f}"
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    st.set_page_config(page_title="Google Unit Converter", page_icon="🔢", layout="centered")

    # Custom CSS for styling
    st.markdown(
        """
        <style>
            body {
                background: linear-gradient(135deg, #667eea, #764ba2);
                font-family: Arial, sans-serif;
            }
            .main-container {
                max-width: 600px;
                margin: auto;
                background: white;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
            }
            .stButton > button {
                background-color: #007BFF;
                color: white;
                padding: 12px 24px;
                font-size: 16px;
                border-radius: 8px;
                width: 100%;
                transition: 0.3s;
            }
            .stButton > button:hover {
                background-color: #0056b3;
            }
            .stSelectbox, .stNumberInput {
                border-radius: 8px;
                padding: 10px;
                width: 100%;
                font-size: 16px;
            }
            .title {
                text-align: center;
                color: #fff;
                font-size: 28px;
                font-weight: bold;
                margin-bottom: 10px;
            }
            .subtitle {
                text-align: center;
                color: #fff;
                font-size: 18px;
                margin-bottom: 20px;
            }
        </style>
        <div class="title">🌍 Google Unit Converter</div>
        <div class="subtitle">Convert different units professionally and efficiently.</div>
        <div class="subtitle">Developed by Abdul Wasay</div>
        """,
        unsafe_allow_html=True
    )

    unit_types = {
        "Length": ["meter", "kilometer", "centimeter", "millimeter", "mile", "yard", "foot", "inch"],
        "Weight": ["gram", "kilogram", "milligram", "pound", "ounce"],
        "Temperature": ["celsius", "fahrenheit", "kelvin"],
        "Volume": ["liter", "milliliter", "gallon", "cup", "pint"],
        "Time": ["second", "minute", "hour", "day"],
    }

    with st.container():
        category = st.selectbox("📌 Select a category", list(unit_types.keys()))
        from_unit = st.selectbox("🔄 From Unit", unit_types[category])
        to_unit = st.selectbox("🔄 To Unit", unit_types[category])
        value = st.number_input("✏️ Enter Value", min_value=0.0, format="%.2f")

    if st.button("Convert 🔥"):
        result = convert_units(value, from_unit, to_unit)
        st.success(f"✅ {value} {from_unit} = {result} {to_unit}")

    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
