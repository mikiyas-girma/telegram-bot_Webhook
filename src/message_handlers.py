from main_bot import bot
from telebot.types import (ReplyKeyboardMarkup, KeyboardButton,
                           KeyboardButtonPollType, ChatPhoto)


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    keyboard = ReplyKeyboardMarkup(one_time_keyboard=True)
    keyboard.resize_keyboard = True
    keyboard.row_width = 3
    keyboard.add(KeyboardButton('finish'),
                 KeyboardButton(
                     'create poll',
                     request_poll=KeyboardButtonPollType('regular')))

    print(bot.get_chat_member_count('@tikvahethiopia'))

    bot.send_message(message.chat.id, f"{message.from_user.first_name}" +
                     " you fine? ", reply_markup=keyboard)


def handle_command(bot, message):
    command = message.text
    if command == "/photo":
        bot.send_message(message.chat.id, text="Please upload jpg type image")
    elif command == "/videos":
        bot.send_message(message.chat.id, text="Please upload video")
    elif command == "/doc":
        bot.send_message(message.chat.id, text="Please upload your doc")


@bot.message_handler(content_types=['photo'])
def handle_photo_upload(message):
    photo_file_id = message.photo[-1].file_id
    file_info = bot.get_file(photo_file_id)
    bot.send_message(message.chat.id, file_info.file_path)
    bot.send_photo(message.chat.id, photo_file_id,
                   caption="Thank you for uploading photo!")


uploaded_videos = {}


@bot.message_handler(content_types=['video'])
def handle_video_upload(message):
    video_file_id = message.video.file_id
    # bot.send_message(message.chat.id, f"{message.video}\
    #                  thank you for the video")
    bot.send_video(message.chat.id, video_file_id,
                   caption="here is what you sent")
    uploaded_videos[message.chat.id] = video_file_id


@bot.message_handler(commands=['showvideo'])
def show_uploaded_video(message):
    chat_id = message.chat.id
    if chat_id in uploaded_videos:
        video_file_id = uploaded_videos[chat_id]
        bot.send_video(chat_id, video_file_id)
    else:
        bot.send_message(chat_id, "No video was uploaded previously.")


@bot.message_handler(commands=['link'])
def send_link(message):
    bot.send_message(message.chat.id,
                     "link to the bot: http://t.me/Pybot_exBot")


@bot.message_handler(commands=['photo', 'videos'])
def prompt_user(message):
    handle_command(bot, message)
