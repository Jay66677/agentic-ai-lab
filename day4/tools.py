import re

# -----------------------------
# Calculator Tool (safer)
# -----------------------------
def calculator(expression):
    try:
        allowed_chars = "0123456789+-*/(). "
        if not all(char in allowed_chars for char in expression):
            return {"error": "Invalid characters"}

        result = eval(expression)
        return {"result": result}

    except:
        return {"error": "Calculation failed"}


# -----------------------------
# Extract Numbers Tool
# -----------------------------
def extract_numbers(text):
    numbers = list(map(int, re.findall(r"\d+", text)))
    return {"numbers": numbers}


# -----------------------------
# Average Tool
# -----------------------------
def calculate_average(numbers):
    if not numbers:
        return {"error": "No numbers provided"}

    avg = sum(numbers) / len(numbers)
    return {"average": avg}


# -----------------------------
# Weather Tool (mocked)
# -----------------------------
def get_weather(city="unknown"):
    return {"weather": f"Sunny, 30°C in {city}"}


# -----------------------------
# Text Summarizer Tool
# -----------------------------
def summarize_text(text):
    words = text.split()

    if len(words) <= 10:
        return {"summary": text}

    return {"summary": " ".join(words[:10]) + "..."}


# -----------------------------
# Greeting Tool
# -----------------------------
def greeting():
    return {"message": "Hello! How can I help you?"}
