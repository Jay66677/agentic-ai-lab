from tools import calculator, get_weather, summarize_text
import re

# -----------------------------
# Input Handler
# -----------------------------
def get_user_input():
    return input("Enter command: ").lower()


# -----------------------------
# Decision Logic (Tool Selection)
# -----------------------------
def select_tool(user_input):
    if "calculate" in user_input:
        return "calculator"
    elif "weather" in user_input:
        return "weather"
    elif "summarize" in user_input:
        return "summarizer"
    elif "hello" in user_input:
        return "greeting"
    else:
        return "unknown"


# -----------------------------
# Tool Execution
# -----------------------------
def execute_tool(tool_name, user_input):
    if tool_name == "calculator":
        expression = user_input.replace("calculate", "").strip()
        return calculator(expression)

    elif tool_name == "weather":
        # extract city if given
        words = user_input.split()
        city = words[-1] if len(words) > 1 else "your area"
        return get_weather(city)

    elif tool_name == "summarizer":
        text = user_input.replace("summarize", "").strip()
        return summarize_text(text)

    elif tool_name == "greeting":
        return "Hello! How can I help you?"

    else:
        return "I don't understand the request."


# -----------------------------
# Main Agent Loop
# -----------------------------
def run_agent():
    while True:
        user_input = get_user_input()

        if user_input in ["exit", "quit"]:
            print("Exiting...")
            break

        tool = select_tool(user_input)
        response = execute_tool(tool, user_input)

        print(response)


if __name__ == "__main__":
    run_agent()
