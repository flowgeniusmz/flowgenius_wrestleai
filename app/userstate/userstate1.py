import streamlit as st


@st.experimental_dialog(title="New User Registration", width="large")
def app_userstate1():
    st.session_state.usertype = "new"