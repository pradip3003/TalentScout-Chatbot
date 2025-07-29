import streamlit as st
# --- Custom Styling for Dark Theme and UI Enhancements ---
# --- Sleek Dark Theme Styling for TalentScout ---
# --- ChatGPT-Style Clean UI for TalentScout ---
st.markdown("""
    <style>
    html, body, .stApp {
        background-color: #f5f5f5;
        color: #333;
        font-family: 'Segoe UI', sans-serif;
    }
    .main {
        max-width: 800px;
        margin: auto;
        padding: 2rem;
        background-color: #ffffff;
        border-radius: 20px;
        box-shadow: 0 0 20px rgba(0, 0, 0, 0.05);
    }
    .stTextInput > div > div > input,
    .stSelectbox > div,
    textarea {
        background-color: #ffffff !important;
        color: #000 !important;
        border: 1px solid #ccc;
        border-radius: 12px;
        padding: 10px;
        font-size: 1rem;
    }
    .stButton > button {
        background-color: #10a37f;
        color: white;
        font-weight: bold;
        padding: 10px 20px;
        border-radius: 12px;
        border: none;
        transition: all 0.3s ease-in-out;
        font-size: 1rem;
    }
    .stButton > button:hover {
        background-color: #0e8c6d;
        cursor: pointer;
    }
    </style>
""", unsafe_allow_html=True)



# Title
st.title("💼 TalentScout - Hiring Assistant Chatbot")

# Sidebar
st.sidebar.title("Candidate Information")

# Collect candidate information
name = st.sidebar.text_input("Name")
email = st.sidebar.text_input("Email")
phone = st.sidebar.text_input("Phone Number")
experience = st.sidebar.selectbox("Years of Experience", ["Fresher", "1-2", "3-5", "5+"])
tech_stack = st.sidebar.multiselect("Tech Stack", ["Python", "JavaScript", "React", "Node.js", "MongoDB", "SQL", "Java", "C++"])

# Generate questions button
if st.sidebar.button("Generate Interview Questions"):
    st.subheader(f"👤 Candidate: {name}")
    st.write(f"📧 Email: {email}")
    st.write(f"📞 Phone: {phone}")
    st.write(f"🧠 Experience: {experience}")
    st.write(f"🛠️ Tech Stack: {', '.join(tech_stack)}")

    st.markdown("### 🔍 Suggested Technical Questions:")
    
    if "Python" in tech_stack:
        st.write("- What are Python decorators and how do you use them?")
        st.write("- Explain list vs tuple.")
    if "JavaScript" in tech_stack:
        st.write("- What is closure in JavaScript?")
        st.write("- Difference between var, let, and const?")
    if "React" in tech_stack:
        st.write("- What are hooks in React?")
        st.write("- What is the virtual DOM?")
    if "Node.js" in tech_stack:
        st.write("- How does event-driven architecture work in Node.js?")
        st.write("- What are streams in Node.js?")
    if "MongoDB" in tech_stack:
        st.write("- Difference between MongoDB and SQL?")
        st.write("- Explain schema design in MongoDB.")
    if "SQL" in tech_stack:
        st.write("- What is normalization?")
        st.write("- Write a SQL query to fetch the second highest salary.")
    if "Java" in tech_stack:
        st.write("- What is OOP? Explain with Java example.")
    if "C++" in tech_stack:
        st.write("- What is the difference between pointer and reference in C++?")

    st.success("✅ Questions Generated!")
