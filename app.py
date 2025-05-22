from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.form["user_input"]
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are Max AI, a helpful educational assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        reply = response.choices[0].message["content"]
    except Exception as e:
        reply = f"Error: {e}"
    return render_template("index.html", user_input=user_input, bot_response=reply)
