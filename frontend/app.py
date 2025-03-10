import streamlit as st
import requests

# Set page title
st.set_page_config(page_title="Bill Gosling AI Chatbot")

# Display title and description
st.title("Bill Gosling AI Chatbot")
st.write("Welcome! I can answer your questions about Bill Gosling Outsourcing.")

# Backend API URL (Update this with your Render backend URL)
BACKEND_URL = "https://bill-gosling-chatbot-api.onrender.com/chat"  # Replace with your actual URL

# Test if backend is running
try:
    health_check = requests.get("https://bill-gosling-chatbot-api.onrender.com/")
    if health_check.status_code != 200:
        st.error("Backend is not responding. Please check the server status.")
except:
    st.error("Backend is down. Please restart the service.")

# Chat functionality...
