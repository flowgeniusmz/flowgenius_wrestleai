import streamlit as st
from classes.class0_pagesetup import PageSetup

def app_userstate0():
    pagenumber = 0                                                                                          # Set arbitrary value since used on main.py
    ps = PageSetup(pagenumber=pagenumber)                                                                      # Explicitly set so we can reference it
    ps.get_backgroud_image(image_type="logo")                                                               # Set background image
    header = ps.display_manual()                                                                            # Display the manual header defined in Pagesetup class
    body_container = st.container(border=False)                                                             # Set a container for the body
    with body_container:
        body_cols = st.columns([1, 7, 1, 20,1])
        with body_cols[1]:
            usertype_container = ps.get_styled_container2(height=400, border=False)
            with usertype_container:
                usertype_header = ps.get_styled_header(type="gray", text="Sign In or Join Today!")
                usertype_popover = st.popover(label="Join Today or Sign In!", use_container_width=True)
                with usertype_popover:
                    newuser_button = st.button(label="New User Registration", type="primary")
                    existuser_button = st.button(label="Sign In Now", type="primary")
        with body_cols[3]:
            chat_container = ps.get_styled_container2(height=300, border=False)                             # Set containers first - chat
            prompt_container = st.container(height=100, border=False)                                       # Set containers first - prompt
            with chat_container:
                guestmessages = [{"role": "assistant", "content": st.secrets.openai.guestinitialmessage}]
                for guestmessage in guestmessages:
                    with st.chat_message(name=guestmessage['role']):
                        st.markdown(guestmessage['content'])
            with prompt_container:
                guestprompt = st.chat_input(placeholder="Enter your question here...", key="guestprompt")
                


