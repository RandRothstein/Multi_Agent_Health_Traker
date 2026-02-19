from langchain_core.tools import Tool

def calculate_bmi(input_str:str):
    weight,height = map(float,input_str.split(','))
    height_m = height / 100
    bmi = weight / (height_m**2)
    return f"BMI is {round(bmi,2)}"


bmi_tool = Tool(
    name = 'bmi_tool',
    func = calculate_bmi,
    description = 'This tool calculates BMI , Input fomate:weight_in_kg,height_in_cm'
)

