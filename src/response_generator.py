# src/response_generator.py
from faq_handler import get_answer as get_faq_answer # Use an alias to avoid confusion if more funcs are added

def generate_response(intent_data: dict, original_query: str = None) -> str:
    """
    Generates a response string based on the intent.
    - 'intent_data': The dictionary returned by the intent parser.
    - 'original_query': The original text input from the user, primarily for FAQ.
    """
    intent_type = intent_data.get("type")

    print(f"✍️ [ResponseGenerator] Generating response for intent type: {intent_type}")

    if intent_type == "faq_query":
        # Use original_query if provided and valid, otherwise use data from intent_data
        query_text = original_query if original_query else intent_data.get("data", "")
        if not query_text:
            print("⚠️ [ResponseGenerator] No query text found for FAQ.")
            return "I received a request for information, but the question was unclear. Could you please rephrase?"
        print(f"🔍 [ResponseGenerator] Getting FAQ answer for: '{query_text}'")
        return get_faq_answer(query_text)
    elif intent_type == "exit_app":
        return "Goodbye! Thanks for using Thinkloop. Have a great day!"
    elif intent_type == "unknown_intent":
        return "I'm sorry, I'm not quite sure how to handle that request. Could you try phrasing it differently?"
    else: # Default fallback for any other intent types not explicitly handled
        return "I'm not equipped to handle that specific request at the moment. Please try something else."

if __name__ == '__main__':
    print("--- Testing Response Generator ---")

    # Test cases
    test_intents = [
        ({"type": "faq_query"}, "Tell me about admission requirements"),
        ({"type": "faq_query", "data": "What is the deadline?"}, None), # Test with data in intent
        ({"type": "exit_app"}, None),
        ({"type": "unknown_intent"}, "gibberish input here"),
        ({"type": "some_other_future_intent"}, "some data")
    ]

    for intent, query in test_intents:
        response = generate_response(intent, original_query=query)
        print(f"Intent: {intent}, Query: '{query}' -> Response: '{response}'")

    # Test FAQ with empty query
    response_empty_faq = generate_response({"type": "faq_query"}, "")
    print(f"Intent: faq_query, Query: '' -> Response: '{response_empty_faq}'")
