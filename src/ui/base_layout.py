import streamlit as st


def style_background_home():

    st.markdown("""
        <style>

            .stApp {
                background: #E0E3FF !important;
            }

            .stApp div[data-testid="stColumn"] {
                background-color: #E0E3FF !important;
                padding: 2.5rem !important;
                border-radius: 2rem !important;
            }

        </style>
    """, unsafe_allow_html=True)


def style_background_dashboard():

    st.markdown("""
        <style>

            .stApp {
                background: #E0E3FF !important;
            }

        </style>
    """, unsafe_allow_html=True)


def style_base_layout():

    st.markdown("""
        <style>

            /* Google Fonts */

            @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
            @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');


            /* Hide Streamlit default UI */

            #MainMenu,
            footer,
            header {
                visibility: hidden;
            }


            /* Main container */

            .block-container {
                padding-top: 1.5rem !important;
            }


            /* Main headings */

            h1,
            h2 {
                font-family: 'Climate Crisis', sans-serif !important;
            }

            h1 {
                font-size: 3.5rem !important;
                line-height: 1.1 !important;
                margin-bottom: 0rem !important;
            }

            h2 {
                font-size: 2rem !important;
                line-height: 0.9 !important;
                margin-bottom: 0rem !important;
            }


            /* All normal text */

            h3,
            h4,
            h5,
            h6,
            p,
            label,
            span,
            div {
                font-family: 'Outfit', sans-serif !important;
            }


            /* Streamlit text elements */

            [data-testid="stCaptionContainer"],
            [data-testid="stMarkdownContainer"],
            [data-testid="stText"],
            [data-testid="stAlert"] {
                font-family: 'Outfit', sans-serif !important;
            }


            /* Inputs */

            input,
            textarea,
            select {
                font-family: 'Outfit', sans-serif !important;
            }


            /* Selectbox */

            div[data-baseweb="select"] * {
                font-family: 'Outfit', sans-serif !important;
            }


            /* Buttons */

            button {
                font-family: 'Outfit', sans-serif !important;
                border-radius: 1.5rem !important;
                background-color: #5865F2 !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            }


            /* Secondary buttons */

            button[kind="secondary"] {
                font-family: 'Outfit', sans-serif !important;
                border-radius: 1.5rem !important;
                background-color: #EB459E !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
            }


            /* Tertiary buttons */

            button[kind="tertiary"] {
                font-family: 'Outfit', sans-serif !important;
                border-radius: 1.5rem !important;
                background-color: black !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
            }


            /* Button hover */

            button:hover {
                transform: scale(1.05);
            }


            /* Tabs */

            button[data-baseweb="tab"] {
                font-family: 'Outfit', sans-serif !important;
            }


            /* File uploader */

            section[data-testid="stFileUploader"] * {
                font-family: 'Outfit', sans-serif !important;
            }


            /* Radio buttons */

            div[data-testid="stRadio"] * {
                font-family: 'Outfit', sans-serif !important;
            }


            /* Checkboxes */

            div[data-testid="stCheckbox"] * {
                font-family: 'Outfit', sans-serif !important;
            }


            /* Metrics */

            div[data-testid="stMetric"] * {
                font-family: 'Outfit', sans-serif !important;
            }

        </style>
    """, unsafe_allow_html=True)