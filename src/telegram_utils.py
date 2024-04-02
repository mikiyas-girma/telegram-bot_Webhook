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


def bot_handlers(bot):
    @bot.message_handler(commands=['start', 'hello'])
    def send_welcome(message):
        bot.send_message(message.chat.id, f"{message.from_user.first_name}" +
                         " welcome to our bot!")

    @bot.message_handler(content_types=['photo'])
    def handle_photo_upload(message):
        photo_file_id = message.photo[-1].file_id
        file_info = bot.get_file(photo_file_id)
        bot.send_message(message.chat.id, file_info.file_path)
        bot.send_photo(message.chat.id, photo_file_id,
                       caption="Thank you for uploading photo!")

    @bot.message_handler(commands=['link'])
    def send_link(message):
        bot.send_message(message.chat.id,
                         "link to the bot: http://t.me/Pybot_exBot")

    @bot.message_handler(commands=['photo', 'videos'])
    def prompt_user(message):
        handle_command(bot, message)
