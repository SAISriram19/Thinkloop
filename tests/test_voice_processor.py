# tests/test_voice_processor.py
import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from voice_processor import speech_to_text, text_to_speech

class TestVoiceProcessorStubs(unittest.TestCase):

    def test_stt_stub_with_string(self):
        test_input = "This is spoken text"
        self.assertEqual(speech_to_text(test_input), test_input)

    def test_stt_stub_with_non_string(self):
        test_input = {"audio_data": "some_bytes"}
        self.assertEqual(speech_to_text(test_input), "Simulated transcribed text from audio.")

    def test_tts_stub(self):
        test_text = "Hello world"
        expected_output = f"[Audio Output Simulated for: '{test_text}']"
        self.assertEqual(text_to_speech(test_text), expected_output)

if __name__ == '__main__':
    unittest.main()
