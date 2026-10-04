import streamlit as st


def header_home():

    st.image(
        "https://i.ibb.co/YTYGn5qV/logo.png",
        width=100
    )

    st.title("SNAP CLASS")


def header_dashboard():

    col1, col2 = st.columns([1, 3])

    with col1:
        st.image(
            "https://i.ibb.co/YTYGn5qV/logo.png",
            width=85
        )

    with col2:
        st.header("SNAP CLASS")