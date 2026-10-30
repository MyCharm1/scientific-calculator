import streamlit as st
import math

# Set Page Configuration
st.set_page_config(page_title="Scientific Calculator", page_icon="🧮", layout="centered")

st.markdown("<h1 style='text-align: center; color: #00ffcc;'>🧮 Modern Scientific Calculator</h1>", unsafe_allow_html=True)

# Initialize session state for the calculator display
if "calc_input" not in st.session_state:
    st.session_state.calc_input = ""

# Callback functions for buttons
def button_click(val):
    if st.session_state.calc_input == "Error":
        st.session_state.calc_input = ""
    st.session_state.calc_input += str(val)

def clear_display():
    st.session_state.calc_input = ""

def delete_last():
    if st.session_state.calc_input != "Error":
        st.session_state.calc_input = st.session_state.calc_input[:-1]

def evaluate_expression():
    try:
        allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
        allowed_names.update({"abs": abs, "round": round})
        expr = st.session_state.calc_input.replace("^", "**")
        result = eval(expr, {"__builtins__": None}, allowed_names)
        if isinstance(result, float):
            result = round(result, 8)
        st.session_state.calc_input = str(result)
    except Exception:
        st.session_state.calc_input = "Error"

# Advanced CSS for Modern UI, Glowing Buttons, and Press Effects
st.markdown(
    """
    <style>
    /* Calculator Display Screen */
    .stTextInput input {
        font-size: 3rem !important; 
        text-align: right !important;
        padding: 20px !important;
        border-radius: 15px !important;
        background-color: #121212 !important;
        color: #00ffcc !important;
        font-family: 'Courier New', Courier, monospace !important;
        box-shadow: inset 0px 4px 15px rgba(0, 0, 0, 0.8) !important;
        border: 2px solid #00ffcc !important;
    }

    /* All Buttons Base Style */
    div[data-testid="stButton"] button {
        border-radius: 15px !important;
        height: 70px !important;
        font-size: 1.5rem !important;
        font-weight: bold !important;
        transition: all 0.2s ease-in-out !important;
        background-color: #2b2b2b !important;
        color: #ffffff !important;
        border: 1px solid #444 !important;
        box-shadow: 3px 5px 10px rgba(0,0,0,0.3) !important;
    }

    /* Hover Effect (Soft Glow) */
    div[data-testid="stButton"] button:hover {
        border-color: #00ffcc !important;
        box-shadow: 0px 0px 15px rgba(0, 255, 204, 0.4) !important;
        transform: translateY(-2px) !important;
        color: #00ffcc !important;
    }

    /* Active/Click Effect (The Light/Shadow Press) */
    div[data-testid="stButton"] button:active {
        transform: translateY(4px) scale(0.95) !important;
        background-color: #00ffcc !important;
        color: #000000 !important;
        box-shadow: 0px 0px 25px rgba(0, 255, 204, 0.9), inset 0px