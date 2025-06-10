# src/simulated_call_handler.py
# Remove direct import of faq_handler.get_answer if it was there
# from faq_handler import get_answer
from app import MainApplication # Import the main app orchestrator

def receive_simulated_call():
    """
    Simulates receiving a call by taking text input from the user.
    """
    print("\n📞 [Simulated Call Handler] Incoming call simulation...")
    user_input = input("🎤 [User Voice (simulated text)]: ")
    return user_input

# process_input is now handled by app.py's MainApplication instance
# send_simulated_response will display what app.py returns

def main_loop():
    """
    Main loop for the simulated call handler.
    Now interacts with the MainApplication from app.py.
    """
    print("🤖 Thinkloop AI Receptionist - Simulated Call Handler (Phase 3)")
    print("   (Interacting with app.py framework)")
    print("Type 'exit' or 'quit' to end the simulation.")

    # Initialize the main application
    application = MainApplication()

    while True:
        user_text = receive_simulated_call()

        # The app's handle_text_input will manage intent parsing, response generation, and TTS (stubbed)
        # It will also handle the 'exit'/'quit' logic internally based on intent.
        app_response_info = application.handle_text_input(user_text)

        print(f"📢 [Simulated Call Handler] App response: {app_response_info}")

        # Check if the app signaled to exit
        # This condition depends on what `handle_text_input` returns for an exit command.
        # For now, we assume "exit" or "quit" typed by user will be handled by app.py
        # and the loop here will break if the user types it directly to the input prompt
        # or if the app response indicates an exit.
        if user_text.lower() in ['exit', 'quit']:
             print("📞 [Simulated Call Handler] Exit command typed directly. Ending simulation.")
             break
        # A more robust way would be for app.handle_text_input to return a specific "EXIT_SIGNAL"
        if "Goodbye!" in app_response_info and "Thanks for using Thinkloop." in app_response_info : # Based on current app stub
             print("📞 [Simulated Call Handler] App signaled exit. Ending simulation.")
             break


if __name__ == "__main__":
    main_loop()
