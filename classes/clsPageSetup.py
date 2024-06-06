import streamlit as st
from streamlit.components.v1 import html
from streamlit_extras.stylable_container import stylable_container as sc
from typing import Literal
from classes import clsUtilities as ut


class PageSetup:
    def __init__(self):
        self._initialize_attributes()

    def get(self, page_number: int):
        self.title = st.secrets.titles[page_number]
        self.subtitle = st.secrets.subtitles[page_number]
        self.path = st.secrets.paths[page_number]
        self.icon = st.secrets.icons[page_number]
        self.header = st.secrets.headers[page_number]
        self.about = st.secrets.abouts[page_number]
        self.description = st.secrets.descriptions[page_number]
    
    @staticmethod
    def get_background(type: Literal["logo", "wrestler", "coach"]):
        if type == "logo":
            path = st.secrets.paths.logo
        elif type == "coach":
            path = st.secrets.paths.coach
        elif type == "wrestler":
            path = st.secrets.paths.wrestler
        else:
            path = st.secrets.paths.logo
        encoded_string = ut.Utilities.encode_image(image_path=path)
        background = st.secrets.styles.style_background6.format(encoded_string)
        st.markdown(body=background, unsafe_allow_html=True)

    @staticmethod
    def get_pagestyling():
        path = st.secrets.paths.css
        with open(path) as file:
            css_content = file.read()
            css = st.secrets.styles.style_css1.format(css_content)
            st.markdown(body=css, unsafe_allow_html=True)


    @staticmethod
    def get_header(type: Literal["blue", "gray", "green"], text: str):
        if type == "blue":
            content = st.secrets.styles.style_header3_blue.format(text)
        elif type == "gray":
            content = st.secrets.styles.style_header2_gray.format(text)
        elif type == "green":
            content = st.secrets.styles.style_header1_green.format(text)
        header = st.markdown(body=content, unsafe_allow_html=True)
        return header

class PageUtilities:
    @staticmethod
    def get_background(type: Literal["logo", "wrestler", "coach"]):
        if type == "logo":
            path = st.secrets.paths.logo
        elif type == "coach":
            path = st.secrets.paths.coach
        elif type == "wrestler":
            path = st.secrets.paths.wrestler
        else:
            path = st.secrets.paths.logo
        encoded_string = ut.Utilities.encode_image(image_path=path)
        background = st.secrets.styles.style_background6.format(encoded_string)
        st.markdown(body=background, unsafe_allow_html=True)
    
    @staticmethod
    def get_background_dialog(type: Literal["dialog1", "dialog2", "dialog3", "dialog4"]):
        if type == "dialog1":
            path = st.secrets.paths.dialog1
            style = st.secrets.styles.style_dialog1
        elif type == "dialog2":
            path = st.secrets.paths.dialog2
            style = st.secrets.styles.style_dialog2
        elif type == "dialog3":
            path = st.secrets.paths.dialog3
            style = st.secrets.styles.style_dialog3
        elif type == "dialog4":
            path = st.secrets.paths.dialog4
            style = st.secrets.styles.style_dialog4
        encoded = ut.Utilities.encode_image(image_path=path)
        dialog = style.format(encoded)
        st.markdown(dialog, unsafe_allow_html=True)
        

    @staticmethod
    def get_pagestyling():
        path = st.secrets.paths.css
        with open(path) as file:
            css_content = file.read()
            css = st.secrets.styles.style_css1.format(css_content)
            st.markdown(body=css, unsafe_allow_html=True)
    
    @staticmethod
    def get_header(type: Literal["blue", "gray", "green"], text: str):
        if type == "blue":
            content = st.secrets.styles.style_header3_blue.format(text)
        elif type == "gray":
            content = st.secrets.styles.style_header2_gray.format(text)
        elif type == "green":
            content = st.secrets.styles.style_header1_green.format(text)
        header = st.markdown(body=content, unsafe_allow_html=True)
        return header
        