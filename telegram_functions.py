# from telegram_utils import send_message, handle_command
# from flask_app import bot


# @bot.message_handler(commands=['start', 'hello'])
# def send_welcome(message):
#     send_message(bot, message.chat.id, "Hey welcome to our bot!")


# @bot.message_handler(content_types=['photo'])
# def handle_photo_upload(message):
#     photo_file_id = message.photo[-1].file_id
#     file_info = bot.get_file(photo_file_id)
#     bot.send_message(message.chat.id, file_info.file_path)
#     bot.send_photo(message.chat.id, photo_file_id,
#                    caption="Thank you for uploading photo!")


# @bot.message_handler(commands=['link'])
# def send_link(message):
#     send_message(bot, message.chat.id,
#                  "Here is the link to the bot: http://t.me/Pybot_exBot")


# @bot.message_handler(commands=['photo', 'videos'])
# def prompt_user(message):
#     handle_command(bot, message)
