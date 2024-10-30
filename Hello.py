import streamlit as st

# Title of the app
st.title("My First Streamlit App")

# Display some text
st.write("Hello, this is a basic Streamlit app!")

# Input field for user's name
name = st.text_input("Enter your name:")

# Display the name if entered
if name:
    st.write(f"Welcome, {name}!")

# Slider for a numeric value
number = st.slider("Select a number:", 0, 100)

# Display the selected number
st.write(f"You selected: {number}")