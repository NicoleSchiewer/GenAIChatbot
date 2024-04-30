import streamlit as streamlit

#upload PDF files
streamlit.header("My First Chatbot")

with streamlit.sidebar:
    streamlit.title("Your Documents")
    file = streamlit.file_uploader("Upload a PDF file and start asking questions", type="pdf")