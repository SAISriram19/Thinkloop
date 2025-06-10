# Thinkloop AI Receptionist

## Overview
The Thinkloop AI Receptionist is an advanced AI voice receptionist tailored for educational institutions. It's designed to handle admission inquiries and general receptionist duties 24/7, providing a near-human conversational experience.

## How it Works
The application processes user input (text, initially) to understand the user's intent.
1.  **Input Handling**: The `src/app.py` receives text input.
2.  **Intent Parsing**: `src/intent_parser.py` analyzes the input to determine the user's goal (e.g., asking an FAQ, exiting).
3.  **Response Generation**: `src/response_generator.py` formulates a text response. This module uses `src/faq_handler.py` if the intent is related to a frequently asked question.
4.  **Voice Output**: `src/voice_processor.py` converts the text response into speech and saves it as an audio file (currently supports Coqui TTS with a fallback to text if TTS is unavailable).

## Features
*   Handles Frequently Asked Questions (FAQs) related to admissions.
*   Parses user intent to understand queries.
*   Generates natural language responses.
*   Provides voice output for responses using Text-to-Speech (TTS).
*   Modular design for easier maintenance and future expansion.

## Getting Started

### Prerequisites
*   Python 3.x installed.
*   Refer to `requirements.txt` for a full list of Python libraries. Some core dependencies include:
    *   `TTS` (from Coqui TTS) for voice output.

### Installation
1.  Clone the repository:
    ```bash
    git clone <your-repository-url>
    cd <repository-name>
    ```
2.  Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```
    **Note on Coqui TTS**: The `TTS` library can be large and may have system dependencies. If you encounter issues or are in a resource-constrained environment, the application is designed to fall back to text-based output if Coqui TTS cannot be initialized. Actual audio generation requires an environment where Coqui TTS and its dependencies (including PyTorch) can be fully installed.

### Running the Application
The application can be run using the simulated call handler, which allows you to interact with it via text input in your console:
```bash
python src/simulated_call_handler.py
```
This script uses the main application logic in `src/app.py` to process your input. Type your queries when prompted, and the system will respond. If Coqui TTS is functional, it will save audio responses to the `audio_outputs/` directory; otherwise, it will print the text response and indicate that no audio was generated. To exit the simulation, type 'exit' or 'quit'.

## Running Tests
The project includes a suite of unit tests to ensure individual components are working correctly. To run all tests:
```bash
python tests/test_app.py
python tests/test_faq_handler.py
python tests/test_intent_parser.py
python tests/test_response_generator.py
python tests/test_simulated_call_handler.py
python tests/test_voice_processor.py
```
Ensure all tests pass to verify the application's core functionalities.

## Project Structure
Here's an overview of the key directories and their contents:
*   `src/`: Contains the core source code for the application, including modules for intent parsing, response generation, voice processing, and FAQ handling.
    *   `app.py`: The main application orchestrator.
*   `tests/`: Includes all unit tests for the different modules of the application.
*   `config/`: Holds configuration files, such as `settings.py`.
*   `docs/`: Contains documentation files, including architecture diagrams and setup guides.
*   `audio_outputs/`: This directory is automatically created (if it doesn't exist) when the application generates voice output. It stores the `.wav` files produced by the Text-to-Speech engine.
*   `requirements.txt`: Lists all Python dependencies for the project.
*   `README.md`: This file, providing an overview and guide to the project.

## Configuration
Key application settings are managed in `config/settings.py`.
*   `APPLICATION_NAME`: Defines the name of the application (e.g., "Thinkloop AI Receptionist").
*   `DEFAULT_LANGUAGE`: Sets the default language for TTS (e.g., "en").

You can modify these settings as needed. For sensitive information like API keys (if added in the future), it's recommended to use environment variables rather than hardcoding them directly into `settings.py`.

## Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these general guidelines:
1.  **Fork the repository.**
2.  **Create a new branch** for your feature or bug fix:
    ```bash
    git checkout -b feature/your-feature-name
    ```
    or
    ```bash
    git checkout -b fix/your-bug-fix-name
    ```
3.  **Make your changes.** Ensure you add or update tests as appropriate.
4.  **Test your changes** thoroughly.
5.  **Commit your changes** with a clear and descriptive commit message.
6.  **Push your branch** to your forked repository.
7.  **Create a Pull Request** to the main repository's `main` branch (or the relevant development branch).

Please ensure your code adheres to the project's coding style (if one is established) and that all tests pass before submitting a pull request.
