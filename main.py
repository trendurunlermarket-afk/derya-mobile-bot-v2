from flask import Flask, request
import telegram
import os

app = Flask(__name__)

BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
bot = telegram.Bot(token=BOT_TOKEN)

@app.route('/')
def home():
    return "Derya Mobile Bot v2 is running 💚"

@app.route('/start', methods=['GET', 'POST'])
def start():
    chat_id = request.args.get('chat_id')
    if chat_id:
        bot.send_message(chat_id=chat_id, text="Merhaba! Derya Mobile Bot v2 aktif 💬")
        return "Message sent!"
    return "No chat_id provided."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
