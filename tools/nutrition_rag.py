from langchain_core.tools import Tool
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
import os
from dotenv import load_dotenv
load_dotenv()

embedd = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",   # ✅ correct
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

db = FAISS.load_local(
    "data/nutrition_index",
    embedd,
    allow_dangerous_deserialization=True
)

def retrive_nutrition(query:str):
    docs = db.similarity_search(query , k =1)
    return "\n\n".join([doc.page_content for doc in docs])


nutrition_tool = Tool(
    name = "nutrition_tool",
    func = retrive_nutrition,
    description = "Provides nutrition advice from scientific documents."   
)