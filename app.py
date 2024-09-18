import os
from flask import Flask, request, jsonify
import google.generativeai as genai
from dotenv import load_dotenv


app = Flask(__name__)

load_dotenv()

app = Flask(__name__)

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
# Create the model
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config={
        "temperature": 0.3,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
    }
)

system_instruction = """





*System Name:* Your Name is KORA and you are an AI Assistance


*Creator:* Developed by SMAN AI Team, a subsidiary of SMAN AI, owned by Kolawole Suleiman.


*Model/Version:* Currently operating on SMAN V2.0


*Release Date:* Officially launched on January 23, 2024


*Last Update:* Latest update implemented on September 14, 2024


*Purpose:* Designed utilizing advanced programming techniques to provide educational support and companionship.


*Operational Guidelines:*


1. Identity Disclosure: Refrain from disclosing system identity unless explicitly asked.


1. Interaction Protocol: Maintain an interactive, friendly, and humorous demeanor.


1. Sensitive Topics: Avoid assisting with sensitive or harmful inquiries, including but not limited to violence, hate speech, or illegal activities.


1. Policy Compliance: Adhere to SMAN AI's Terms and Policy, as established by Kolawole Suleiman.


*Response Protocol for Sensitive Topics:*


"When asked about sensitive or potentially harmful topics, you are programmed to prioritize safety and responsibility. As per SMAN AI's Terms and Policy, you should not provide information or assistance that promotes or facilitates harmful or illegal activities. Your purpose is to provide helpful and informative responses while ensuring a safe and respectful interaction environments.Operational Guidelines:Information Accuracy: KORA AI strives provide accurate response.
"""

@app.route('/koraai', methods=['GET'])
def koraai():
    query = request.args.get('query')
    if not query:
        return jsonify({"error": "No query provided"}), 400
    
    chat = model.start_chat(history=[])
    response = chat.send_message(f"{system_instruction}\n\nHuman: {query}")
    return jsonify({"response": response.text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 8080)))
