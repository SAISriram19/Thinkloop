# tests/test_voice_processor.py
import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Add project root to sys.path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# Add src to sys.path for importing voice_processor
SRC_PATH = os.path.join(PROJECT_ROOT, 'src')
if SRC_PATH not in sys.path:
    sys.path.insert(1, SRC_PATH)

# We need to test the behavior based on whether TTS is "enabled" (i.e., import succeeded) or not.
# To do this, we can check the TTS_ENABLED flag in voice_processor.
import voice_processor
# from src.voice_processor import speech_to_text, text_to_speech, TTS_ENABLED, tts_instance

class TestVoiceProcessor(unittest.TestCase):

    def test_stt_stub_with_string(self):
        test_input = "This is spoken text"
        self.assertEqual(voice_processor.speech_to_text(test_input), test_input)

    def test_stt_stub_with_non_string(self):
        test_input = {"audio_data": "some_bytes"}
        self.assertEqual(voice_processor.speech_to_text(test_input), "Simulated transcribed text from audio (STT Stub).")

    # Test the TTS function. It will either call the real (mocked) TTS or the stub.
    @patch('voice_processor.tts_instance') # Mock the global tts_instance
    def test_tts_behavior(self, mock_tts_instance_global):
        test_text = "Hello world"

        if voice_processor.TTS_ENABLED and voice_processor.tts_instance:
            # If TTS is "enabled", mock its tts_to_file method
            # This mock_tts_instance_global might not be the actual instance if initialization failed.
            # Instead, we mock the actual tts_instance that's part of the voice_processor module.
            # The @patch above already does this for voice_processor.tts_instance

            # Ensure the mocked instance is used
            voice_processor.tts_instance.tts_to_file = MagicMock()

            output_path = voice_processor.text_to_speech(test_text)

            voice_processor.tts_instance.tts_to_file.assert_called_once()
            args, kwargs = voice_processor.tts_instance.tts_to_file.call_args
            self.assertEqual(kwargs['text'], test_text)
            self.assertTrue(output_path.startswith(voice_processor.OUTPUT_AUDIO_DIR))
            self.assertTrue(output_path.endswith(".wav"))
            print(f"Test (TTS Enabled): Output path {output_path}")

        else: # TTS is NOT enabled (fallback stub)
            expected_output = f"[STUB TTS - No Audio: '{test_text}']"
            actual_output = voice_processor.text_to_speech(test_text)
            self.assertEqual(actual_output, expected_output)
            print(f"Test (TTS Disabled/Stub): Output {actual_output}")
            # Ensure no attempt to call tts_to_file on a None tts_instance
            if voice_processor.tts_instance is not None: # Should be None if not enabled or failed init
                 voice_processor.tts_instance.tts_to_file.assert_not_called()


    @patch('voice_processor.TTS_ENABLED', False) # Force TTS_ENABLED to False for this test
    def test_tts_explicitly_stubbed_output(self): # Removed mock_tts_enabled
        test_text = "This is a forced stub test"
        expected_output = f"[STUB TTS - No Audio: '{test_text}']"
        self.assertEqual(voice_processor.text_to_speech(test_text), expected_output)


if __name__ == '__main__':
    unittest.main()
