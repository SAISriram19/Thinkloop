# tests/test_simulated_call_handler.py
import unittest
from unittest.mock import patch
import sys
import os

# Adjust path to import from src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from simulated_call_handler import receive_simulated_call, process_input, send_simulated_response
# Note: 'get_answer' is imported within simulated_call_handler.py, so we patch it there.

class TestSimulatedCallHandler(unittest.TestCase):

    @patch('builtins.input', return_value='Hello there')
    def test_receive_simulated_call(self, mock_input):
        self.assertEqual(receive_simulated_call(), 'Hello there')
        mock_input.assert_called_once()

    @patch('simulated_call_handler.get_answer', return_value='FAQ Answer: Yes')
    def test_process_input_uses_faq_handler(self, mock_get_answer):
        user_text = "Do you offer scholarships?"
        expected_response = 'FAQ Answer: Yes'
        actual_response = process_input(user_text)
        mock_get_answer.assert_called_once_with(user_text)
        self.assertEqual(actual_response, expected_response)

    @patch('builtins.print')
    def test_send_simulated_response(self, mock_print):
        response_text = "This is a test response."
        send_simulated_response(response_text)
        # Check if print was called with the formatted string
        mock_print.assert_any_call(f"📢 [Simulated Call Handler] Sending response: '{response_text}'")

if __name__ == '__main__':
    unittest.main()
