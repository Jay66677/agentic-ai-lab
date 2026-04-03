import datetime
import re

# -----------------------------
# Input Handler
# -----------------------------
def get_user_input():
    return input("Enter command: ").lower()


# -----------------------------
# Decision Logic
# -----------------------------
def identify_intent(user_input):
    if "hello" in user_input:
        return "greeting"
    elif "date" in user_input:
        return "date"
    elif "calculate" in user_input:
        return "calculation"
    else:
        return "unknown"


# -----------------------------
# Action Execution
# -----------------------------
def execute_action(intent, user_input):
    if intent == "greeting":
        return "Hello! How can I help you?"

    elif intent == "date":
        return str(datetime.date.today())

    elif intent == "calculation":
        # extract math expression
        expression = user_input.replace("calculate", "").strip()
        try:
            result = eval(expression)
            return f"Result: {result}"
        except:
            return "Invalid calculation"

    else:
        return "Sorry, I didn't understand that."


# -----------------------------
# Main Agent Loop
# -----------------------------
def run_agent():
    while True:
        user_input = get_user_input()

        if user_input in ["exit", "quit"]:
            print("Exiting agent...")
            break

        intent = identify_intent(user_input)
        response = execute_action(intent, user_input)

        print(response)


if __name__ == "__main__":
    run_agent()
