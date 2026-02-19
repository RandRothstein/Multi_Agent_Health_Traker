from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os
from dotenv import load_dotenv
import streamlit as st
load_dotenv()

@st.cache_resource
def create_knowledge_base():
    embedd = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    google_api_key=os.getenv("GOOGLE_API_KEY")
    )

    loader = PyPDFLoader('data/nutrition.pdf')
    document = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    docs = text_splitter.split_documents(document)
    db = FAISS.from_documents(docs, embedd)
    db.save_local("data/nutrition_index")
    print("Index created successfully.")

if __name__ == "__main__":
    create_knowledge_base()