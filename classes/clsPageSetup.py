import streamlit as st
from streamlit.components.v1 import html
from streamlit_extras.stylable_container import stylable_container as sc
from typing import Literal
from classes import clsUtilities as ut


class PageSetup:
    def __init__(self, type: Literal["standard", "custom"], page_number: int):
        self.type = type
        self.pagenumber = page_number
        self.controller()
    
    def controller(self):
        if self.type == "standard":
            self.get_standard()
        elif self.type == "custom":
            self.get_custom()

    def get_standard(self):
        self._initialize_standard_attributes()
        background = PageUtilities.get_background(type="logo")
        header = PageUtilities.get_standardheader_section(pagenumber=self.pagenumber)
        overview = PageUtilities.get_overview_section(pagenumber=self.pagenumber)

    def get_custom(self):
        self._initialize_custom_attributes()

    def _initialize_standard_attributes(self):
        self.title = st.secrets.pages.titles[self.pagenumber]
        self.subtitle = st.secrets.pages.subtitles[self.pagenumber]
        self.path = st.secrets.pages.paths[self.pagenumber]
        self.icon = st.secrets.pages.icons[self.pagenumber]
        self.header = st.secrets.pages.headers[self.pagenumber]
        self.about = st.secrets.pages.abouts[self.pagenumber]
        self.description = st.secrets.pages.descriptions[self.pagenumber]
    
    def _display_standard(self):
        title = PageUtilities.auto_title(pagenumber=self.pagenumber)
        overview = PageUtilities.get_overview_section(pagenumber=self.pagenumber)

    def _initialize_custom_attributes(self):
        self.title = None

    
   
    
    

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
    
    @staticmethod
    def get_popover_menu(pagenumber: int):
        menu = st.popover(label="Menu", use_container_width=True)
        page_count = st.secrets.pages.count
        with menu:
            for i in range(page_count):
                st.page_link(page=st.secrets.pages.paths[i], label=st.secrets.pages.subtitles[i], disabled=(pagenumber == i))
        return menu
    
    @staticmethod
    def manual_title(title: str, subtitle: str, div: bool=False):
        style = st.secrets.styles.style_title1.format(title, subtitle)
        title_display = st.markdown(body=style, unsafe_allow_html=True)
        if div:
            st.divider()
        return title_display
    
    @staticmethod
    def auto_title(pagenumber: int, div: bool=False):
        title = st.secrets.pages.titles[pagenumber]
        subtitle = st.secrets.pages.subtitles[pagenumber]
        style = st.secrets.styles.style_title1.format(title, subtitle)
        title_display = st.markdown(body=style, unsafe_allow_html=True)
        if div:
            st.divider()
        return title_display
    
    @staticmethod
    def get_userstate_menu():
        menu = st.popover(label="Try It Now")
        with menu:
            newuser_button = st.button(label="Sign Up", type="primary", use_container_width=True)
            existuser_button = st.button(label="Login", type="primary", use_container_width=True)
            if newuser_button:
                st.session_state.userstate = 2
                st.rerun()
            if existuser_button:
                st.session_state.userstate = 4
                st.rerun()

    @staticmethod
    def get_header_titlewithmenu(title: str, subtitle:str, menu_type: Literal["user", "nav"], pagenumber: int, div: bool=True):
        header_container = st.container(border=False)
        with header_container:
            header_subcontainer = st.container(border=False)
            with header_subcontainer:
                header_columns = st.columns([10, 2])
                with header_columns[0]:
                    title = PageUtilities.manual_title(title=title, subtitle=subtitle)
                with header_columns[1]:
                    if menu_type == "nav":
                        menu = PageUtilities.get_popover_menu(pagenumber=pagenumber)
                    elif menu_type == "user":
                        menu = PageUtilities.get_userstate_menu()  
            if div:
                st.divider()
        return header_container
    
    @staticmethod
    def get_material_icon(icon_name: str):
        icon_style = st.secrets.styles.style_icon1_material
        icon = icon_style.format(icon_name)
        return icon

    @staticmethod
    def get_styled_container1(height: int=None, border: bool=False):
        styleouter = st.secrets.styles.style_container1
        styleinner = st.secrets.styles.style_container2
        outer = sc(key="outer", css_styles=styleouter)
        with outer:
            inner = sc(key="inner", css_styles=styleinner)
            with inner:
                if height is not None:
                    container = st.container(height=height, border=border)
                else:
                    container = st.container(border=border)
        return container
    
    @staticmethod
    def get_overview_section(pagenumber: int):
        header_text = st.secrets.pages.headers[pagenumber]
        description_text = st.secrets.pages.descriptions[pagenumber]
        maincontainer = st.container(border=False)
        with maincontainer:
            header = PageUtilities.get_header(type="gray", text=header_text)
            overviewcontainer = PageUtilities.get_styled_container1()
            with overviewcontainer:
                description = st.markdown(description_text)
        st.divider()
        return maincontainer
    
    @staticmethod
    def get_standardheader_section(pagenumber: int):
        header_container = st.container(border=False)
        with header_container:
            header_cols = st.columns([10,3])
            with header_cols[0]:
                title = PageUtilities.auto_title(pagenumber=pagenumber, div=False)
            with header_cols[1]:
                menu = PageUtilities.get_popover_menu(pagenumber=pagenumber)
        st.divider()
        return header_container
