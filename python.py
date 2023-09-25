import streamlit as st
from streamlit_1 import page1  
from streamlit_2 import page2
from streamlit_3 import page3
from streamlit_4 import page4
from streamlit_5 import page5
from streamlit_6 import page6
from streamlit_7 import page7
from streamlit_8 import page8
from streamlit_9 import page9
from streamlit_10 import page10
from streamlit_11 import page11
from streamlit_12 import page12


user_responses = {}
pages = [
    page1, page2, page3, page4, page5, page6,
    page7, page8, page9, page10, page11, page12
]


st.title("Multi-Page Survey App")

current_page_index = st.session_state.get("current_page_index", 0)
current_page = pages[current_page_index]


user_responses.update(current_page())

col1, col2, col3 = st.columns([1, 6, 1])


if col1.button("Previous", key="previous_button"):
    current_page_index = max(current_page_index - 1, 0)


if col3.button("Next", key="next_button"):
    current_page_index = min(current_page_index + 1, len(pages) - 1)


st.session_state["current_page_index"] = current_page_index
