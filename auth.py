import streamlit as st
import psycopg2
import hashlib

# Database connection details (replace with your actual values)
DATABASE_URL = st.secrets["my_database"]["DATABASE_URL"]

def generate_hash(password):
    """Hashes the password using SHA-256."""
    return hashlib.sha256(str.encode(password)).hexdigest()

def check_hash(password, hashed_text):
    """Checks if the generated hash matches the stored hash."""
    return generate_hash(password) == hashed_text

def create_user(username, password):
    """Creates a new user in the PostgreSQL database."""
    if len(username) == 0 or len(password) == 0:
        st.error("Username and password must be at least one character long.")
        return
    try:
        with psycopg2.connect(DATABASE_URL) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT 1 FROM users WHERE username = %s", (username,))
                existing_user = cur.fetchone()
                if existing_user:
                    st.error("This username already exists.")
                else:
                    hashed_password = generate_hash(password)
                    cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
                    conn.commit()
                    st.success("User created successfully!")
    except psycopg2.Error as e:
        st.error(f"Database error: {e}")

def authenticate():
    """Authenticates the user against the PostgreSQL database."""
    if len(st.session_state.username) == 0 or len(st.session_state.password) == 0:
        st.error("Username and password must be at least one character long.")
        return False
    try:
        with psycopg2.connect(DATABASE_URL) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT password FROM users WHERE username = %s", (st.session_state.username,))
                user = cur.fetchone()
                if user:
                    hashed_password = user[0]
                    if check_hash(st.session_state.password, hashed_password):
                        st.session_state["authenticated"] = True
                        #st.session_state["username"] = username
                        st.success("Connecté avec succès!")
                        return True
                    else:
                        st.error("Nom d'utilisateur ou mot de passe incorrect.")
                return False
    except psycopg2.Error as e:
        st.error(f"Database error: {e}")
        return False