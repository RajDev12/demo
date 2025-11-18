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
            return None

# Button to trigger calculation
if st.button("Calculate"):
    result = calculate(num1, num2, operation)
    if result is None:
        st.error("Error: Division by zero")
    else:
        st.success(f"Result: {result}")
        # Check if result is an integer and odd
        if isinstance(result, (int, float)) and result % 2 == 1:
            st.markdown("🎉 **It's an odd number! Celebrate!**")
        else:
            st.markdown("😞 **It's not odd. Better luck next time!**")