# Day 4: Multi-Step Planning Agent

## Objective
To design an AI agent that can handle both simple and complex tasks by breaking them into steps and executing them sequentially.

---

## Approach

The agent follows a planning-based architecture:

Input → LLM Planning → Step Execution → Output

1. The user provides an input query
2. A local LLM (LLaMA3 via Ollama) generates a sequence of steps
3. Each step corresponds to a tool
4. Steps are executed in order
5. Intermediate outputs are displayed
6. Final result is returned

---

## Key Design Decision

Unlike previous phases, this agent:
- Does NOT use rule-based routing
- Uses the LLM for **all decisions**, even simple ones

This ensures:
- Consistent agent behavior
- True AI-driven tool selection
- Alignment with agentic system design

---

## Tools Implemented

- `greeting` → Handles basic greetings
- `calculator` → Performs arithmetic evaluation
- `weather` → Returns mocked weather data
- `extract_numbers` → Extracts numbers from input
- `calculate_average` → Computes average of numbers
- `summarize` → Generates concise output

---

## How It Works

### Step 1: Planning
The LLM receives the user input and generates a sequence of steps.

Example:

Input:
Find average of 5, 10, 15 and summarize


LLM Output:

extract_numbers
calculate_average
summarize


---

### Step 2: Execution

Each step is executed using corresponding tools:

- Extract numbers → [5, 10, 15]  
- Calculate average → 10  
- Summarize → "The average is 10..."

---

### Step 3: Output

Final result is displayed after all steps are completed.

---

## Example Runs

### Example 1
Input:

hi


Steps:

greeting


Output:

Hello! How can I help you?


---

### Example 2
Input:

calculate 5 * 6


Steps:

calculator


Output:

30


---

### Example 3
Input:

find average of 5, 10, 15 and summarize


Steps:

extract_numbers
calculate_average
summarize


Output:

The average is 10...


---

## Features

- LLM-based planning for all inputs
- Multi-step task decomposition
- Sequential execution of steps
- Intermediate output logging
- Modular and reusable tool design
- Fully local (no external API required)

---

## Learning Outcomes

- Understanding planning-based AI agents
- Sequential reasoning and execution
- Tool orchestration using LLMs
- Designing modular agent systems

---

## Notes

- Ollama is used to run LLaMA3 locally
- No external APIs are required
- The agent supports both single-step and multi-step tasks
