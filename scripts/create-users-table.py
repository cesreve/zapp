import psycopg2
import streamlit as st

DATABASE_URL = st.secrets["my_database"]["DATABASE_URL"]

with psycopg2.connect(DATABASE_URL) as conn:
    with conn.cursor() as cur:
        cur.execute("""DROP TABLE users;""")
        conn.commit()


def create_users_table():
    """Crée la table 'users' dans la base de données PostgreSQL."""
    try:
        with psycopg2.connect(DATABASE_URL) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS users (
                        user_id SERIAL PRIMARY KEY,
                        username VARCHAR(255) UNIQUE NOT NULL,
                        password VARCHAR(255) NOT NULL
                    );
                """)
                conn.commit()
                print("Table 'users' créée avec succès!")
    except psycopg2.Error as e:
        print(f"Erreur lors de la création de la table: {e}")

# Appel de la fonction pour créer la table 'users'
create_users_table()


# CREATE TABLE IF NOT EXISTS users (
# user_id SERIAL PRIMARY KEY,
# username VARCHAR(255) UNIQUE NOT NULL,
# password VARCHAR(255) NOT NULL,   

# email VARCHAR(255) UNIQUE NOT NULL,
# first_name VARCHAR(255),
# last_name VARCHAR(255),   

# role VARCHAR(50) DEFAULT 'user',
# created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
# last_login TIMESTAMP,
# is_active BOOLEAN DEFAULT TRUE