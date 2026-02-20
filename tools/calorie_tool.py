from langchain_core.tools import Tool
from tools.extract_llm import extract_user_metrics

def calculate_calorie(input_str:str):
    try:
        metrics = extract_user_metrics(query)
        
        weight = metrics['weight']
        age = metrics['age']
        height = metrics['height']

        bmr = 10*weight + 6.25*height - 5*age + 5
        calories = bmr * 1.55

        return f"Estimated daily calorie intake: {round(calories,2)}"
    except:
        return f"Issue with calorie_tool"

calorie_tool = Tool(
    name = "calorie_tool",
    func = calculate_calorie,
    description = "Calculates the daily calorie needs. Formate:weight,height,age"
)