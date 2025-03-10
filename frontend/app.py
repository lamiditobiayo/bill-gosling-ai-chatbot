import streamlit as st
import requests

# Set page title
st.set_page_config(page_title="Bill Gosling AI Chatbot")

# Display title and description
st.title("Bill Gosling AI Chatbot")
st.write("Welcome! I can answer your questions about Bill Gosling Outsourcing.")

# Backend API URL (Update this with your Render backend URL)
BACKEND_URL = "https://bill-gosling-chatbot-api.onrender.com/chat"  # Replace with your actual URL

# Knowledge Base Shortcuts
BGO_TOPICS = {
    "Mission": "What is the mission of Bill Gosling Outsourcing?",
    "Core Values": "What are the core values of Bill Gosling Outsourcing?",
    "Services": "What services does Bill Gosling Outsourcing offer?",
    "Resources": "What resources does Bill Gosling Outsourcing provide?",
    "Book of Bill": "What is the Book of Bill at Bill Gosling Outsourcing?"
}

# Sidebar for Knowledge Base Shortcuts
st.sidebar.header("📖 Bill Gosling Knowledge Base")
for topic, query in BGO_TOPICS.items():
    if st.sidebar.button(topic):
        st.session_state["messages"].append({"role": "user", "content": query})
        response = requests.post(BACKEND_URL, json={"message": query})
        chatbot_reply = response.json().get("response", "Error retrieving response.")
        st.session_state["messages"].append({"role": "assistant", "content": chatbot_reply})

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Type your question here..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Send user input to backend
    try:
        response = requests.post(BACKEND_URL, json={"message": prompt}, timeout=10)
        if response.status_code == 200:
            response_data = response.json()
            chatbot_reply = response_data.get("response", "I am unable to respond at the moment.")
        else:
            chatbot_reply = f"Error {response.status_code}: Backend is not responding."

    except requests.exceptions.RequestException as e:
        chatbot_reply = f"Error: Unable to connect to backend. ({str(e)})"

    # Add chatbot response to chat history
    st.session_state.messages.append({"role": "assistant", "content": chatbot_reply})
    # Display chatbot response
    with st.chat_message("assistant"):
        st.markdown(chatbot_reply)
