import sys
import os

# Ensure the backend folder is in the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "backend")))

import streamlit as st
from chatbot import get_chatbot_response  # Import chatbot function correctly

# Set page title
st.set_page_config(page_title="Bill Gosling AI Chatbot")

# Display title and description
st.title("Bill Gosling AI Chatbot")
st.write("Welcome! I'm here to assist you. Ask me anything.")

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

    # Get chatbot response
    response = get_chatbot_response(prompt)
    # Add chatbot response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
    # Display chatbot response
    with st.chat_message("assistant"):
        st.markdown(response)
