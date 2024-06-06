import streamlit as st
from classes.class0_pagesetup import PageSetup
from app.userstate.userstate0 import app_userstate0

# 0-Render, 1-Info, 2-Payment, 3-Login, 4-Welcome

class UserState:
    def __init__(self):
        self.initialize()
        self.pagesetup = PageSetup()

    def initial_state(self):
        if "userstate" not in st.session_state:
            if st.query_params:
                self.userstate = 3
            else:
                self.userstate = 0
            st.session_state.userstate = self.userstate
        else:
            self.userstate = st.session_state.userstate

    def controller(self):
        if self.userstate == 0:
            self._userstate0()
            self.callback(userstate=1)
        elif self.userstate == 1:
            self._userstate1()
            self.callback(userstate=2)
        elif self.userstate == 2:
            self._userstate2()
            self.callback(userstate=3)
        elif self.userstate == 3:
            self._userstate3()
            self.callback(userstate=4)
        elif self.userstate == 4:
            self._userstate4()

    def callback(self, userstate: int):
        st.session_state.userstate = userstate
        st.rerun()
        

    def _userstate0(self):
        app_userstate0()
        

    def _userstate1(self):
        st.write("a")
        
    def _userstate2(self):
        st.write("a")
        
    def _userstate3(self):
        st.write("a")

    def _userstate4(self, ):
        st.switch_page(page=st.secrets.pages.paths[0])