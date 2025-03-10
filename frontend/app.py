import streamlit as st
import requests

# Set page title
st.set_page_config(page_title="Bill Gosling AI Chatbot")

# Display title and description
st.title("Bill Gosling AI Chatbot")
st.write("Welcome! I'm here to assist you. Ask me anything.")

# Backend API URL (Update this with your Render backend URL)
BACKEND_URL = "https://bill-gosling-chatbot-api.onrender.com/chat"  # Replace with your actual URL

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Type your message here..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Send user input to backend
    try:
        response = requests.post(BACKEND_URL, json={"message": prompt})
        response_data = response.json()
        chatbot_reply = response_data.get("response", "Error: No response received.")

    except Exception as e:
        chatbot_reply = f"Error: {str(e)}"

    # Add chatbot response to chat history
    st.session_state.messages.append({"role": "assistant", "content": chatbot_reply})
    # Display chatbot response
    with st.chat_message("assistant"):
        st.markdown(chatbot_reply)
