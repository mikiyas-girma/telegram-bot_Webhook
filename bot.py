import telebot
import os
import requests

BOT_TOKEN = os.getenv('BOT_TOKEN')
WEBHOOK_URL = os.getenv('WEBHOOK_URL')

bot = telebot.TeleBot(BOT_TOKEN)

# Set the webhook URL to receive updates from Telegram
bot.set_webhook(url=WEBHOOK_URL)


# Add handler for text messages
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Echo the message back to the user
    bot.send_message(message.chat.id, message.text)
    bot.send_message(message.chat.id, "sent pro")

    # Process the message sent by the user
    process_input(message.chat.id, message.text)


# Function to process user input
def process_input(chat_id, text):
    try:
        requests.post(WEBHOOK_URL,
                      json={'chat_id': chat_id, 'text': text})
    except requests.exceptions.RequestException as e:
        print("Error occurred while sending message to Flask server:", e)


if __name__ == "__main__":
    bot.infinity_polling()
