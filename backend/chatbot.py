import os
import openai
from flask import Flask, request, jsonify
from backend.config import OPENAI_API_KEY  # Fixed import path

# Initialize OpenAI client
client = openai.OpenAI(api_key=OPENAI_API_KEY)

# Initialize Flask app
app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    """
    API endpoint to receive user messages and return AI responses.
    """
    data = request.get_json()
    user_input = data.get("message", "")

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "You are a helpful assistant."},
                      {"role": "user", "content": user_input}],
            temperature=0.7
        )
        return jsonify({"response": response.choices[0].message.content})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask app (only in local development)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
