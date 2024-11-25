import duckdb

def create_users_table():
    """Crée une table 'users' dans DuckDB."""
    conn = duckdb.connect("app.db")
    conn.execute("""
        CREATE SEQUENCE IF NOT EXISTS seq_user_id START 1;
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY DEFAULT nextval('seq_user_id'),
            username VARCHAR(255) UNIQUE NOT NULL,
            password TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)
    conn.close()