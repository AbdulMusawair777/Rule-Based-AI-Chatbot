"""
Project 1: Rule-Based AI Chatbot
DecodeLabs Industrial Training Kit - Batch 2026

A simple rule-based chatbot demonstrating:
- Continuous input loop (while True)
- Input sanitization (lower + strip)
- Dictionary-based knowledge base (O(1) lookup via .get())
- Fallback response for unrecognized input
- Clean exit strategy
"""

# ---------------------------------------------------------
# PHASE 2: KNOWLEDGE BASE (Dictionary of intents -> responses)
# ---------------------------------------------------------
responses = {
    "hello": "Hi there! How can I help you today?",
    "hi": "Hello! What can I do for you?",
    "how are you": "I'm just a bunch of if-else logic, but I'm doing great! How about you?",
    "what is your name": "I'm RuleBot, your friendly rule-based assistant.",
    "what can you do": "I can chat with you using predefined rules. Try asking me about myself!",
    "help": "You can say hello, ask my name, ask how I am, or type 'bye' to exit.",
    "thank you": "You're welcome!",
    "thanks": "Anytime!",
}

# Exit commands that break the loop
EXIT_COMMANDS = {"bye", "exit", "quit"}


def get_response(user_input: str) -> str:
    """
    Look up the sanitized user input in the knowledge base.
    Falls back to a default response if no match is found.
    """
    return responses.get(user_input, "I do not understand that yet. Try 'help' to see what I can do.")


def chatbot():
    """
    Runs the main chatbot loop (the 'heartbeat').
    Continues until the user issues an exit command.
    """
    print("RuleBot: Hello! I'm RuleBot. Type 'bye' to exit.")

    while True:
        # ---------------------------------------------------------
        # PHASE 1: INPUT & SANITIZATION
        # ---------------------------------------------------------
        raw_input = input("You: ")
        clean_input = raw_input.lower().strip()

        # ---------------------------------------------------------
        # EXIT STRATEGY: Kill command breaks the infinite loop
        # ---------------------------------------------------------
        if clean_input in EXIT_COMMANDS:
            print("RuleBot: Goodbye! Have a great day.")
            break

        # ---------------------------------------------------------
        # PROCESS: Intent matching via dictionary lookup
        # ---------------------------------------------------------
        reply = get_response(clean_input)

        # ---------------------------------------------------------
        # OUTPUT: Response generation
        # ---------------------------------------------------------
        print(f"RuleBot: {reply}")


if __name__ == "__main__":
    chatbot()
