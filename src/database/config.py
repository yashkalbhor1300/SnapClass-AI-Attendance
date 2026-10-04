import streamlit as st
from supabase import create_client

SUPABASE_URL = "https://qyzwabvydgnrevgnfzvr.supabase.co"
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]

supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)