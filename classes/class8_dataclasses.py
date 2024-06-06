import streamlit as st
from dataclasses import dataclass, field
from typing import Literal, Dict, List

@dataclass
class User:
    username: str = ""
    password: str = "" 
    email: str = "" 
    firstname: str = "" 
    lastname: str = ""
    fullname: str = "" 
    threadid: str = "" 
    vectorid: str = "" 
    createddate: str = ""
    userrole: Literal["Admin", "Athlete", "Coach", "Supporter"]
    paytype: Literal["paid", "unpaid"]

@dataclass
class GuestAssistant:
    assistantid: str = st.secrets.openai.assistantid
    threadid: str = st.secrets.openai.guestthreadid
    vectorid: str = st.secrets.openai.guestvectorid
    runinstructions: str = st.secrets.openai.guestinstructions
    messages: List = []
    