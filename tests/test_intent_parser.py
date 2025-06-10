# tests/test_intent_parser.py
import unittest
import sys
import os

# Add project root to sys.path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# Add src to sys.path for importing intent_parser
SRC_PATH = os.path.join(PROJECT_ROOT, 'src')
if SRC_PATH not in sys.path:
    sys.path.insert(1, SRC_PATH)

from intent_parser import get_intent, EXIT_KEYWORDS, FAQ_INDICATORS

class TestIntentParser(unittest.TestCase):

    def test_exit_intent(self):
        for keyword in EXIT_KEYWORDS:
            intent = get_intent(f"I want to {keyword} now")
            self.assertEqual(intent["type"], "exit_app")
            intent_direct = get_intent(keyword)
            self.assertEqual(intent_direct["type"], "exit_app")

    def test_faq_intent_indicators(self):
        # Basic check, more robust tests would involve more varied phrases
        test_phrases = [
            "What are the admission requirements?",
            "Tell me about deadlines",
            "how much is tuition",
            "any scholarships?"
        ]
        for phrase in test_phrases:
            intent = get_intent(phrase)
            self.assertEqual(intent["type"], "faq_query", f"Failed for phrase: {phrase}")

    def test_unknown_intent_if_not_strong_faq_signal(self):
        # Based on current intent_parser logic, non-exit phrases default to faq_query
        # This test reflects that; if logic changes, test needs update.
        intent = get_intent("This is a generic statement.")
        self.assertEqual(intent["type"], "faq_query") # Current default
        self.assertEqual(intent.get("message"), "Defaulted to FAQ query.")


    def test_empty_input(self):
        intent = get_intent("")
        self.assertEqual(intent["type"], "unknown_intent")
        self.assertIn("Input was empty", intent.get("message", ""))
        intent_space = get_intent("   ")
        self.assertEqual(intent_space["type"], "unknown_intent")
        self.assertIn("Input was empty", intent_space.get("message", ""))

if __name__ == '__main__':
    unittest.main()
