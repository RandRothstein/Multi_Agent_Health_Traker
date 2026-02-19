from langchain_core.tools import Tool


def calculate_calorie(input_str:str):
    weight,height,age = map(float,input_str.split(','))

    bmr = 10*weight + 6.25*height - 5*age + 5
    calories = bmr * 1.55

    return f"Estimated daily calorie intake: {round(calories,2)}"


calorie_tool = Tool(
    name = "calorie_tool",
    func = calculate_calorie,
    description = "Calculates the daily calorie needs. Formate:weight,height,age"
)