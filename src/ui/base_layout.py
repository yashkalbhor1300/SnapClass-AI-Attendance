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

            /* ============================= */
            /* GOOGLE FONTS */
            /* ============================= */

            @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
            @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');


            /* ============================= */
            /* HIDE STREAMLIT DEFAULT UI */
            /* ============================= */

            #MainMenu,
            footer,
            header {
                visibility: hidden;
            }


            /* ============================= */
            /* MAIN CONTAINER */
            /* ============================= */

            .block-container {
                padding-top: 1.5rem !important;
            }


            /* ============================= */
            /* HEADINGS */
            /* ============================= */

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


            /* ============================= */
            /* NORMAL TEXT */
            /* ============================= */

            p,
            label {
                font-family: 'Outfit', sans-serif !important;
            }


            /* ============================= */
            /* STREAMLIT TEXT */
            /* ============================= */

            [data-testid="stCaptionContainer"],
            [data-testid="stMarkdownContainer"],
            [data-testid="stText"],
            [data-testid="stAlert"] {
                font-family: 'Outfit', sans-serif !important;
            }


            /* ============================= */
            /* INPUTS */
            /* ============================= */

            input,
            textarea,
            select {
                font-family: 'Outfit', sans-serif !important;
            }


            /* ============================= */
            /* SELECTBOX */
            /* ============================= */

            div[data-baseweb="select"] * {
                font-family: 'Outfit', sans-serif !important;
            }


            /* ============================= */
            /* BUTTON CONTAINER */
            /* ============================= */

            div[data-testid="stButton"] {
                width: 100% !important;
                box-sizing: border-box !important;
            }


            /* ============================= */
            /* NORMAL STREAMLIT BUTTONS */
            /* ============================= */

            .stButton > button {
                font-family: 'Outfit', sans-serif !important;
                border-radius: 1.5rem !important;
                background-color: #5865F2 !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                min-height: 45px !important;
                width: 100% !important;
                max-width: 100% !important;
                box-sizing: border-box !important;
                margin: 0 !important;
                transform: none !important;
            }

            .stButton > button p {
                color: white !important;
                font-family: 'Outfit', sans-serif !important;
            }


            /* ============================= */
            /* PRIMARY BUTTON */
            /* ============================= */

            .stButton > button[kind="primary"] {
                background-color: #5865F2 !important;
                color: white !important;
            }


            /* ============================= */
            /* SECONDARY BUTTON */
            /* ============================= */

            .stButton > button[kind="secondary"] {
                background-color: #EB459E !important;
                color: white !important;
            }


            /* ============================= */
            /* TERTIARY BUTTON */
            /* ============================= */

            .stButton > button[kind="tertiary"] {
                background-color: black !important;
                color: white !important;
            }


            /* ============================= */
            /* BUTTON HOVER */
            /* ============================= */

            .stButton > button:hover {
                transform: none !important;
                margin: 0 !important;
            }


            /* ============================= */
            /* CAMERA INPUT */
            /* ============================= */

            div[data-testid="stCameraInput"] button {
                background-color: #5865F2 !important;
                color: white !important;
                border: none !important;
                border-radius: 1.5rem !important;
                font-family: 'Outfit', sans-serif !important;
                box-sizing: border-box !important;
            }

            div[data-testid="stCameraInput"] button p {
                color: white !important;
                font-family: 'Outfit', sans-serif !important;
            }

            div[data-testid="stCameraInput"] button:hover {
                background-color: #4752C4 !important;
                color: white !important;
            }


            /* ============================= */
            /* FILE UPLOADER */
            /* ============================= */

            section[data-testid="stFileUploader"] * {
                font-family: 'Outfit', sans-serif !important;
            }


            /* ============================= */
            /* RADIO BUTTONS */
            /* ============================= */

            div[data-testid="stRadio"] * {
                font-family: 'Outfit', sans-serif !important;
            }


            /* ============================= */
            /* CHECKBOXES */
            /* ============================= */

            div[data-testid="stCheckbox"] * {
                font-family: 'Outfit', sans-serif !important;
            }


            /* ============================= */
            /* METRICS */
            /* ============================= */

            div[data-testid="stMetric"] * {
                font-family: 'Outfit', sans-serif !important;
            }


            /* ============================= */
            /* TABS */
            /* ============================= */

            button[data-baseweb="tab"] {
                font-family: 'Outfit', sans-serif !important;
            }

        </style>
    """, unsafe_allow_html=True)