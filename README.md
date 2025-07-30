# TalentScout - AI-Powered Hiring Assistant Chatbot

TalentScout is an intelligent chatbot designed to assist recruitment agencies in collecting candidate information and generating relevant technical questions based on the candidate's tech stack.

## Features

* **Collects Candidate Details**: Gathers essential information such as name, email, phone number, years of experience, desired position, and location.
* **Tech Stack Input**: Allows candidates to provide their tech stack as a comma-separated list.
* **Automatic Question Generation**: Generates technical questions dynamically based on the provided tech stack (currently supports Python, React, Node, and SQL).
* **User-Friendly Interface**: Features a clean and interactive chat interface built with Streamlit.
* **Input Validation**: Basic validation for email and phone number formats.
* **Conversation Flow Management**: Guides the user through a structured conversation to gather all necessary details.
* **Exit Functionality**: Users can type 'exit', 'quit', or 'bye' at any point to end the chat.

## Tech Stack

* **Frontend**: Streamlit (Python-based UI framework)
* **Backend**: Python
* **Logic**: Custom Python logic for managing conversation flow, data collection, and question generation.

## How to Run the Project

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/pradip3003/TalentScout-Chatbot.git](https://github.com/pradip3003/TalentScout-Chatbot.git)
    cd TalentScout-Chatbot
    ```

2.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```
    (You will need to create a `requirements.txt` file in your project with `streamlit` listed in it).

3.  **Run the Streamlit application:**

    ```bash
    streamlit run app.py
    ```

## Example Interaction

Here's a sample flow of how the chatbot interacts with a user:

**Bot**: 👋 Hello! I'm TalentScout, your AI hiring assistant. I'll ask you a few questions to learn more about your skills, and generate technical questions based on your tech stack. Type 'exit' or 'quit' anytime to end the chat.

**User**: My name is John Doe

**Bot**: Great! Can you share your 📧 email address?

**User**: john.doe@example.com

**Bot**: Thanks! What's your 📞 phone number?

**User**: 1234567890

**Bot**: How many years of 🧠 experience do you have? (e.g. Fresher, 1-2, 3-5, 5+)

**User**: 3-5

**Bot**: Which position are you applying for? 💼

**User**: Software Engineer

**Bot**: Where are you currently located? 📍

**User**: New York

**Bot**: Please list the 🛠️ tech stack you know (comma-separated: Python, React, etc.)

**User**: Python, React, SQL

**Bot**: Generating technical questions based on your skills...

**Bot**: What are Python's key features?
**Bot**: Explain the difference between list and tuple in Python.
**Bot**: How does Python handle memory management?
**Bot**: What is the virtual DOM in React?
**Bot**: Explain the difference between props and state.
**Bot**: What is normalization in SQL?
**Bot**: What is the difference between DELETE and TRUNCATE?

**Bot**: 👋 That’s all for now! Thank you, and we’ll be in touch shortly.

## Project Structure
TalentScout-Chatbot/
├── app.py          # Main chatbot logic and Streamlit application
└── README.md       # Project documentation (this file)


## Developer Info

Pradeep Suryawanshi
BCA Student, Bharati Vidyapeeth, Pune
Skills: Python, Web Development, AI Tools, Freelancing
