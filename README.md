# Project 1: Rule-Based AI Chatbot 🤖

**DecodeLabs Industrial Training Kit — Batch 2026**

## Overview

This is a simple rule-based chatbot built as the foundation project for the AI Engineer track at DecodeLabs. Instead of using machine learning or deep learning, this bot relies on **explicit control flow and dictionary lookups** to simulate a basic conversational interface — the "logic engine" that underlies more advanced AI guardrail systems.

## Goal

Create a rule-based chatbot that:
- Responds to predefined user inputs
- Handles greetings and exit commands
- Uses a knowledge base (dictionary) instead of long if-elif chains
- Runs in a continuous input loop until told to stop

## Key Skills Practiced

- Control flow and decision-making logic
- Input sanitization (case-insensitive, whitespace-safe matching)
- Dictionary-based (`O(1)`) intent matching using `.get()`
- Designing a clean exit strategy for an infinite loop

## Files

| File | Description |
|---|---|
| `chatbot.py` | Main chatbot program |
| `requirements.txt` | Dependency list (none required) |
| `README.md` | This file |

## Requirements

- Python 3.7 or higher
- No external packages needed (uses only Python built-ins)

## How to Run

1. Open this folder in VS Code.
2. Open `chatbot.py`.
3. Run it:
   - Click the **Run ▶** button in VS Code, **or**
   - Open a terminal and run:
     ```bash
     python chatbot.py
     ```
     (use `python3` on macOS/Linux if `python` isn't recognized)
4. Chat with the bot! Type `bye`, `exit`, or `quit` to end the conversation.

## Example Interaction

```
RuleBot: Hello! I'm RuleBot. Type 'bye' to exit.
You: hello
RuleBot: Hi there! How can I help you today?
You: what is your name
RuleBot: I'm RuleBot, your friendly rule-based assistant.
You: banana
RuleBot: I do not understand that yet. Try 'help' to see what I can do.
You: bye
RuleBot: Goodbye! Have a great day.
```

## How It Works

1. **Input & Sanitization** — raw text is lowercased and stripped of extra whitespace so `"Hello "`, `"hello"`, and `"HELLO"` are all treated the same.
2. **Knowledge Base** — a Python dictionary maps recognized phrases (intents) to responses, giving instant `O(1)` lookups instead of a slow, hard-to-maintain `if/elif` ladder.
3. **Fallback** — `.get()` returns a default "I don't understand" message for any unmatched input, in a single atomic lookup-and-fallback operation.
4. **Loop & Exit** — a `while True` loop keeps the conversation going until the user types an exit command, which triggers a `break`.

## Ideas to Extend This Project

- Add more intents/responses to `responses` in `chatbot.py`
- Match on keywords instead of exact phrases (e.g. check if a word appears in the input)
- Give the bot a unique personality or name
- Add simple state/memory (e.g. remember the user's name across the conversation)
- Log conversations to a file

## Qualification Criteria

- ✅ Complete this project to unlock future weekly projects
- ✅ Ensure code is clean, tested, and verified before submission
- ✅ This is the mandatory starting point for every DecodeLabs AI intern

---

**DecodeLabs**
📞 +91 89330 06408 · ✉️ decodelabs.tech@gmail.com · 🌐 www.decodelabs.tech
📍 Greater Lucknow, India
