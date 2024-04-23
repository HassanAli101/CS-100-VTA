# Final app.py
# import files
from flask import Flask, render_template, request, session
import google.generativeai as genai  # Importing the Gemini library

app = Flask(__name__)
app.secret_key = 'AIzaSyCI8TKWRfx6faRSQLc0SvyytvHXHnIaP7s'  # Replace with your actual secret key

# Replace 'XYZ' with your actual Gemini API key
GOOGLE_API_KEY = "AIzaSyCI8TKWRfx6faRSQLc0SvyytvHXHnIaP7s"
genai.configure(api_key=GOOGLE_API_KEY)

# Start a chat session with the Gemini model
chat_model = genai.GenerativeModel('gemini-pro')
chat = chat_model.start_chat(history=[])

@app.route("/")
def home():
    session['chat_history'] = []  # Initialize conversation history
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    response = chat.send_message(userText)
    # Store only the text part of the response in the session
    session['chat_history'].append({'user': userText, 'bot': response.text})
    return response.text

if __name__ == "__main__":
    app.run()
