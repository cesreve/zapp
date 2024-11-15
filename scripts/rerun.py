import streamlit as st

def callback():
  """This function will be called when the text input changes."""
  st.write(st.session_state.my_input)

st.title("`on_change` Argument Example")

st.write("Type something in the text input below:")
st.text_input("My Input", key="my_input", on_change=callback)