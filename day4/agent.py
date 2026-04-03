import requests
from tools import (
    extract_numbers,
    calculate_average,
    summarize_text,
    calculator,
    get_weather,
    greeting
)

# -----------------------------
# Input
# -----------------------------
def get_user_input():
    return input("Enter command: ")


# -----------------------------
# LLM Planning (FOR ALL INPUTS)
# -----------------------------
def plan_steps(user_input):
    prompt = f"""
You are an AI agent.

Break the user request into steps using ONLY these tools:

- greeting
- calculator
- weather
- extract_numbers
- calculate_average
- summarize

Rules:
- Return only tool names
- One per line
- No explanation
- Even for simple inputs, return ONE step

Examples:

Input: hi
Output:
greeting

Input: calculate 5+2
Output:
calculator

Input: weather hyderabad
Output:
weather

Input: find average of 5,10,15 and summarize
Output:
extract_numbers
calculate_average
summarize

Now process:

Input: {user_input}
"""

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            }
        )

        raw = response.json()["response"].strip().lower().split("\n")
        steps = [s.strip() for s in raw if s.strip()]
        return steps

    except:
        return []


# -----------------------------
# Execute Steps
# -----------------------------
def execute_steps(steps, user_input):
    data = {}

    for step in steps:
        print(f"\n[STEP] {step}")

        if "greeting" in step:
            res = greeting()
            print("Output:", res)
            return res

        elif "weather" in step:
            city = user_input.split()[-1]
            res = get_weather(city)
            print("Output:", res)
            return res

        elif "calculator" in step:
            expr = user_input.replace("calculate", "").strip()
            res = calculator(expr)
            print("Output:", res)
            return res

        elif "extract" in step:
            res = extract_numbers(user_input)
            data["numbers"] = res.get("numbers", [])
            print("Output:", res)

        elif "average" in step:
            res = calculate_average(data.get("numbers", []))
            data["average"] = res.get("average")
            print("Output:", res)

        elif "summarize" in step:
            text = f"The average is {data.get('average')}"
            res = summarize_text(text)
            print("Output:", res)
            return res

    return data


# -----------------------------
# Main Agent
# -----------------------------
def run_agent():
    while True:
        user_input = get_user_input()

        if user_input.lower() in ["exit", "quit"]:
            print("Exiting agent...")
            break

        # ALWAYS use LLM
        steps = plan_steps(user_input)

        print("\nPlanned Steps:")
        for s in steps:
            print("-", s)

        final_output = execute_steps(steps, user_input)

        print("\nFinal Output:", final_output)


# -----------------------------
# Entry
# -----------------------------
if __name__ == "__main__":
    run_agent()
