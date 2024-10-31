import streamlit as st
from auth import create_user, authenticate

# Title of the app
st.title("My First Streamlit App")

# Display some text
st.write("Hello, this is a basic Streamlit app!")

DATABASE_URL = st.secrets["my_database"]["DATABASE_URL"]

# --- Streamlit App ---
st.title("Authentification")

# --- Sidebar with Login/Signup ---
with st.sidebar:
    st.subheader("Authentification")
    # Initialize 'authenticated' in session_state if not already present
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False

    if not st.session_state.authenticated:
        username = st.text_input("Nom d'utilisateur")
        password = st.text_input("Mot de passe", type="password")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Connexion"):
                if authenticate(username, password):
                    st.success("Connecté avec succès!")
                    st.session_state.authenticated = True
                    st.rerun()
                else:
                    st.error("Nom d'utilisateur ou mot de passe incorrect.")
        # with col2:
        #     if st.button("Créer"):
        #         create_user(username, password)
    else:
        st.write(f"Bienvenue, {st.session_state.username}!")
        if st.button("Déconnexion"):
            st.session_state.authenticated = False
            st.rerun()  # Rerun to show login screen

# --- Main App Content ---
if st.session_state.authenticated:
    # Your app content goes here ...
    st.write("Ceci est le contenu de l'application.")
    st.session_state.test2 = True



# st.write("Welcome, you're logged in!")

# conn = connect_to_db()
# cur = conn.cursor()
# cur.execute("SELECT * FROM products;")
# data = cur.fetchall()
# cur.close()
# conn.close()
# st.dataframe(data)