import psycopg2
import streamlit as st

# Get the database URL from environment variable
DATABASE_URL = st.secrets["my_database"]["DATABASE_URL"]


def connect_to_db():
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(DATABASE_URL)

    except Exception as e:
        print(f"Error accessing database: {e}")
