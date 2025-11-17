from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    fullname = request.form["fullname"]

    message = f"🔔 Нове повідомлення!\nСтудент: {fullname}"

    requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                 params={"chat_id": CHAT_ID, "text": message})

    return "Дякую! Дані відправлено викладачу."
