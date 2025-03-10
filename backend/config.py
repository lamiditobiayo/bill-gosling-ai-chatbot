import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get OpenAI API Key from environment
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Check if API key is found
if not OPENAI_API_KEY:
    raise ValueError("OpenAI API key is missing! Add it to the .env file or Render environment variables.")
