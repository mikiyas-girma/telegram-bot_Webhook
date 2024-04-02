from io import BytesIO
import logging
import requests
import telebot
import os
from telebot import types

BOT_TOKEN = os.getenv('BOT_TOKEN')
WEBHOOK_URL = os.getenv('WEBHOOK_URL')

bot = telebot.TeleBot(BOT_TOKEN)
bot.set_webhook(WEBHOOK_URL)


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"{message.from_user.first_name}" +
                     " ye geta sra dink nw ")


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


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Echo the message back to the user
    print(message.text)
    bot.send_message(message.chat.id, message.text)


# bot.remove_webhook()


@bot.inline_handler(lambda query: query.query == 'miki')
def query_text(inline_query):
    try:
        m1 = types.InlineQueryResultArticle(
            '100',
            'the wine',
            types.InputTextMessageContent('wine to water'),
            url='you.com')
        m2 = types.InlineQueryResultArticle(
            '101',
            'mike\'s ceo on',
            types.InputTextMessageContent('no cache after all'),
            url='soap.com')
        w1 = types.InlineQueryResultArticle(
            '2193',
            '/start',
            types.InputTextMessageContent('/start'))

        bot.answer_inline_query(inline_query.id, [m1, m2, w1], cache_time=0)
    except Exception as e:
        logging.error("Error handling inline query: %s", e)
        print(e)


@bot.inline_handler(lambda query: query.query == 'admin')
def query_admin(inline_query):
    try:
        a1 = types.InlineQueryResultArticle(
            '11',
            'Admin?',
            types.InputTextMessageContent('mikias girma'),
            url='mikegirma.vercel.app.com')

        bot.answer_inline_query(inline_query.id, [a1], cache_time=0)
    except Exception as e:
        logging.error("Error handling inline query: %s", e)
        print(e)


@bot.inline_handler(lambda query: query.query == 'photo')
def query_photo(inline_query):
    try:
        r = types.InlineQueryResultPhoto(
            '1',
            'https://raw.githubusercontent.com/eternnoir/pyTelegramBotAPI/master/examples/detailed_example/kitten.jpg',
            'https://raw.githubusercontent.com/eternnoir/pyTelegramBotAPI/master/examples/detailed_example/kitten.jpg',
            input_message_content=types.InputTextMessageContent('ava photo'))

        r2 = types.InlineQueryResultPhoto(
            '2',
            'https://raw.githubusercontent.com/eternnoir/pyTelegramBotAPI/master/examples/detailed_example/rooster.jpg',
            'https://raw.githubusercontent.com/eternnoir/pyTelegramBotAPI/master/examples/detailed_example/rooster.jpg')

        p1 = types.InlineQueryResultPhoto(
            '3',
            'https://img.freepik.com/premium-vector/single-line-drawing-male-businessman-typing-business-ideas-concept-laptop-while-sitting-premi_615031-256.jpg',
            'https://img.freepik.com/premium-vector/single-line-drawing-male-businessman-typing-business-ideas-concept-laptop-while-sitting-premi_615031-256.jpg',
            caption='Programmer',
            description='Programmer typing code')

        bot.answer_inline_query(inline_query.id, [r, r2, p1], cache_time=0)

    except Exception as e:
        logging.error("Error handling inline query: %s", e)


@bot.inline_handler(lambda query: query.query == 'video')
def query_video(inline_query):
    try:
        r = types.InlineQueryResultVideo(
            '1',
            'https://github.com/eternnoir/pyTelegramBotAPI/blob/master/tests/test_data/test_video.mp4?raw=true',
            'video/mp4',
            'https://raw.githubusercontent.com/eternnoir/pyTelegramBotAPI/master/examples/detailed_example/rooster.jpg',
            'Title'
            )
        bot.answer_inline_query(inline_query.id, [r])
    except Exception as e:
        print(e)


@bot.inline_handler(lambda query: query.query == 'audio')
def query_audio(inline_query):
    try:
        a1 = types.InlineQueryResultAudio(
            '11',
            'https://archive.org/download/mona_lisa_2403.poem_librivox/monalisa_horsford_dbw_128kb.mp3',
            title='monalisa',
            caption='piano'
            )

        bot.answer_inline_query(inline_query.id, [a1], cache_time=300)

    except Exception as e:
        logging.error("error handling inline query: %s", e)


# @bot.inline_handler(lambda query: query.query == 'audio')
# def query_audio(inline_query):
    """
    the following commented function is best if the audio link is not
    supported by telegram api and when it can't handle it
    """
#     try:
#         audio_url = 'https://www.kozco.com/tech/piano2.wav'
#         with requests.get(audio_url, stream=True, timeout=4) as r:
#             r.raise_for_status()
#             audio_data = BytesIO(r.content)
#             audio_data.name = 'piano2.wav'
#             bot.send_audio(inline_query.from_user.id, audio_data,
#                            title='mike music',
#                            caption='piano')

#     except requests.exceptions.Timeout as e:
#         logging.error("Timeout error: %s", e)
#         bot.answer_inline_query(inline_query.id, [], cache_time=300,
#                                 switch_pm_text="Error: Timeout occurred",
#                                 switch_pm_parameter="timeout")

#     except Exception as e:
#         logging.error("Error handling inline query: %s", e)
#         bot.answer_inline_query(inline_query.id, [], cache_time=300,
#                                 switch_pm_text="Error: Something went wrong",
#                                 switch_pm_parameter="error")


@bot.inline_handler(lambda query: len(query.query) == 0)
def default_query(inline_query):
    """handle when no query term is inserted"""
    try:
        r = types.InlineQueryResultArticle(
            '1',
            'default',
            types.InputTextMessageContent('default'))

        bot.answer_inline_query(inline_query.id, [r])

    except Exception as e:
        print(e)
