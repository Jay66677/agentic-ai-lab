import datetime

# -----------------------------
# Tool 1: Calculator
# -----------------------------
def calculator(expression):
    try:
        result = eval(expression)
        return f"Result: {result}"
    except:
        return "Invalid calculation"


# -----------------------------
# Tool 2: Weather (mocked)
# -----------------------------
def get_weather(city="unknown"):
    # mock response (no API needed)
    return f"Weather in {city}: Sunny, 30°C"


# -----------------------------
# Tool 3: Text Summarizer
# -----------------------------
def summarize_text(text):
    # simple summarization (basic logic)
    words = text.split()
    if len(words) <= 10:
        return text
    return " ".join(words[:10]) + "..."
