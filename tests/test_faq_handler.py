# tests/test_faq_handler.py

import unittest
import sys
import os

# Adjust the path to import from the src directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from faq_handler import get_answer, PREDEFINED_FAQS

class TestFAQHandler(unittest.TestCase):

    def test_known_questions(self):
        """Test that known questions return their predefined answers."""
        for question, expected_answer in PREDEFINED_FAQS.items():
            # Test with exact casing as in keys (though function converts to lower)
            self.assertEqual(get_answer(question), expected_answer)
            # Test with different casing
            self.assertEqual(get_answer(question.upper()), expected_answer)
            self.assertEqual(get_answer(question.capitalize()), expected_answer)

    def test_unknown_question(self):
        """Test that an unknown question returns the default fallback message."""
        unknown_question = "What is the meaning of life?"
        expected_fallback = "I'm sorry, I don't have an answer to that question right now. Please try asking something else or contact our admissions office."
        self.assertEqual(get_answer(unknown_question), expected_fallback)

    def test_empty_question(self):
        """Test that an empty question returns the fallback message."""
        expected_fallback = "I'm sorry, I don't have an answer to that question right now. Please try asking something else or contact our admissions office."
        self.assertEqual(get_answer(""), expected_fallback)
        self.assertEqual(get_answer("   "), expected_fallback) # Test with whitespace

    def test_question_with_extra_whitespace(self):
        """Test that questions with leading/trailing whitespace are handled."""
        question = " what are the admission requirements? "
        expected_answer = PREDEFINED_FAQS["what are the admission requirements?"]
        self.assertEqual(get_answer(question), expected_answer)

if __name__ == '__main__':
    unittest.main()
