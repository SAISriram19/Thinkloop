# config/settings.py

# Placeholder for future model paths or other configurations
# For example, if we were using a local STT model:
# STT_MODEL_PATH = "models/stt/your_stt_model.tflite"

# If Coqui XTTS required specific speaker WAVs to be configured:
# DEFAULT_SPEAKER_WAV = "path/to/your/default_speaker.wav"

# For now, just a general placeholder
APPLICATION_NAME = "Thinkloop AI Receptionist"
DEFAULT_LANGUAGE = "en"

# Example of a setting that might be used by a database interface later
# DATABASE_URL = "sqlite:///./thinkloop.db"

# API keys (should ideally be loaded from environment variables in production)
# SOME_API_KEY = "your_api_key_here"

print("⚙️ [Config] Settings loaded (or defined).")

if __name__ == '__main__':
    print("--- Testing Config Settings ---")
    print(f"Application Name: {APPLICATION_NAME}")
    print(f"Default Language: {DEFAULT_LANGUAGE}")
    # print(f"Database URL: {DATABASE_URL}") # Example
