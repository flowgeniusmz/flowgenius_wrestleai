import streamlit as st
import base64

class Utilities:
    def encode_image(self, image_path: str):
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
            return encoded_string