import streamlit as st

VERSION = "1.30"

st.set_page_config(
    page_title=f"Streamlit App",
    page_icon=':memo:',
    initial_sidebar_state="expanded",
    layout="wide",
)

intro = "This example streamlit app to deploy to Azure App Service with GitHub Action. " \

text = f"""

**Highlights**

- Hello World!
"""
def draw_main_page():

    st.title(f"Streamlit App Sample! :wave:", anchor=False)

    st.caption(intro)

    st.write(text)

draw_main_page()
