import streamlit as st


def style_background_home():
    st.markdown(
        """
        <style>
            .stApp,
            [data-testid="stAppViewContainer"] {
                background: #5865F2 !important;
            }
        </style>
        """,
        unsafe_allow_html=True
    )


def style_background_dashboard():
    st.markdown(
        """
        <style>
            .stApp,
            [data-testid="stAppViewContainer"] {
                background: #E0E3FF !important;
            }
        </style>
        """,
        unsafe_allow_html=True
    )


def style_base_layout():
    st.markdown(
        """
        <style>

            @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
            @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

            /* Hide Streamlit UI */
            #MainMenu,
            footer,
            header,
            [data-testid="stHeader"] {
                visibility: hidden;
            }

            /* Main container */
            .block-container {
                padding-top: 1.5rem !important;
            }

            /* Headings */
            h1,
            h2 {
                font-family: "Climate Crisis", sans-serif !important;
                color: #E0E3FF !important;
            }

            h1 {
                font-size: 3.5rem !important;
                line-height: 1.1 !important;
                margin-bottom: 0rem !important;
            }

            h2 {
                font-size: 3.5rem !important;
                line-height: 1 !important;
                margin-bottom: 0rem !important;
            }

            h3,
            h4,
            p {
                font-family: "Outfit", sans-serif !important;
            }


            /* PRIMARY BUTTON */

            button[kind="primary"],
            [data-testid="stBaseButton-primary"] {
                border-radius: 1.5rem !important;
                background: black  !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            }


            /* SECONDARY BUTTON */

            button[kind="secondary"],
            [data-testid="stBaseButton-secondary"] {
                border-radius: 1.5rem !important;
                background: black !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            }


            /* TERTIARY BUTTON */

            button[kind="tertiary"],
            [data-testid="stBaseButton-tertiary"] {
                border-radius: 1.5rem !important;
                background: #EB459E !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            }

        </style>
        """,
        unsafe_allow_html=True
    )