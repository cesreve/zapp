import streamlit as st
import psycopg2
import os

# Title of the app
st.title("My First Streamlit App")

# Display some text
st.write("Hello, this is a basic Streamlit app!")

DATABASE_URL = st.secrets["my_database"]["DATABASE_URL"]


st.write("Welcome, you're logged in!")
conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor()
cur.execute("SELECT * FROM products;")
data = cur.fetchall()
cur.close()
conn.close()
st.dataframe(data)