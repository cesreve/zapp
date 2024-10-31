import streamlit as st

st.title("titre")

"st.session_state object", st.session_state

if "a_counter" not in st.session_state:
    st.session_state['a_counter'] = 0

if "boolean" not in st.session_state:
    st.session_state.boolean = False

st.write(st.session_state)

button = st.button("Click me")
if button:
    st.session_state['a_counter'] += 1
    st.session_state['boolean'] = not st.session_state['boolean']