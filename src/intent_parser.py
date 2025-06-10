# src/intent_parser.py
import re

# Predefined keywords for intents (very basic for now)
EXIT_KEYWORDS = ["exit", "quit", "bye", "goodbye"]
FAQ_INDICATORS = [
    "what", "how", "when", "who", "where", "why", "tell me about", "can you", "do you",
    "requirements", "deadline", "tuition", "scholarships", "programs", "tour", "contact", "status"
] # More keywords could be added from faq_handler.py's keywords for better coverage

def get_intent(text_input: str) -> dict:
    """
    Parses the user's text input to determine their intent.
    Returns a dictionary with 'type' (intent name) and 'data' (original input or parts of it).
    """
    text_lower = text_input.lower().strip()
    words = set(re.findall(r'\b\w+\b', text_lower))

    if not text_lower: # Handle empty input
        return {"type": "unknown_intent", "data": text_input, "message": "Input was empty."}

    # Check for exit intent
    for keyword in EXIT_KEYWORDS:
        if keyword in words:
            return {"type": "exit_app", "data": text_input}

    # Check for FAQ indicators (very basic)
    # This is a simplistic check. A more robust solution might use more keywords,
    # scoring, or eventually ML models.
    for indicator in FAQ_INDICATORS:
        if indicator in text_lower: # Checking substring for multi-word indicators
            return {"type": "faq_query", "data": text_input}

    # If no strong indicators for FAQ, but it's not an exit command,
    # for now, we can default to faq_query if it's not empty,
    # or a more specific unknown/clarification intent later.
    # For this basic stub, let's assume if not exit, it's a potential FAQ.
    if text_lower: # If it's not empty and not an exit command
         return {"type": "faq_query", "data": text_input, "message": "Defaulted to FAQ query."}


    # Default if no other intent is matched
    return {"type": "unknown_intent", "data": text_input}

if __name__ == '__main__':
    print("--- Testing Intent Parser ---")
    test_phrases = [
        "Tell me about admission requirements",
        "What is the application deadline?",
        "How much is tuition?",
        "exit",
        "I want to quit",
        "Just some random statement.",
        "Can you help with scholarships?",
        "",
        "   "
    ]
    for phrase in test_phrases:
        intent = get_intent(phrase)
        print(f"Input: '{phrase}' -> Intent: {intent}")
