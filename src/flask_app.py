import telebot
from main_bot import bot
from flask import Flask, request
import message_handlers
import inline_handlers
import callback_handlers
import keyboards

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook_handler():
    update = telebot.types.Update.de_json(
        request.stream.read().decode('utf-8'))
    bot.process_new_updates([update])
    return '', 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
