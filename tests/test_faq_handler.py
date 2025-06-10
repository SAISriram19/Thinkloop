# tests/test_faq_handler.py
import unittest
import sys
import os

# Add project root to sys.path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# Add src to sys.path for importing faq_handler
SRC_PATH = os.path.join(PROJECT_ROOT, 'src')
if SRC_PATH not in sys.path:
    sys.path.insert(1, SRC_PATH)

from faq_handler import get_answer, PREDEFINED_FAQS, DEFAULT_FALLBACK_ANSWER

class TestFAQHandlerRefined(unittest.TestCase):

    def test_known_questions_keywords(self):
        """Test that questions matching keywords return their correct answers."""
        test_cases = {
            "Tell me about admission requirements.": PREDEFINED_FAQS["admission_requirements"]["answer"],
            "When is the application deadline?": PREDEFINED_FAQS["application_deadline"]["answer"],
            "How much does tuition cost?": PREDEFINED_FAQS["tuition_fee"]["answer"],
            "Do you have scholarships?": PREDEFINED_FAQS["scholarships_info"]["answer"],
            "What programs can I study?": PREDEFINED_FAQS["programs_offered"]["answer"],
            "Can I get a campus tour?": PREDEFINED_FAQS["campus_tour"]["answer"],
            "How do I contact the admissions office?": PREDEFINED_FAQS["contact_admissions"]["answer"],
            "check status of my application": PREDEFINED_FAQS["application_status"]["answer"],
            "info on faculty": PREDEFINED_FAQS["faculty_info"]["answer"],
        }
        for question, expected_answer in test_cases.items():
            self.assertEqual(get_answer(question), expected_answer, f"Failed for Q: {question}")

    def test_unknown_question(self):
        """Test that an unknown question returns the default fallback message."""
        unknown_question = "What is the meaning of life in this university?"
        self.assertEqual(get_answer(unknown_question), DEFAULT_FALLBACK_ANSWER)

    def test_empty_or_punctuation_question(self):
        """Test that an empty or punctuation-only question returns the fallback message."""
        self.assertEqual(get_answer(""), DEFAULT_FALLBACK_ANSWER)
        self.assertEqual(get_answer("   "), DEFAULT_FALLBACK_ANSWER)
        self.assertEqual(get_answer("?!."), DEFAULT_FALLBACK_ANSWER)

    def test_partial_keywords(self):
        """Test questions that might only match a keyword or two."""
        # This test depends on the scoring logic in get_answer.
        # If "admission" alone is enough to trigger "admission_requirements"
        self.assertEqual(get_answer("admission"), PREDEFINED_FAQS["admission_requirements"]["answer"])
        self.assertEqual(get_answer("deadline"), PREDEFINED_FAQS["application_deadline"]["answer"])
        self.assertEqual(get_answer("tour campus"), PREDEFINED_FAQS["campus_tour"]["answer"])


    def test_case_insensitivity(self):
        """Test that matching is case-insensitive."""
        self.assertEqual(get_answer("TELL ME ABOUT ADMISSION REQUIREMENTS."), PREDEFINED_FAQS["admission_requirements"]["answer"])
        self.assertEqual(get_answer("how much is TUITION?"), PREDEFINED_FAQS["tuition_fee"]["answer"])

if __name__ == '__main__':
    unittest.main()
