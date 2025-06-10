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
