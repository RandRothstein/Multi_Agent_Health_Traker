import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import json

load_dotenv()

extract_model = ChatGoogleGenerativeAI(
    model = 'gemini-2.5-flash',
    google_api_key = os.getenv('GOOGLE_API_KEY'),
    temperature = 0
)

def extract_user_metrics(query:str):
    """
    Use Gemini to extract weight (kg), height (cm) and age(years) from natural language query.
    Returns dictionary.
    """
    
    prompt = f""" 
    Extract the following information from the user query.

    Return ONLY valid JSON in this format:
    {{
        "weight": float or null,
        "height": float or null,
        "age": int or null
    }}
    
    Rules:
    - Weight mush be in kilograms.
    - Height mush be in centimeters.
    - If missing , return "Give more information such as height, weight and age"
    
    User Query:
    {query}
    """

    response = extract_model.invoke(prompt)

    try:
        data = json.loads(response.content)
        return data
    except:
        return {
            "weight":None,
            "age":None,
            "height":None
        }
    