# src/app.py
# Import stubs or actual modules as they get developed
# For now, direct imports if they exist, or define stubs here

# from .faq_handler import get_answer # Will be called by response_generator
# from .intent_parser import get_intent # To be created
# from .response_generator import generate_response # To be created
# from .voice_processor import text_to_speech # To be updated
from voice_processor import text_to_speech # Assuming speech_to_text might be used later
from intent_parser import get_intent # New import
from response_generator import generate_response # New import
from config import settings # New import for settings

# IntentParser class is removed from app.py
# ResponseGenerator class is removed from app.py

class MainApplication:
    def __init__(self):
        # self.intent_parser is removed
        # self.response_generator is removed
        print(f"🚀 {settings.APPLICATION_NAME} is starting...") # Illustrative print
        print("🤖 [App] MainApplication initialized.")

    def handle_text_input(self, text_input: str) -> str:
        """
        Main logic for handling text input and generating a response.
        Returns a string indicating the path to the audio file.
        """
        print(f"▶️ [App] Handling text input: '{text_input}'")

        # Use imported get_intent function
        intent_result = get_intent(text_input)

        # Pass original text_input as original_query for FAQ intent
        response_text = generate_response(intent_result, original_query=text_input)

        if intent_result.get("type") == "exit_app":
            print(f"🛑 [App] Exit command recognized. Response: '{response_text}'")
            return response_text

        # Actual TTS call from voice_processor.py
        audio_output_path = text_to_speech(response_text)

        print(f"✅ [App] Response generated. Audio at: {audio_output_path}")
        # In a real scenario, we might return the text response for display,
        # and the audio path for playback. For sim handler, path is enough.
        return f"Audio response saved to {audio_output_path}. Text was: '{response_text}'"

# Global instance (or manage through a factory/DI later)
# For now, a simple global instance for the simulator to call
# This will be refined as the app structure matures
# app_instance = MainApplication() # Not yet, let simulator instantiate

if __name__ == '__main__':
    app = MainApplication()
    print("\n--- Testing app.py directly (with externalized IntentParser) ---")
    test_inputs = ["Tell me about admission requirements", "What is the deadline?", "exit"]
    for ti in test_inputs:
        print(f"\nInput: {ti}")
        output = app.handle_text_input(ti)
        print(f"Output: {output}")
        # If exit intent leads to a specific response text, use that for breaking.
        if "Goodbye! Thanks for using Thinkloop." in output and "Audio response saved" not in output :
             print("Exit detected in app.py main loop, breaking.")
             break
