# tests/test_app.py
import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Add project root to sys.path to allow importing 'config'
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# Add src to sys.path for importing app and its dependencies
SRC_PATH = os.path.join(PROJECT_ROOT, 'src')
if SRC_PATH not in sys.path:
    sys.path.insert(1, SRC_PATH) # Insert after project root

from app import MainApplication
# We'll need to mock the functions imported by app.py
# from intent_parser import get_intent
# from response_generator import generate_response
# from voice_processor import text_to_speech

class TestMainApplication(unittest.TestCase):

    @patch('app.get_intent')
    @patch('app.generate_response')
    @patch('app.text_to_speech')
    def test_handle_text_input_faq_flow(self, mock_text_to_speech, mock_generate_response, mock_get_intent):
        # Setup mocks
        mock_get_intent.return_value = {"type": "faq_query", "data": "user question"}
        mock_generate_response.return_value = "FAQ answer text"
        mock_text_to_speech.return_value = "path/to/audio_faq.wav"

        app = MainApplication()
        user_input = "Tell me about requirements"
        result = app.handle_text_input(user_input)

        mock_get_intent.assert_called_once_with(user_input)
        mock_generate_response.assert_called_once_with({"type": "faq_query", "data": "user question"}, original_query=user_input)
        mock_text_to_speech.assert_called_once_with("FAQ answer text")
        self.assertEqual(result, "Audio response saved to path/to/audio_faq.wav. Text was: 'FAQ answer text'")

    @patch('app.get_intent')
    @patch('app.generate_response')
    @patch('app.text_to_speech')
    def test_handle_text_input_exit_flow(self, mock_text_to_speech, mock_generate_response, mock_get_intent):
        # Setup mocks
        mock_get_intent.return_value = {"type": "exit_app"}
        mock_generate_response.return_value = "Goodbye message"
        # text_to_speech should not be called for exit intent

        app = MainApplication()
        user_input = "exit"
        result = app.handle_text_input(user_input)

        mock_get_intent.assert_called_once_with(user_input)
        mock_generate_response.assert_called_once_with({"type": "exit_app"}, original_query=user_input)
        mock_text_to_speech.assert_not_called()
        self.assertEqual(result, "Goodbye message")

    @patch('app.get_intent')
    @patch('app.generate_response')
    @patch('app.text_to_speech')
    @patch('app.settings.APPLICATION_NAME', "TestApp") # Corrected config patch
    def test_app_initialization_uses_config(self, mock_tts, mock_resp_gen, mock_intent): # Renamed mock args for clarity
        # This test is more about showing config can be mocked if needed.
        # The print statement in __init__ is a side effect, hard to assert directly without capturing stdout.
        # For now, just ensure it runs without error with a mocked config.
        try:
            app = MainApplication() # Should print "🚀 TestApp is starting..."
            # If we captured stdout, we could assert it.
        except Exception as e:
            self.fail(f"MainApplication initialization failed with mocked config: {e}")


if __name__ == '__main__':
    unittest.main()
