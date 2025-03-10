import os
import openai
from config import OPENAI_API_KEY  # Fix import issue

# Initialize OpenAI client
client = openai.OpenAI(api_key=OPENAI_API_KEY)

def get_chatbot_response(user_input):
    """
    Sends user input to OpenAI and returns chatbot response.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "You are a helpful assistant."},
                      {"role": "user", "content": user_input}],
            temperature=0.7
        )
        return response.choices[0].message.content
    
    except Exception as e:
        return f"Error: {str(e)}"
