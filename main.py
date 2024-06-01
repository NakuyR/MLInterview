# streamlit
import streamlit as st
import streamlit.components.v1 as components
from streamlit_pages.streamlit_pages import MultiPage

import loadWebsite

answerList = []

def home():
    loadWebsite.loadHomePage()

def test():
    loadWebsite.resetQuestion()

    loadWebsite.addQuestion("일이삼사오육칠팔구십")
    loadWebsite.addQuestion("12345678910")
    loadWebsite.addQuestion("onetwothreefourfive")
    loadWebsite.addQuestion("하나둘셋넷다섯여섯일곱")

    loadWebsite.loadTestPage()

    st.write(st.session_state.reply1)   # 답변 1번 (st.session_state.reply1 or st.session_state[reply1])
    st.write(st.session_state.reply1)   # 답변 2번 (st.session_state.reply2 or st.session_state[reply2])

def about():
    loadWebsite.loadAboutPage()

app = MultiPage()

app.add_page("Home", home)
app.add_page("Test", test)
app.add_page("About", about)

app.run()
