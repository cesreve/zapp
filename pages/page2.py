import streamlit as st

if "username" in st.session_state:
    st.write(st.session_state.username)

if "username" in st.session_state:
    if len(st.session_state.username)>0:
        username = st.text_input("Username", value=st.session_state.username)
        st.session_state.username = username
    else:
        username = st.text_input("Username")
        st.session_state.username = username
else:
    username = st.text_input("Username")
    st.session_state.username = username