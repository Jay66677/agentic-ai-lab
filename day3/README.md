# Day 3: LLM-Based Agent (Ollama)

## Objective
To replace rule-based decision making with an LLM.

## Approach
- A local LLM (LLaMA3 via Ollama) is used
- The model decides which tool to use
- Tool is executed and output returned

## Features
- Local AI decision-making (no API)
- Tool selection using LLM
- Logging of:
  - Input
  - Selected tool
  - Output

## Tools
- Calculator
- Weather (mocked)
- Text Summarizer

## Note
Ollama was used to run LLaMA3 locally instead of external APIs.
