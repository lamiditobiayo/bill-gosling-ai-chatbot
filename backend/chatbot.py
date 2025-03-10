import os
import openai
from flask import Flask, request, jsonify
from backend.config import OPENAI_API_KEY  # Ensure this is correct

# Initialize OpenAI client
client = openai.OpenAI(api_key=OPENAI_API_KEY)

# Initialize Flask app
app = Flask(__name__)

# Bill Gosling Outsourcing Knowledge Base
BGO_KNOWLEDGE_BASE = {
    "mission": "To empower businesses to deliver extraordinary customer experiences.",
    "core_values": [
        "Never Satisfied",
        "Able to Grow, Eager",
        "Make Others Better",
        "Creativity and Innovation",
        "Have Fun, Energetic"
    ],
    "services": [
        "Account Receivables Management",
        "Customer Experience",
        "Sales and Acquisition",
        "Data Excellence",
        "Quality Services",
        "Professional Services",
        "NEQQO",
        "GooseTek",
        "B2B Collections Platform",
        "Learning and Content Development",
        "Workforce Management Solution"
    ],
    "resources": [
        "E-Books",
        "Whitepapers",
        "Case Studies",
        "Blogs",
        "Data Visualization"
    ],
    "book_of_bill": "An internal resource at BGO that outlines company policies, procedures, and cultural values, serving as a guide for employees."
}

def get_knowledge_response(user_input):
    """
    Checks if the user query matches any predefined knowledge in the BGO database.
    """
    user_input = user_input.lower()
    
    if "mission" in user_input:
        return BGO_KNOWLEDGE_BASE["mission"]
    elif "core values" in user_input:
        return ", ".join(BGO_KNOWLEDGE_BASE["core_values"])
    elif "services" in user_input:
        return ", ".join(BGO_KNOWLEDGE_BASE["services"])
    elif "resources" in user_input:
        return ", ".join(BGO_KNOWLEDGE_BASE["resources"])
    elif "book of bill" in user_input:
        return BGO_KNOWLEDGE_BASE["book_of_bill"]
    else:
        return None  # If not found, return None so the chatbot uses OpenAI

@app.route("/chat", methods=["POST"])
def chat():
    """
    API endpoint to receive user messages and return AI responses.
    """
    data = request.get_json()
    user_input = data.get("message", "")

    # Check knowledge base first
    knowledge_response = get_knowledge_response(user_input)
    if knowledge_response:
        return jsonify({"response": knowledge_response})

    # If not in knowledge base, use OpenAI
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "You are a helpful assistant knowledgeable about Bill Gosling Outsourcing."},
                      {"role": "user", "content": user_input}],
            temperature=0.7
        )
        return jsonify({"response": response.choices[0].message.content})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/", methods=["GET"])
def home():
    return "Backend is running!"

# Run the Flask app (only in local development)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
