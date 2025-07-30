import streamlit as st
import re

# --- Initial Setup ---
st.set_page_config(page_title="TalentScout Chatbot", page_icon="💬")
st.title("💼 TalentScout - Chatbot Mode")

# --- Session State Setup ---
if "messages" not in st.session_state:
    st.session_state.messages = []
if "candidate_info" not in st.session_state:
    st.session_state.candidate_info = {
        "name": None,
        "email": None,
        "phone": None,
        "experience": None,
        "position": None,
        "location": None,
        "tech_stack": []
    }
if "ended" not in st.session_state:
    st.session_state.ended = False

# --- Greeting (on first load) ---
if len(st.session_state.messages) == 0:
    greeting = """
    👋 Hello! I'm TalentScout, your AI hiring assistant.

    I'll ask you a few questions to learn more about your skills, and generate technical questions based on your tech stack.

    Type 'exit' or 'quit' anytime to end the chat.
    """
    st.session_state.messages.append({"role": "bot", "content": greeting})

# --- Function: Generate Questions Manually Based on Tech Stack ---
def generate_manual_questions(tech_stack):
    question_bank = {
        "Python": [
            "What are Python's key features?",
            "Explain the difference between list and tuple in Python.",
            "How does Python handle memory management?",
            "What is a Python decorator?",
            "What are Python generators?"
        ],
        "React": [
            "What is the virtual DOM in React?",
            "Explain the difference between props and state.",
            "What are React hooks?",
            "How does useEffect work?",
            "What is Redux and why is it used with React?"
        ],
        "Node": [
            "What is event-driven programming in Node.js?",
            "Explain the use of middleware in Express.js.",
            "What is the role of package.json in Node.js?",
            "How does Node handle asynchronous I/O?",
            "Difference between require and import in Node.js?"
        ],
        "SQL": [
            "What is normalization in SQL?",
            "What is the difference between DELETE and TRUNCATE?",
            "What is a JOIN? Name its types.",
            "What is a subquery in SQL?",
            "Write a query to find the second highest salary."
        ]
    }
    questions = []
    for tech in tech_stack:
        tech = tech.strip().title()
        if tech in question_bank:
            questions.extend(question_bank[tech])
    return questions[:5 * len(tech_stack)]

# --- Chat Interface ---
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --- End conversation early ---
if st.session_state.ended:
    st.info("👋 Thanks for chatting! We'll reach out to you with next steps.")
    st.stop()

# --- User Input ---
user_input = st.chat_input("Type your response...")
if user_input:
    # Display user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Exit check
    if user_input.lower() in ["exit", "quit", "bye"]:
        goodbye = "👋 Thanks for sharing your details! We’ll reach out soon."
        st.session_state.messages.append({"role": "bot", "content": goodbye})
        with st.chat_message("bot"):
            st.markdown(goodbye)
        st.session_state.ended = True
        st.stop()

    # --- Bot Logic ---
    info = st.session_state.candidate_info
    response = ""

    if not info["name"]:
        info["name"] = user_input
        response = "Great! Can you share your 📧 email address?"

    elif not info["email"]:
        if re.match(r"[^@\s]+@[^@\s]+\.[a-zA-Z0-9]+$", user_input):
            info["email"] = user_input
            response = "Thanks! What's your 📞 phone number?"
        else:
            response = "❌ Please enter a valid email address."

    elif not info["phone"]:
        if re.match(r"^\d{10}$", user_input):
            info["phone"] = user_input
            response = "How many years of 🧠 experience do you have? (e.g. Fresher, 1-2, 3-5, 5+)"
        else:
            response = "❌ Please enter a valid 10-digit mobile number."

    elif not info["experience"]:
        info["experience"] = user_input
        response = "Which position are you applying for? 💼"

    elif not info["position"]:
        info["position"] = user_input
        response = "Where are you currently located? 📍"

    elif not info["location"]:
        info["location"] = user_input
        response = "Please list the 🛠️ tech stack you know (comma-separated: Python, React, etc.)"

    elif not info["tech_stack"]:
        stack = [tech.strip() for tech in user_input.split(",") if tech.strip()]
        info["tech_stack"] = stack

        # ✅ Generate questions
        response = "Generating technical questions based on your skills..."
        with st.chat_message("bot"):
            st.markdown(response)

        questions = generate_manual_questions(stack)
        for q in questions:
            st.session_state.messages.append({"role": "bot", "content": q})
            with st.chat_message("bot"):
                st.markdown(q)

        # 🎯 End chat with goodbye
        goodbye = "👋 That’s all for now! Thank you, and we’ll be in touch shortly."
        st.session_state.messages.append({"role": "bot", "content": goodbye})
        with st.chat_message("bot"):
            st.markdown(goodbye)
        st.session_state.ended = True
        st.stop()

    else:
        response = "✅ All info collected. Type 'exit' to end or ask anything else."

    # Add bot message
    st.session_state.messages.append({"role": "bot", "content": response})
    with st.chat_message("bot"):
        st.markdown(response)