from flask import Flask, request
from telegram_utils import create_bot, set_webhook, setup_handlers
import telebot
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv('BOT_TOKEN')
WEBHOOK_URL = os.getenv('WEBHOOK_URL')

bot = create_bot(BOT_TOKEN)

set_webhook(bot, WEBHOOK_URL)
setup_handlers(bot)


@app.route('/webhook', methods=['POST'])
def webhook_handler():
    update = request.json
    if update and 'message' in update:
        bot.process_new_updates([telebot.types.Update.de_json(update)])
    return '', 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
