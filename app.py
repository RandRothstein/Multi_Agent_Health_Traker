import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
import os

from knowledge_base import create_knowledge_base
from tools.bmi_tool import bmi_tool
from tools.nutrition_rag import nutrition_tool
from tools.calorie_tool import calorie_tool
from tools.workout_tool import workout_tool

from dotenv import load_dotenv
load_dotenv()



st.title('AI Multi Agent Fitness Genie')

create_knowledge_base()

model = ChatGoogleGenerativeAI(
    model = 'gemini-2.5-flash',
    google_api_key = os.getenv('GOOGLE_API_KEY'),
    temperature = 0
)



tools = [
    bmi_tool,
    calorie_tool,
    workout_tool,
    nutrition_tool
]

agent = create_agent(
    model = model,
    tools = tools
)

user_input = st.text_input("Describe your fitness goal")


if st.button('ASK'):
    if user_input:
        response = agent.invoke({
            "messages": [
                {"role": "user", "content": user_input}
            ]
        })
        
        st.write(response["messages"][-1].content)