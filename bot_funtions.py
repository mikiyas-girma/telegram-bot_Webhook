import telebot
import os

BOT_TOKEN = os.getenv('BOT_TOKEN')
WEBHOOK_URL = os.getenv('WEBHOOK_URL')


def create_bot(bot_token):
    return telebot.TeleBot(bot_token)


def set_webhook(bot, webhook_url):
    bot.remove_webhook()
    bot.set_webhook(url=webhook_url)


def send_message(bot, chat_id, text):
    bot.send_message(chat_id, text)


def handle_command(bot, message):
    command = message.text
    if command == "/photo":
        bot.send_message(message.chat.id, text="Please upload jpg type image")
    elif command == "/videos":
        bot.send_message(message.chat.id, text="Please upload video")
    elif command == "/doc":
        bot.send_message(message.chat.id, text="Please upload your doc")
