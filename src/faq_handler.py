# src/faq_handler.py

PREDEFINED_FAQS = {
    "what are the admission requirements?": "For our undergraduate programs, you typically need a high school diploma or equivalent, standardized test scores (like SAT or ACT) if applicable, letters of recommendation, and a personal essay. Specific requirements can vary by program. Which program are you interested in?",
    "what is the application deadline?": "The general application deadline for the upcoming fall semester is March 15th. However, some programs may have different deadlines. It's always best to check the specific deadline for the program you're applying to.",
    "how much is the tuition fee?": "Tuition fees vary depending on the program and whether you are an in-state or out-of-state student. For a general idea, undergraduate tuition is approximately $X per year for in-state students and $Y for out-of-state students. We also offer various financial aid and scholarship options.",
    "do you offer scholarships?": "Yes, we offer a variety of scholarships based on academic merit, financial need, and other criteria. I recommend visiting the financial aid section of our website or contacting the financial aid office for detailed information and application procedures."
}

def get_answer(question: str) -> str:
    """
    Answers a predefined question from the FAQ list.
    The matching is case-insensitive and looks for the question as a key.
    """
    question_lower = question.lower().strip()
    return PREDEFINED_FAQS.get(question_lower, "I'm sorry, I don't have an answer to that question right now. Please try asking something else or contact our admissions office.")

if __name__ == '__main__':
    # Example Usage
    test_questions = [
        "What are the admission requirements?",
        "WHAT IS THE APPLICATION DEADLINE?",
        "How much is the tuition fee?",
        "Do you offer scholarships?",
        "What programs do you offer?" # Test a question not in the list
    ]

    for q in test_questions:
        print(f"Q: {q}")
        print(f"A: {get_answer(q)}\n")
