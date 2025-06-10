# src/faq_handler.py
import re

# Structure: "question_key": {"keywords": ["kw1", "kw2"], "answer": "The answer."}
# Keywords will be used for matching. More specific phrases are preferred.
PREDEFINED_FAQS = {
    "admission_requirements": {
        "keywords": ["admission requirements", "how to apply", "application criteria", "what is needed to apply", "program prerequisites", "admission"],
        "answer": "For our undergraduate programs, you typically need a high school diploma or equivalent, standardized test scores (like SAT or ACT) if applicable, letters of recommendation, and a personal essay. Specific requirements can vary by program. Which program are you interested in?"
    },
    "application_deadline": {
        "keywords": ["application deadline", "deadline for application", "when is application due", "submission deadline", "apply by when", "deadline"],
        "answer": "The general application deadline for the upcoming fall semester is March 15th. However, some programs may have different deadlines. It's always best to check the specific deadline for the program you're applying to."
    },
    "tuition_fee": {
        "keywords": ["tuition fee", "cost of tuition", "how much is tuition", "program cost", "fee structure", "payment for courses"],
        "answer": "Tuition fees vary depending on the program and whether you are an in-state or out-of-state student. For a general idea, undergraduate tuition is approximately $X per year for in-state students and $Y for out-of-state students. We also offer various financial aid and scholarship options."
    },
    "scholarships_info": {
        "keywords": ["scholarships", "financial aid", "funding options", "grants available", "student support"],
        "answer": "Yes, we offer a variety of scholarships based on academic merit, financial need, and other criteria. I recommend visiting the financial aid section of our website or contacting the financial aid office for detailed information and application procedures."
    },
    "programs_offered": {
        "keywords": ["programs offered", "degree programs", "available majors", "what can i study", "list of courses", "fields of study available"],
        "answer": "We offer a wide range of undergraduate and graduate programs, including Engineering, Business, Arts & Sciences, and Health Professions. Could you tell me which field you are interested in for more specific information?"
    },
    "campus_tour": {
        "keywords": ["campus tour", "visit campus", "see the university", "open house information", "guided tour", "tour"],
        "answer": "We'd love to show you around! Campus tours are available Monday to Friday. You can book a tour through our website or I can help you find the booking page. Would you like the website link?"
    },
    "contact_admissions": {
        "keywords": ["contact admissions", "admissions office contact", "admissions phone number", "email for admissions", "talk to admissions counselor"],
        "answer": "You can contact the admissions office by phone at 1-800-555-ADMIT or by email at admissions@exampleuniversity.edu."
    },
    "application_status": {
        "keywords": ["application status", "check my application status", "status of my application", "did my application go through", "application submitted successfully"],
        "answer": "You can typically check your application status through our online admissions portal. You'll need your application ID and password. Would you like me to direct you to the portal?"
    },
    "faculty_info": {
        "keywords": ["faculty information", "professors information", "who teaches here", "department faculty", "research areas of professors", "faculty info", "faculty"],
        "answer": "We have distinguished faculty members across all departments. You can find information about specific professors, their research, and publications on the departmental websites. Is there a particular department or professor you're interested in?"
    }
}

DEFAULT_FALLBACK_ANSWER = "I'm sorry, I don't have an answer to that specific question right now. You can try rephrasing, or I can help you find contact information for the relevant department. How would you like to proceed?"

def get_answer(question: str) -> str:
    """
    Answers a question by finding the FAQ with the most matching keywords from the input question.
    The matching is case-insensitive and tokenizes the question.
    A simple scoring mechanism is used: 1 point for each keyword found.
    """
    question_lower = question.lower()
    # Normalize by removing punctuation and splitting into words
    # This helps in matching keywords more reliably.
    question_words = set(re.findall(r'\b\w+\b', question_lower))

    if not question_words: # Handle empty or punctuation-only input
        return DEFAULT_FALLBACK_ANSWER

    best_match_key = None
    max_score = 0

    for key, faq_data in PREDEFINED_FAQS.items():
        current_score = 0
        # Check for presence of each keyword associated with an FAQ
        for keyword in faq_data["keywords"]:
            kw_is_multi_word = " " in keyword

            if keyword in question_lower: # Full phrase match (good for multi-word keywords)
                current_score += 1.0
            elif not kw_is_multi_word and keyword in question_words: # Single keyword word match
                current_score += 1.0 # Give single keywords a strong score if they match a word
            elif kw_is_multi_word: # Only if it's a multi-word keyword that wasn't a full phrase match
                # This part handles partial matches for multi-word keywords
                keyword_parts = set(keyword.split())
                common_words = keyword_parts.intersection(question_words)
                if common_words:
                    # Score based on proportion of matched words in the keyword phrase
                    # This gives higher scores to more complete partial matches.
                    # Using a slightly lower weight for partials vs full phrase match.
                    current_score += (len(common_words) / len(keyword_parts)) * 0.8

        if current_score > max_score:
            max_score = current_score
            best_match_key = key

    # Threshold for considering a match valid (e.g., at least 1 full keyword match or significant partial)
    if best_match_key and max_score >= 0.9: # Adjusted threshold slightly due to proportional scoring
        return PREDEFINED_FAQS[best_match_key]["answer"]

    return DEFAULT_FALLBACK_ANSWER

if __name__ == '__main__':
    # Example Usage
    test_questions = [
        "Tell me about admission requirements.",
        "When is the application deadline?",
        "How much is tuition?",
        "Are there any scholarships for students?",
        "What kind of programs do you have available?",
        "Can I visit the campus for a tour?",
        "How to contact admissions office?",
        "How can I check my application status?",
        "Who are the professors in engineering?",
        "What's the weather like there?", # Test a question not in the list
        "admission criteria", # Test with fewer words
        "deadline for application",
        "cost of study"
    ]

    print("🤖 Thinkloop FAQ Handler (Refined with Keyword Matching)\n")
    for q in test_questions:
        print(f"Q: {q}")
        print(f"A: {get_answer(q)}\n")
