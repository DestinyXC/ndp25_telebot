import os
from flask import Flask, request
import telebot

# Retrieve the bot token from the environment variable
BOT_TOKEN = os.getenv('BOT_TOKEN')
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN environment variable is not set!")

# Initialize Flask app and Telegram bot
app = Flask(__name__)
bot = telebot.TeleBot(BOT_TOKEN)

# Define a simple command handler
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! I'm your bot.")

# Handle incoming webhook updates
@app.route("/", methods=["POST"])
def webhook():
    if request.headers.get("content-type") == "application/json":
        json_string = request.get_data().decode("utf-8")
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return "OK", 200
    else:
        return "Unsupported Media Type", 415

# Set the webhook URL when the app starts
if __name__ == "__main__":
    # Remove any existing webhook
    bot.remove_webhook()
    # Set the webhook to your Render service's URL
    bot.set_webhook(url="https://ndp25_telebot.onrender.com/")
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 8080)))