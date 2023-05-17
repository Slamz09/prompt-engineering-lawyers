import streamlit as st


def use_custom_css():
    with open("custom.css") as custom_css:
        return st.write(f'<style>{custom_css.read()}</style>', unsafe_allow_html=True)


def check_openai_key():
    if st.session_state.get("api_success", False) is False:
        return st.warning("""
        No OpenAI key was found! Click Home in the Sidebar, enter your API Key and return here.
        
        If you don't set the OpenAI Key, none of the exercises here will work.
        """, icon="🤦‍♀️")
