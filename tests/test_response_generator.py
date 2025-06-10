# tests/test_response_generator.py
import unittest
from unittest.mock import patch
import sys
import os

# Add project root to sys.path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# Add src to sys.path for importing response_generator
SRC_PATH = os.path.join(PROJECT_ROOT, 'src')
if SRC_PATH not in sys.path:
    sys.path.insert(1, SRC_PATH)

from response_generator import generate_response
# Assuming faq_handler.get_answer is imported as get_faq_answer in response_generator

class TestResponseGenerator(unittest.TestCase):

    @patch('response_generator.get_faq_answer', return_value="Mocked FAQ Answer")
    def test_faq_query_intent(self, mock_get_faq_answer):
        intent_data = {"type": "faq_query"}
        original_query = "What are the requirements?"
        response = generate_response(intent_data, original_query=original_query)
        mock_get_faq_answer.assert_called_once_with(original_query)
        self.assertEqual(response, "Mocked FAQ Answer")

    @patch('response_generator.get_faq_answer')
    def test_faq_query_with_data_in_intent(self, mock_get_faq_answer):
        mock_get_faq_answer.return_value = "FAQ answer from intent data"
        intent_data = {"type": "faq_query", "data": "some question from intent data"}
        response = generate_response(intent_data, original_query=None) # No original query passed
        mock_get_faq_answer.assert_called_once_with("some question from intent data")
        self.assertEqual(response, "FAQ answer from intent data")

    @patch('response_generator.get_faq_answer')
    def test_faq_query_empty_query(self, mock_get_faq_answer):
        intent_data = {"type": "faq_query"}
        response = generate_response(intent_data, original_query="")
        self.assertIn("question was unclear", response)
        mock_get_faq_answer.assert_not_called()


    def test_exit_app_intent(self):
        intent_data = {"type": "exit_app"}
        response = generate_response(intent_data)
        self.assertIn("Goodbye! Thanks for using Thinkloop.", response)

    def test_unknown_intent(self):
        intent_data = {"type": "unknown_intent"}
        response = generate_response(intent_data)
        self.assertIn("not quite sure how to handle that request", response)

    def test_other_intent_fallback(self):
        intent_data = {"type": "some_other_intent"}
        response = generate_response(intent_data)
        self.assertIn("not equipped to handle that specific request", response)

if __name__ == '__main__':
    unittest.main()
