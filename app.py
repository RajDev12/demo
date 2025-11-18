import streamlit as st

# Title
st.title("🧮 Simple Calculator")

# Input fields
num1 = st.number_input("Enter first number", format="%.2f")
num2 = st.number_input("Enter second number", format="%.2f")

# Operation selection
operation = st.selectbox("Select operation", ["Add", "Subtract", "Multiply", "Divide"])

# Calculate result
def calculate(n1, n2, op):
    if op == "Add":
        return n1 + n2
    elif op == "Subtract":
        return n1 - n2
    elif op == "Multiply":
        return n1 * n2
    elif op == "Divide":
        if n2 != 0:
            return n1 / n2
        else:
            return "Error: Division by zero"

# Button to trigger calculation
if st.button("Calculate"):
    result = calculate(num1, num2, operation)
    st.success(f"Result: {result}")