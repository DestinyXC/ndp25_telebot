import telebot
from flask import Flask, request
import os

# Initialize bot with your API token
TOKEN = '7857517263:AAEKGJodf5GxBTW_WV-mWOgOnvwXzRMQM6I'
bot = telebot.TeleBot(TOKEN)

# Initialize Flask application
app = Flask(__name__)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! I am your bot.")

# Webhook endpoint
@app.route('/{}'.format(TOKEN), methods=['POST'])
def webhook():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return '', 200

@app.route('/')
def index():
    return "Hello, I'm running on Render!"

# Set the webhook for Telegram
def set_webhook():
    webhook_url = f'https://ndp25_telebot.onrender.com/{TOKEN}'
    bot.remove_webhook()
    bot.set_webhook(url=webhook_url)

if __name__ == "__main__":
    # Call the function to set the webhook
    set_webhook()
    app.run(host='0.0.0.0', port=5000)
