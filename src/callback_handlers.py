from main_bot import bot
from telebot.types import (InlineKeyboardMarkup,
                           InlineKeyboardButton,
                           SwitchInlineQueryChosenChat)
from telebot.util import quick_markup


@bot.message_handler(commands=['social'])
def list_social_media(message):
    social = quick_markup({
        'Chapa': {'pay': True},
        'Twitter': {'url': 'https://twitter.com'},
        'Facebook': {'url': 'https://facebook.com'},
        'Back': {'callback_data': 'whatever'}
    }, row_width=2)

    bot.send_message(message.chat.id, 'social medias', reply_markup=social)


@bot.message_handler(commands=['confirm'])
def confirm_command(message):

    markup = InlineKeyboardMarkup()
    markup.row_width = 1

    markup.add(InlineKeyboardButton(
        'admin',
        switch_inline_query_chosen_chat=SwitchInlineQueryChosenChat(
            'admin', allow_user_chats=True)),

               InlineKeyboardButton('confirm', callback_data='confirm'),
               InlineKeyboardButton('cancel', callback_data='cancel'))
    bot.send_message(message.chat.id, "Are you sure you want to confirm?",
                     reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    callback_data = call.data
    callback_sender = call.from_user

    if callback_data == 'confirm':
        bot.answer_callback_query(call.id, text="confirmed", show_alert=True)
    elif callback_data == 'cancel':
        bot.answer_callback_query(
            call.id,
            f"{callback_sender.first_name} you have cancelled it")
