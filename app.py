import streamlit as st
import pandas as pd
import psycopg  # psycopg v3
from sqlalchemy import create_engine

# ------------------ PostgreSQL Connection ------------------

db_info = st.secrets["postgres"]  # ensure .streamlit/secrets.toml has correct Supabase details

# psycopg v3 connection
def connect_db():
    conn = psycopg.connect(
        host=db_info["host"],
        port=db_info["port"],
        dbname=db_info["database"],
        user=db_info["user"],
        password=db_info["password"],
        sslmode="require"  # Supabase requires SSL
    )
    return conn

conn = connect_db()
cursor = conn.cursor()

# SQLAlchemy engine using psycopg v3 driver
# NOTE: SQLAlchemy does not officially support psycopg v3 directly via dialect name yet, so use psycopg2 for engine
host = db_info["host"]
port = db_info["port"]
dbname = db_info["database"]
user = db_info["user"]
password = db_info["password"]

# psycopg2 remains the correct dialect string even with psycopg v3
engine = create_engine(f'postgresql+psycopg://{user}:{password}@{host}:{port}/{dbname}?sslmode=require')

st.set_page_config(page_title="Courier Management System", layout="wide")
st.success("✅ Connected to Supabase PostgreSQL Database!")
