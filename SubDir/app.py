import streamlit as st

VERSION = "1.30"

st.set_page_config(
    page_title=f"SubDir App",
    page_icon=':memo:',
    initial_sidebar_state="expanded",
    layout="wide",
)

intro = "This example streamlit app to deploy to Azure App Service with GitHub Action. " \

text = f"""

**Highlights**

- This is a subdirectory app
"""
def draw_main_page():

    st.title(f"Streamlit App Sample! :wave:", anchor=False)

    st.caption(intro)

    st.write(text)

draw_main_page()
