import streamlit as st

# Function
# to handle operations
def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 // num2  # Use integer division
    else:
        return "Invalid operator"

# Streamlit UI setup
st.set_page_config(page_title="Calculator", page_icon="🧮")

# Custom CSS for styling
st.markdown("""
    <style>
    body {
        background-color: #5A2D81;  /* Purple background */
    }
    .stButton>button {
        background-color: #6D28D9;  /* Button color */
        color: white;
        border-radius: 5px;
        height: 3em;
        font-size: 16px;
    }
    .stTextInput>div>input {
        border-radius: 5px;
        height: 2em;
        font-size: 16px;
    }
    </style>
    """, unsafe_allow_html=True)

# Title of the app
st.title("Calculator")

# Inputs
num1 = st.number_input("Enter first number", min_value=0, format="%d")
num2 = st.number_input("Enter second number", min_value=0, format="%d")
operator = st.selectbox("Choose an operator", ['+', '-', '*', '/'])

# Calculate button
if st.button("Calculate"):
    result = calculate(num1, num2, operator)
    st.write(f"**Result**: {result}")

