import streamlit as st
from auth import authenticate ,create_user

# --- Streamlit App ---
st.head("test")

# Title of the app
st.title("My First hello")

# Display some text
st.write("Hello, this is a basic Streamlit app!")
    
# --- Sidebar with Login/Signup ---
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False
with st.sidebar:
    st.subheader("Authentification")
    if not st.session_state["authenticated"]:
        username = st.text_input("Nom d'utilisateur")
        if len(username)>0:
            st.session_state.username = username
        st.text_input("Mot de passe", type="password", key="password", on_change=authenticate )

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Connexion"):
                if authenticate():
                    st.success("Connecté avec succès!")
                    st.rerun()  # Rerun to show authenticated content
                else:
                    st.error("Nom d'utilisateur ou mot de passe incorrect.")
        with col2:
          if st.button("Créer"):
               create_user(st.session_state.username, st.session_state.password)
    else:
        if 'username' in st.session_state:
            if len(st.session_state.username)>0:
                st.write(f"Bienvenue, {st.session_state.username}!")
        if st.button("Déconnexion"):
            st.session_state["authenticated"] = False
            st.rerun()  # Rerun to show login screen

# --- Main App Content ---
st.title("Authentification")
if st.session_state.authenticated:
    if 'username' in st.session_state:
        if len(st.session_state.username) > 0 :
            st.write(f"Bienvenue, {st.session_state.username}!")
else:
    st.write("Pas authentifié")
