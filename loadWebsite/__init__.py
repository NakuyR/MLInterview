# streamlit
import streamlit as st
import streamlit.components.v1 as components

# Web Design
from loadWebsite.websiteCommon import css_nicepage, js_topbar
from loadWebsite.websiteMain   import html_main, css_main, js_main
from loadWebsite.websiteTest   import html_test, css_test, js_test
from loadWebsite.websiteAbout  import html_about

questionList = []

def loadHomePage():
    #html
    st.markdown(
        html_main.returnHtml(),
        unsafe_allow_html=True
    )

    #css
    st.markdown(
        css_main.returnCss(),
        unsafe_allow_html=True
    )

    st.markdown(
        css_nicepage.returnCss(),
        unsafe_allow_html=True
    )

    #js
    components.html(
        js_topbar.returnJs()
    )

    components.html(
        js_main.returnJs()
    )

def loadTestPage():
    #html
    html_test.resetQuestion()

    html_test.htmlHeader()

    for str in questionList:
        html_test.addQuestion(str)

    html_test.htmlFooter()

    #css
    st.markdown(
        css_nicepage.returnCss(),
        unsafe_allow_html=True
    )

    st.markdown(
        css_test.returnCss(),
        unsafe_allow_html=True
    )

    #js
    components.html(
        js_topbar.returnJs()
    )

    components.html(
        js_test.returnJs()
    )

def loadAboutPage():
    #html
    st.markdown(
        html_about.returnHtml(),
        unsafe_allow_html=True
    )

    #css
    st.markdown(
        css_main.returnCss(),
        unsafe_allow_html=True
    )
    
    st.markdown(
        css_nicepage.returnCss(),
        unsafe_allow_html=True
    )

    #js
    components.html(
        js_topbar.returnJs()
    )

def resetQuestion():
    global questionList
    questionList = []

def addQuestion(str):
    questionList.append(str)