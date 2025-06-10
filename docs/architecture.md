# System Architecture (From Scratch Build)

This document outlines the high-level architecture for the Thinkloop AI Voice Receptionist, built from scratch.

## Core Objective
Develop an advanced AI voice receptionist tailored for educational institutions to handle admission inquiries and general receptionist duties 24/7, providing a near-human conversational experience.

## Main Application Flow
1.  **Call/Message Reception:** The system receives an incoming call or text-based message. (Details of telephony/channel integration will be defined later).
2.  **Input Processing (Speech-to-Text - STT):** If the input is voice, it's converted to text.
3.  **Intent Parsing:** The system analyzes the user's text input to understand their intent (e.g., asking a question, requesting to be routed, scheduling).
4.  **Information Retrieval/Action Execution:** Based on the intent:
    *   If it's a question, query the knowledge base (e.g., FAQ handler, institution database).
    *   If it's a request for routing, determine the correct department.
    *   If it's scheduling, interact with calendar systems.
5.  **Response Generation:** Formulate a natural language response.
6.  **Output Processing (Text-to-Speech - TTS):** If the output channel is voice, convert the text response to speech.
7.  **Response Delivery:** Send the response (voice or text) back to the user.
8.  **Logging:** Log the interaction details.

## Key Modules
1.  **`entry_point_handler` (e.g., `main.py` or `app.py`):**
    *   Manages the overall lifecycle of an interaction.
    *   Coordinates between different modules.
    *   Handles initial reception of contact and final sending of response.
    *   (Replaces the Make.com workflow concept).

2.  **`voice_processor` (`src/voice_processor.py`):**
    *   **SpeechToText (STT):** Converts spoken audio from the user into text.
        *   _Initial:* Stub that passes input text through.
        *   _Future:* Integration with an STT engine (e.g., Whisper, Google Speech-to-Text).
    *   **TextToSpeech (TTS):** Converts text responses from the AI into spoken audio.
        *   _Initial:* Stub that prints text or returns it as a string.
        *   _Future:* Integration with a TTS engine (e.g., ElevenLabs, Google TTS, Coqui TTS).

3.  **`intent_parser` (`src/intent_parser.py`):**
    *   Analyzes the user's text input to determine their goal or question type.
    *   _Initial:* May use simple keyword matching or regex for basic intents.
    *   _Future:* Could involve more sophisticated NLP models (e.g., Rasa NLU, spaCy, or custom models).

4.  **`faq_handler` (`src/faq_handler.py`):**
    *   Manages and answers frequently asked questions.
    *   (Already partially implemented).

5.  **`knowledge_base_interface` (`src/kb_interface.py`):**
    *   Module for interacting with the institution’s database for dynamic information (program details, event schedules, etc.).
    *   _Initial:* May be a stub or connect to mock data.
    *   _Future:* Connect to actual databases (SQL, NoSQL).

6.  **`crm_interface` (`src/crm_interface.py`):**
    *   Handles logging caller details and interactions to CRM systems (e.g., Salesforce, HubSpot).
    *   _Initial:* Stubs for logging.
    *   _Future:* Integration with CRM APIs.

7.  **`calendar_interface` (`src/calendar_interface.py`):**
    *   Manages scheduling appointments or campus tours by interacting with calendar systems (e.g., Google Calendar, Microsoft Outlook).
    *   _Initial:* Stubs for scheduling.
    *   _Future:* Integration with Calendar APIs.

8.  **`response_generator` (`src/response_generator.py`):**
    *   Constructs natural-sounding responses based on information retrieved or actions taken.
    *   _Initial:* May select from predefined templates or directly use FAQ answers.
    *   _Future:* More dynamic response generation, possibly using NLG techniques.

9.  **`call_router` (`src/call_router.py`):**
    *   Determines how to route calls to appropriate departments or human agents if the AI cannot handle the query.
    *   Includes escalation protocols.

10. **`session_manager` (`src/session_manager.py`):**
    *   Maintains context across multiple turns in a conversation.
    *   Manages user-specific data during an interaction.

11. **`config_manager` (`config/settings.py`):**
    *   Manages configuration settings for the application (API keys, database URLs, etc.).

## Data Flow (Example: FAQ Query)
1.  User calls/sends message -> `entry_point_handler`
2.  `entry_point_handler` -> `voice_processor.stt` (if voice) -> text
3.  `entry_point_handler` -> `intent_parser` (identifies as FAQ) -> intent
4.  `entry_point_handler` -> `faq_handler.get_answer(text)` -> answer_text
5.  `entry_point_handler` -> `response_generator` (formats answer) -> final_response_text
6.  `entry_point_handler` -> `voice_processor.tts` (if voice) -> audio_response
7.  `entry_point_handler` -> Delivers response to user.

This architecture provides a modular and scalable foundation for building the AI receptionist from scratch.
