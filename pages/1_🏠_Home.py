import streamlit as st
from classes.class0_pagesetup import PageSetup
from app import app_athlete, app_coach, app_supporter

# 1. Set ST PAGE CONFIG
st.set_page_config(page_icon=st.secrets.app.icon, page_title=st.secrets.app.title, layout=st.secrets.app.layout, initial_sidebar_state=st.secrets.app.sidebar)

# 2. Set Page Setup
pagenumber = 0
PageSetup(pagenumber=pagenumber).display_auto()

# 3. Display App
if st.session_state.userrole == "athlete":
    app_athlete.app_athlete()
elif st.session_state.userrole == "coach":
    app_coach.app_coach()
elif st.session_state.userrole == "supporter":
    app_supporter.app_supporter()



