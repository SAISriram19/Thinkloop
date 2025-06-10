# src/simulated_call_handler.py

from faq_handler import get_answer

def receive_simulated_call():
    """
    Simulates receiving a call by taking text input from the user.
    In a real application, this would be replaced by actual telephony integration
    and speech-to-text processing.
    """
    print("\n📞 [Simulated Call Handler] Incoming call simulation...")
    user_input = input("🎤 [User Voice (simulated text)]: ")
    return user_input

def process_input(text_input: str):
    """
    Processes the received text input by forwarding it to the FAQ handler.
    """
    print(f"💬 [Simulated Call Handler] Received text: '{text_input}'")
    print(f"🧠 [Simulated Call Handler] Forwarding to FAQ handler...")
    ai_response = get_answer(text_input)
    return ai_response

def send_simulated_response(response_text: str):
    """
    Simulates sending a response back to the caller.
    In a real application, this would involve text-to-speech and sending audio
    or text back via the communication channel.
    """
    print(f"📢 [Simulated Call Handler] Sending response: '{response_text}'")

def main_loop():
    """
    Main loop for the simulated call handler.
    Allows for multiple interactions in a single simulation run.
    """
    print("🤖 Thinkloop AI Receptionist - Simulated Call Handler (Basic)")
    print("Type 'exit' or 'quit' to end the simulation.")

    while True:
        user_text = receive_simulated_call()

        if user_text.lower() in ['exit', 'quit']:
            print("📞 [Simulated Call Handler] Simulation ended by user.")
            break

        ai_response = process_input(user_text)
        send_simulated_response(ai_response)

if __name__ == "__main__":
    main_loop()
