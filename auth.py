import duckdb
import hashlib
import streamlit as st

def generate_hash(password):
    """Hashes the password using SHA-256."""
    return hashlib.sha256(str.encode(password)).hexdigest()

def check_hash(password, hashed_text):
    """Checks if the generated hash matches the stored hash."""
    return generate_hash(password) == hashed_text

def create_user(username, password):
    """Creates a new user in the DuckDB database."""
    if len(username) == 0 or len(password) == 0:
        st.error("Username and password must be at least one character long.")
        return
    try:
        conn = duckdb.connect('app.db')  # Connect to the DuckDB database file
        cur = conn.cursor()

        cur.execute("SELECT 1 FROM users WHERE username = ?", (username,))
        existing_user = cur.fetchone()
        if existing_user:
            st.error("This username already exists.")
        else:
            hashed_password = generate_hash(password)
            cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
            conn.commit()
            st.success("User created successfully!")

    except Exception as e:  # Use a more general exception for DuckDB
        st.error(f"Database error: {e}")
    finally:
        if conn:
            cur.close()
            conn.close()

def authenticate():
    """Authenticates the user against the DuckDB database."""
    username = st.session_state.get("username")  # Safely access session state
    password = st.session_state.get("password")

    if not username or not password:
        st.error("Username and password must be at least one character long.")
        return False

    try:
        conn = duckdb.connect('app.db')
        cur = conn.cursor()
        cur.execute("SELECT password FROM users WHERE username = ?", (username,))
        user = cur.fetchone()

        if user:
            hashed_password = user[0]
            if check_hash(password, hashed_password):
                st.session_state["authenticated"] = True
                st.success("Logged in successfully!") # Changed to English for consistency
                return True
            else:
                st.error("Incorrect username or password.")
        else:
            st.error("Incorrect username or password.")  # User not found
        return False  # Explicitly return False if authentication fails

    except Exception as e:
        st.error(f"Database error: {e}")
        return False

    finally:
        if conn:  # Ensure connection is closed in all cases
            cur.close()
            conn.close()
