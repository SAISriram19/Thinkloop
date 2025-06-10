# src/voice_processor.py
import os

OUTPUT_AUDIO_DIR = "audio_outputs"
os.makedirs(OUTPUT_AUDIO_DIR, exist_ok=True)

tts_instance = None
TTS_ENABLED = False

try:
    from TTS.api import TTS
    # Using XTTS-v2 model
    MODEL_NAME = "tts_models/multilingual/multi-dataset/xtts_v2"
    print("🎙️ [Voice Processor] Attempting to initialize Coqui XTTS-v2 model...")
    # Try to initialize, but anticipate failure in constrained environments
    # Forcing CPU to avoid large CUDA downloads if that's the main space issue.
    # If TTS library itself is not installed, this will also fail.
    tts_instance = TTS(model_name=MODEL_NAME, progress_bar=True, gpu=False)
    TTS_ENABLED = True
    print("✅ [Voice Processor] Coqui XTTS-v2 model initialized successfully (or was already cached).")
except ImportError:
    print("⚠️ [Voice Processor] TTS library not found. TTS functionality will be stubbed.")
except Exception as e:
    print(f"⚠️ [Voice Processor] Failed to initialize Coqui XTTS-v2 model: {e}. TTS functionality will be stubbed.")

def speech_to_text(audio_input_simulation) -> str:
    """
    Stub for Speech-to-Text (STT) processing.
    """
    if isinstance(audio_input_simulation, str):
        return audio_input_simulation
    return "Simulated transcribed text from audio (STT Stub)."

def text_to_speech(text_input: str, speaker_wav=None) -> str:
    """
    Text-to-Speech (TTS) processing. Uses Coqui XTTS-v2 if available,
    otherwise falls back to a simple text representation.
    Saves generated speech to a .wav file if TTS is operational.
    """
    if TTS_ENABLED and tts_instance:
        print(f"🔊 [Voice Processor] TTS (Coqui) processing for: '{text_input}'")
        try:
            output_filename = f"output_{hash(text_input)}.wav"
            output_path = os.path.join(OUTPUT_AUDIO_DIR, output_filename)

            tts_instance.tts_to_file(
                text=text_input,
                speaker_wav=speaker_wav,
                file_path=output_path
            )
            print(f"✅ [Voice Processor] Audio saved to: {output_path}")
            return output_path
        except Exception as e:
            print(f"⚠️ [Voice Processor] Error during TTS generation with Coqui: {e}")
            # Fall through to stub behavior if Coqui fails mid-operation

    # Fallback stub behavior
    print(f"🔊 [Voice Processor STUB] TTS processing for: '{text_input}' (No audio will be generated).")
    return f"[STUB TTS - No Audio: '{text_input}']"

if __name__ == '__main__':
    print("\n--- TTS (Coqui XTTS-v2 / Stub Fallback) Simulation ---")

    text_for_speech_1 = "Hello, this is a test of the Coqui XTTS version 2 model, or a stub if it's not working."
    output_file_1 = text_to_speech(text_for_speech_1)
    print(f"TTS Output 1: {output_file_1}")

    text_for_speech_2 = "Another test sentence for the voice processor."
    output_file_2 = text_to_speech(text_for_speech_2)
    print(f"TTS Output 2: {output_file_2}")

    if TTS_ENABLED and tts_instance:
        print("✅ TTS is operational.")
        # Check if files were created (only if TTS was expected to work)
        if os.path.exists(output_file_1) and ".wav" in output_file_1 :
             print(f"File {output_file_1} confirmed to exist.")
        else:
             print(f"File {output_file_1} was NOT created as expected by real TTS.")
    else:
        print("⚠️ TTS is NOT operational. Running in fallback stub mode.")

    print("\n--- STT Simulation ---")
    simulated_audio_input = "This is a test of the STT stub."
    transcribed_text = speech_to_text(simulated_audio_input)
    print(f"STT Transcribed text: {transcribed_text}")
