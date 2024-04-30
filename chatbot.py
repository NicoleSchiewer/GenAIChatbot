import streamlit as streamlit
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# upload PDF files
streamlit.header("My First Chatbot")

with streamlit.sidebar:
    streamlit.title("Your Documents")
    file = streamlit.file_uploader("Upload a PDF file and start asking questions", type="pdf")

# Extract the text
if file is not None:
    pdf_reader = PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()

# Break text into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        separators="\n",
        chunk_size=1000,
        chunk_overlap=150,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    streamlit.write(chunks)