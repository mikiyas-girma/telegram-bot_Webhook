from main_bot import bot
import telebot


# Handler for /confirm command
@bot.message_handler(commands=['confirm'])
def confirm_command(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_confirm = telebot.types.InlineKeyboardButton(
        'Confirm',
        callback_data='confirm')
    keyboard.row(button_confirm)
    bot.send_message(message.chat.id, "Are you sure you want to confirm?",
                     reply_markup=keyboard)


# Handler for inline callback query
@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    # Extract information from the callback query
    callback_data = call.data
    chat_id = call.message.chat.id

    # Perform custom logic based on the callback data
    if callback_data == 'confirm':
        bot.send_message(chat_id, "You confirmed!")
        bot.answer_callback_query(call.id)
    elif callback_data == 'cancel':
        bot.send_message(chat_id, "You canceled!")
        bot.answer_callback_query(call.id)
