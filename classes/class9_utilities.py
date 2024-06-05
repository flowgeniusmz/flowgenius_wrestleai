import streamlit as st
import base64

class Utilities:
    @staticmethod
    def encode_image( image_path: str):
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
            return encoded_string