import os
import telebot
from flask import Flask, request
from telegram_utils import create_bot, set_webhook, send_message, handle_command

app = Flask(__name__)

BOT_TOKEN = os.getenv('BOT_TOKEN')
WEBHOOK_URL = os.getenv('WEBHOOK_URL')

bot = create_bot(BOT_TOKEN)

set_webhook(bot, WEBHOOK_URL)


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    # bot.send_message(message.chat.id, "Hey welcome to our bot!")
    send_message(bot, message.chat.id, "Hey server to our bot!")


@bot.message_handler(content_types=['photo'])
def handle_photo_upload(message):
    photo_file_id = message.photo[-1].file_id
    # retrieve information about the photo
    file_info = bot.get_file(photo_file_id)
    bot.send_message(message.chat.id, file_info.file_path)
    bot.send_photo(message.chat.id, photo_file_id,
                   caption="Thank you for uploading photo!")


@bot.message_handler(commands=['link'])
def send_link(message):
    send_message(bot, message.chat.id,
                 "Here is the link to the bot: http://t.me/Pybot_exBot")


@bot.message_handler(commands=['photo', 'videos'])
def prompt_user(message):
    handle_command(bot, message)


@app.route('/webhook', methods=['POST'])
def webhook_handler():
    update = request.json
    if update and 'message' in update:
        bot.process_new_updates([telebot.types.Update.de_json(update)])
    return '', 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
