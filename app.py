import streamlit as st
import math

# Page Setup
st.set_page_config(page_title="Pro Neon Scientific Calculator", page_icon="💡", layout="centered")

# Initialize Session State
if "calc_input" not in st.session_state:
    st.session_state.calc_input = ""

if "history" not in st.session_state:
    st.session_state.history = []

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
        allowed_names.update({"abs": abs, "round": round, "factorial": math.factorial})
        expr = st.session_state.calc_input.replace("^", "**")
        result = eval(expr, {"__builtins__": None}, allowed_names)
        if isinstance(result, float):
            result = round(result, 8)
        
        # Save to calculation history
        calc_record = f"{st.session_state.calc_input} = {result}"
        if calc_record not in st.session_state.history:
            st.session_state.history.insert(0, calc_record)
            if len(st.session_state.history) > 5: # Keep last 5 items
                st.session_state.history.pop()

        st.session_state.calc_input = str(result)
    except Exception:
        st.session_state.calc_input = "Error"

# Intense Neon & Cyberpunk Glow CSS
st.markdown(
    """
    <style>
    .stApp {
        background: radial-gradient(circle at center, #0f172a 0%, #020617 100%);
    }
    h1 {
        color: #38bdf8;
        font-weight: 700;
        text-align: center;
        font-size: 2.2rem !important;
        text-shadow: 0 0 20px rgba(56, 189, 248, 0.6);
        margin-bottom: 0px !important;
    }
    .stTextInput input {
        font-size: 2.8rem !important;
        text-align: right !important;
        padding: 18px 22px !important;
        border-radius: 18px !important;
        background-color: #090d16 !important;
        color: #00ffcc !important;
        font-family: 'Courier New', Courier, monospace !important;
        font-weight: bold !important;
        border: 2px solid #00ffcc !important;
        box-shadow: inset 0 0 20px rgba(0, 255, 204, 0.3), 0 0 15px rgba(0, 255, 204, 0.2) !important;
    }
    div[data-testid="stButton"] button {
        border-radius: 14px !important;
        height: 60px !important;
        font-size: 1.25rem !important;
        font-weight: 600 !important;
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%) !important;
        color: #38bdf8 !important;
        border: 1px solid rgba(56, 189, 248, 0.4) !important;
        transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5) !important;
    }
    div[data-testid="stButton"] button:hover {
        background: linear-gradient(135deg, #334155 100%, #1e293b 0%) !important;
        border-color: #00ffcc !important;
        color: #00ffcc !important;
        box-shadow: 0 0 20px rgba(0, 255, 204, 0.7), inset 0 0 8px rgba(0, 255, 204, 0.4) !important;
        transform: translateY(-2px) scale(1.02);
    }
    div[data-testid="stButton"] button:active {
        background: #00ffcc !important;
        color: #020617 !important;
        transform: translateY(3px) scale(0.96) !important;
        box-shadow: 0 0 35px #00ffcc, inset 0 0 15px rgba(2, 6, 23, 0.9) !important;
        border-color: #ffffff !important;
    }
    .block-container {
        padding-top: 2rem !important;
        max-width: 480px !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# App Title
st.markdown("<h1>⚡ Neon Scientific Calculator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 0.95rem;'>Expandable Advanced Tools & Glow Interface</p>", unsafe_allow_html=True)

# Screen Display
st.text_input("Display", value=st.session_state.calc_input, disabled=True, label_visibility="collapsed")
st.write("")

# ----------------- EXPANDABLE ADVANCED FEATURES & HISTORY -----------------
with st.expander("🛠️ Advanced Tools, Constants & History (Click to Open/Minimize)"):
    col_a, col_b, col_c = st.columns(3)
    if col_a.button("n!", use_container_width=True):
        button_click("factorial(")
    if col_b.button("abs(", use_container_width=True):
        button_click("abs(")
    if col_c.button("deg2rad", use_container_width=True):
        button_click("radians(")
        
    st.markdown("**Recent Calculations History:**")
    if st.session_state.history:
        for h in st.session_state.history:
            st.code(h, language="text")
        if st.button("Clear History", use_container_width=True):
            st.session_state.history = []
            st.rerun()
    else:
        st.info("No calculations yet.")
# --------------------------------------------------------------------------

# Main Calculator Button Grid (5 columns)
c1, c2, c3, c4, c5 = st.columns(5)

# Row 1
c1.button("sin(", on_click=button_click, args=["sin("], use_container_width=True)
c2.button("cos(", on_click=button_click, args=["cos("], use_container_width=True)
c3.button("tan(", on_click=button_click, args=["tan("], use_container_width=True)
c4.button("(", on_click=button_click, args=["("], use_container_width=True)
c5.button(")", on_click=button_click, args=[")"], use_container_width=True)

# Row 2
c1.button("log(", on_click=button_click, args=["log10("], use_container_width=True)
c2.button("sqrt(", on_click=button_click, args=["sqrt("], use_container_width=True)
c3.button("^", on_click=button_click, args=["^"], use_container_width=True)
c4.button("DEL", on_click=delete_last, use_container_width=True)
c5.button("C", on_click=clear_display, use_container_width=True)

# Row 3
c1.button("7", on_click=button_click, args=["7"], use_container_width=True)
c2.button("8", on_click=button_click, args=["8"], use_container_width=True)
c3.button("9", on_click=button_click, args=["9"], use_container_width=True)
c4.button("/", on_click=button_click, args=["/"], use_container_width=True)
c5.button("pi", on_click=button_click, args=["pi"], use_container_width=True)

# Row 4
c1.button("4", on_click=button_click, args=["4"], use_container_width=True)
c2.button("5", on_click=button_click, args=["5"], use_container_width=True)
c3.button("6", on_click=button_click, args=["6"], use_container_width=True)
c4.button("*", on_click=button_click, args=["*"], use_container_width=True)
c5.button("e", on_click=button_click, args=["e"], use_container_width=True)

# Row 5
c1.button("1", on_click=button_click, args=["1"], use_container_width=True)
c2.button("2", on_click=button_click, args=["2"], use_container_width=True)
c3.button("3", on_click=button_click, args=["3"], use_container_width=True)
c4.button("-", on_click=button_click, args=["-"], use_container_width=True)
c5.button(".", on_click=button_click, args=["."], use_container_width=True)

# Row 6
c1.button("0", on_click=button_click, args=["0"], use_container_width=True)
c2.button("00", on_click=button_click, args=["00"], use_container_width=True)
c3.button("%", on_click=button_click, args=["%"], use_container_width=True)
c4.button("+", on_click=button_click, args=["+"], use_container_width=True)
c5.button("=", on_click=evaluate_expression, use_container_width=True)