from langchain_core.tools import Tool
from tools.bmi_tool import calculate_bmi

def basic_workout(input_str:str):
    
    try:
        weight = re.search(r'weight.*?(\d+)', input_str, re.IGNORECASE)
        height = re.search(r'height.*?(\d+)', input_str, re.IGNORECASE)
        bmi = calculate_bmi(weight,height)
        print(f"bmi calculated")
    except:
        return "Missing height and weight"
    
    if bmi < 18.5:
        level = "Beginner (Underweight)"
        plan = """
        Focus: Muscle gain
        Monday: Light Full Body
        Wednesday: Resistance Training
        Friday: Strength Training
        """

    elif 18.5 <= bmi < 25:
        level = "Intermediate"
        plan = """
        Focus: Balanced fitness
        Monday: Upper Body
        Tuesday: Cardio
        Thursday: Lower Body
        Saturday: HIIT
        """

    elif 25 <= bmi < 30:
        level = "Beginner (Fat Loss)"
        plan = """
        Focus: Fat loss
        Monday: Full Body Circuit
        Wednesday: Brisk Walking
        Friday: Strength + Core
        """

    else:
        level = "Beginner (Obesity - Low Impact)"
        plan = """
        Focus: Low impact fat loss
        Monday: Walking
        Wednesday: Light Exercises
        Friday: Cycling / Swimming
        """

    return f"""
    BMI: {bmi}
    Level:{level}
    Workout Plan:
    {plan}"""

workout_tool = Tool(
    name="workout_tool",
    func = basic_workout,
    description  = "Generates workout plan based on body metrics. Format:weight_in_kg,height_in_cm"
)

