# Setup and Running (Phase 1: Basic FAQ Handler)

This document describes how to set up and run the initial basic FAQ handler functionality of the Thinkloop project.

## Prerequisites
- Python 3.x installed.
- No external Python libraries are required for this phase beyond the standard library.

## Components
- **`src/faq_handler.py`**: Contains the logic for answering predefined admission-related questions.
- **`tests/test_faq_handler.py`**: Contains unit tests for the FAQ handler.
- **`docs/make_com_workflow_structure.md`**: Describes the conceptual Make.com workflow.

## Running the FAQ Handler (Locally)
The `faq_handler.py` script can be run directly to see example interactions:
```bash
python src/faq_handler.py
```
This will print a few test questions and their answers to the console.

## Running Tests
To run the unit tests:
```bash
python tests/test_faq_handler.py
```
All tests should pass, indicating the FAQ handler is working as expected.

## Conceptual Make.com Setup
Refer to `docs/make_com_workflow_structure.md` for the conceptual outline of how this FAQ handler would fit into a Make.com workflow. In essence:
1. A Make.com scenario would be triggered by an incoming call/message.
2. The user's input (text) would be passed to a system capable of executing the `get_answer(question)` function from `src/faq_handler.py`.
3. The returned answer would then be relayed back to the user via the Make.com scenario.

This phase does not include actual Make.com integration, only the foundational Python script.


## Phase 2: Running the Simulated Call Handler with FAQ Integration

### Prerequisites
- Python 3.x installed.
- No external Python libraries are required for this phase beyond the standard library.

### Components
- **`src/simulated_call_handler.py`**: Simulates a call environment and interacts with the FAQ handler.
- **`src/faq_handler.py`**: Provides answers to questions based on keyword matching.
- **`src/voice_processor.py`**: Contains stubs for STT/TTS (not directly run, but used conceptually).
- **`tests/`**: Contains unit tests for the above components.
- **`docs/architecture.md`**: Describes the system architecture.

### Running the Simulation
To run the simulated call handler:
```bash
python src/simulated_call_handler.py
```
This will start an interactive loop where you can type questions (simulating user speech) and see the AI's responses from the FAQ handler. Type 'exit' or 'quit' to end the simulation.

### Running Tests
To run all tests for Phase 2 components:
```bash
python tests/test_simulated_call_handler.py
python tests/test_voice_processor.py
python tests/test_faq_handler.py # (Updated tests)
```
All tests should pass.

## Phase 3: Basic Application Framework & TTS (Stubbed) Integration

### Prerequisites
- Python 3.x installed.
- **`TTS` (from Coqui TTS)**: This library is listed in `requirements.txt`.
    - **Note on current environment:** Due to disk space limitations in the current development environment, `pip install TTS` may fail or the library may not be fully functional. The `src/voice_processor.py` module is designed to gracefully fall back to a text-based stub if Coqui TTS cannot be initialized. Actual audio generation requires an environment where Coqui TTS and its dependencies (including PyTorch) can be fully installed.

### Key Components Developed/Updated
- **`src/app.py`**: Main application orchestrator.
- **`src/intent_parser.py`**: Basic intent recognition (FAQ, exit, unknown).
- **`src/response_generator.py`**: Generates text responses based on intent, using `faq_handler`.
- **`src/voice_processor.py`**: Includes Coqui XTTS-v2 integration for TTS, with a fallback to stub if the library is not functional. STT remains a basic stub.
- **`config/settings.py`**: Basic configuration file.
- **`tests/`**: New tests for `app`, `intent_parser`, `response_generator`, and updated tests for `voice_processor`.

### Running the Application (Simulated)
The main application logic can be tested via the simulated call handler:
```bash
python src/simulated_call_handler.py
```
This will use `src/app.py` to process your text input. Responses will be printed to the console. If Coqui TTS were fully functional, it would save audio files to the `audio_outputs/` directory; in the current stubbed mode, it will indicate that no audio was generated.

### Running Individual Modules for Testing
You can also run some modules directly to see their basic behavior:
```bash
python src/intent_parser.py
python src/response_generator.py
python src/voice_processor.py # (Will show TTS stub/fallback status)
python config/settings.py
python src/app.py # (Runs its own internal test loop)
```

### Running Tests
To run all unit tests for Phase 3 components (and previous ones):
```bash
python tests/test_app.py
python tests/test_intent_parser.py
python tests/test_response_generator.py
python tests/test_voice_processor.py
python tests/test_faq_handler.py
python tests/test_simulated_call_handler.py
```
All tests should pass.
