import requests
from tools import calculator, get_weather, summarize_text

# -----------------------------
# Input
# -----------------------------
def get_user_input():
    return input("Enter command: ")


# -----------------------------
# LLM Decision (Ollama)
# -----------------------------
def decide_tool(user_input):
    prompt = f"""
You are an AI agent.

Available tools:
- calculator
- weather
- summarizer
- greeting

Rules:
- Respond with ONLY one tool name
- No explanation

User input: {user_input}
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

        result = response.json()["response"].strip().lower()

        # sanitize output
        if "calculator" in result:
            return "calculator"
        elif "weather" in result:
            return "weather"
        elif "summarizer" in result:
            return "summarizer"
        elif "greeting" in result or "hello" in result:
            return "greeting"
        else:
            return "unknown"

    except Exception as e:
        return "unknown"


# -----------------------------
# Tool Execution
# -----------------------------
def execute_tool(tool, user_input):
    if tool == "calculator":
        expression = user_input.replace("calculate", "").strip()
        return calculator(expression)

    elif tool == "weather":
        words = user_input.split()
        city = words[-1] if len(words) > 1 else "your area"
        return get_weather(city)

    elif tool == "summarizer":
        text = user_input.replace("summarize", "").strip()
        return summarize_text(text)

    elif tool == "greeting":
        return "Hello! How can I help you?"

    else:
        return "Tool not recognized."


# -----------------------------
# Logging (MANDATORY)
# -----------------------------
def log_step(user_input, tool, output):
    print("\n--- LOG ---")
    print(f"Input: {user_input}")
    print(f"Selected Tool: {tool}")
    print(f"Output: {output}")
    print("------------\n")


# -----------------------------
# Main Loop
# -----------------------------
def run_agent():
    while True:
        user_input = get_user_input()

        if user_input.lower() in ["exit", "quit"]:
            break

        tool = decide_tool(user_input)
        output = execute_tool(tool, user_input)

        log_step(user_input, tool, output)
        print(output)


if __name__ == "__main__":
    run_agent()
