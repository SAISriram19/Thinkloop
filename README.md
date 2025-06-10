# Thinkloop - AI Voice Receptionist

**Project Status (Phase 1 - Initial Setup & Basic FAQ):**
- Basic project structure created (`src`, `tests`, `docs`, `config`).
- A simple FAQ handler (`src/faq_handler.py`) for admission inquiries is implemented with predefined questions and answers.
- Unit tests (`tests/test_faq_handler.py`) for the FAQ handler are in place and passing.
- Conceptual documentation for Make.com workflow (`docs/make_com_workflow_structure.md`) and setup (`docs/setup.md`) has been created.
- Next steps will involve expanding functionalities, implementing NLP, and actual integrations.

---
(Original README content below)
# Thinkloop
# Advanced AI Voice Receptionist for Educational Institutions

## Objective
Develop an advanced AI voice receptionist tailored for colleges, universities, and schools to handle admission inquiries and general receptionist duties. The AI must operate 24/7, provide a near-human conversational experience, reduce staff workload, and improve response times by efficiently managing calls and inquiries.

## System Requirements
1. **Platform**: Build using Make.com's automation capabilities, integrating with a robust voice AI platform (e.g., Dialogflow, Twilio, or ElevenLabs for voice synthesis) for real-time voice interaction.
2. **Availability**: Operate 24/7 with high uptime and reliability to handle calls at any time.
3. **Voice Capabilities**:
   - Use natural language processing (NLP) for human-like conversation.
   - Support multilingual capabilities (at least English, Spanish, and one additional language based on the institution's demographic).
   - Offer clear, professional, and friendly voice tones customizable to match the institution's brand.
4. **Integration**:
   - Connect with CRM systems (e.g., Salesforce, HubSpot) to log caller details and interactions.
   - Integrate with the institution’s database for real-time access to program details, admission requirements, and event schedules.
   - Sync with calendar systems (e.g., Google Calendar, Microsoft Outlook) for scheduling appointments or campus tours.
5. **Scalability**: Handle multiple simultaneous calls with minimal latency.
6. **Security**: Comply with FERPA and GDPR for handling sensitive student data securely.

## Core Functionalities
### 1. Admission Inquiry Handling
- **Purpose**: Address prospective students’ and parents’ questions about admissions.
- **Features**:
  - Answer FAQs about programs, application deadlines, eligibility criteria, tuition fees, scholarships, and financial aid.
  - Guide callers through the application process step-by-step (e.g., document submission, online portals).
  - Provide updates on application status when callers provide identifiable information (e.g., application ID).
  - Escalate complex queries (e.g., specific financial aid scenarios) to human staff with detailed call summaries.
- **Example Interaction**:
  - Caller: "What are the admission requirements for the engineering program?"
  - AI: "For our engineering program, you’ll need a high school diploma or equivalent, a minimum GPA of 3.0, SAT or ACT scores, and two letters of recommendation. Would you like details on the application process or specific prerequisites for a particular engineering major?"

### 2. General Receptionist Duties
- **Purpose**: Manage non-admission-related calls to reduce staff workload.
- **Features**:
  - Route calls to appropriate departments (e.g., registrar, financial aid, student services) based on caller intent.
  - Provide information on campus events, office hours, and directions to the institution.
  - Schedule appointments for campus tours, advisor meetings, or open house events.
  - Handle basic inquiries (e.g., contact details, operating hours) without human intervention.
- **Example Interaction**:
  - Caller: "Can I speak to someone in the registrar’s office?"
  - AI: "I can connect you to the registrar’s office. May I have your name and a brief reason for your call to assist them better? Alternatively, I can provide information on common registrar topics like transcript requests or course registration."

### 3. Natural Conversation and Near-Human Experience
- **Tone and Style**:
  - Use a warm, professional, and empathetic tone to make callers feel valued.
  - Adapt responses based on caller sentiment (e.g., calming tone for frustrated callers).
  - Avoid robotic phrasing; use conversational fillers (e.g., “Let me check that for you”) for natural flow.
- **Context Retention**:
  - Maintain conversation context across multiple turns (e.g., remembering caller’s name or previous question).
  - Handle interruptions gracefully (e.g., if the caller changes topics mid-conversation).
- **Personalization**:
  - Greet returning callers by name if their number is recognized in the CRM.
  - Tailor responses based on caller type (e.g., prospective student, parent, alumnus).
- **Example Interaction**:
  - Caller: "I’m worried about missing the application deadline."
  - AI: "I understand how stressful deadlines can be! The application deadline for the fall semester is June 30th. Would you like me to guide you through the steps to start your application now, or send you a reminder closer to the date?"

### 4. Workload Reduction and Efficiency
- **Automation**:
  - Automate repetitive tasks like answering FAQs, scheduling appointments, and logging call details.
  - Provide self-service options (e.g., sending application links via SMS/email, booking tours via voice commands).
- **Escalation Protocol**:
  - Identify when human intervention is needed (e.g., emotional distress, complex queries) and transfer calls seamlessly with a summary of the interaction sent to staff via CRM or email.
- **Analytics**:
  - Generate reports on call volume, common inquiries, and resolution rates to help staff optimize processes.
  - Flag high-priority inquiries (e.g., urgent application issues) for immediate human follow-up.
- **Example Interaction**:
  - Caller: "I need to speak to someone about my scholarship application."
  - AI: "I can help with general scholarship questions, but for specific application details, I’ll connect you to our financial aid team. To make this quick, could you share your application ID? I’ll pass along a summary to ensure they have all the details."

### 5. Technical Implementation Details
- **Voice Platform**:
  - Use a text-to-speech (TTS) engine (e.g., ElevenLabs, Google TTS) for natural-sounding voice output.
  - Implement speech-to-text (STT) for accurate caller input recognition, even with accents or background noise.
- **Make.com Workflow**:
  - Create a workflow that triggers on incoming calls via a telephony integration (e.g., Twilio).
  - Parse caller input using NLP to identify intent and extract entities (e.g., “application deadline” → intent: query_deadline).
  - Query the institution’s database or CRM for real-time data (e.g., program details, event schedules).
  - Log interactions in the CRM and send follow-up emails/SMS as needed (e.g., application links, appointment confirmations).
- **Error Handling**:
  - Gracefully handle unclear inputs (e.g., “I’m not sure what you mean, could you clarify?”).
  - Fallback to human transfer if the AI cannot resolve the query after two attempts.
- **Testing**:
  - Simulate various call scenarios (e.g., angry caller, unclear speech, complex queries) to ensure robustness.
  - Validate multilingual support and CRM/database integrations.

## Customization Options
- **Institution-Specific Data**:
  - Allow the institution to upload program details, FAQs, and contact directories via a Make.com module.
  - Support custom voice branding (e.g., accent, gender, tone) to align with the institution’s identity.
- **Scalable Modules**:
  - Enable/disable features (e.g., appointment scheduling, multilingual support) based on the institution’s needs.
  - Allow integration with additional platforms (e.g., Slack for internal staff notifications).

## Success Metrics
- **Response Time**: Reduce average call handling time by 30% compared to human staff.
- **Caller Satisfaction**: Achieve a caller satisfaction rate of 90%+ based on post-call surveys.
- **Workload Reduction**: Automate 70% of routine inquiries, freeing staff for complex tasks.
- **Uptime**: Maintain 99.9% availability for 24/7 operation.

## Example Workflow in Make.com
1. **Trigger**: Incoming call via Twilio.
2. **Action 1**: Convert caller speech to text using STT.
3. **Action 2**: Process text with NLP to identify intent and entities.
4. **Action 3**: Query database/CRM for relevant information (e.g., program details).
5. **Action 4**: Generate a natural-language response and convert to voice via TTS.
6. **Action 5**: Log interaction in CRM and send follow-up (e.g., email with links).
7. **Action 6**: Escalate to human staff if needed, with a call summary.

## Constraints
- Ensure compliance with data privacy laws (FERPA, GDPR).
- Avoid overpromising (e.g., guaranteeing admission outcomes).
- Limit call duration to 5 minutes for automated handling unless escalated.

## Deliverables
- A fully functional Make.com workflow for the AI voice receptionist.
- Documentation for setup, customization, and integration with institution systems.
- Test scripts for validating functionality across common call scenarios.
- A dashboard for monitoring call analytics and performance metrics.

## Notes
- Prioritize user-friendly setup for institutions with limited technical expertise.
- Ensure the AI can handle high call volumes during peak admission seasons.
- Regularly update the AI’s knowledge base with new program details and FAQs.
