import telebot
import os
import requests

BOT_TOKEN = os.getenv('BOT_TOKEN')
WEBHOOK_URL = os.getenv('WEBHOOK_URL')

bot = telebot.TeleBot(BOT_TOKEN)


# Set the webhook URL to receive updates from Telegram
def set_webhook():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/\
            setWebhook?url={WEBHOOK_URL}/webhook"
    response = requests.post(url)
    if response.status_code == 200:
        print("Webhook has been set successfully")
    else:
        print("Failded to set the webhook")


set_webhook()


# Add your message handlers here
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.send_message(message.chat.id, text="Hey welcome to our bot!")


@bot.message_handler(commands=['link'])
def send_link(message):
    bot.send_message(message.chat.id,
                     text="Here is link to the bot: http://t.me/Pybot_exBot")


@bot.message_handler(commands=['photo', 'videos'])
def prompt_user(message):
    command = message.text
    if command == "/photo":
        bot.send_message(message.chat.id, text="Please upload jpg type image")
    elif command == "/videos":
        bot.send_message(message.chat.id, text="Please upload video")
    elif command == "/doc":
        bot.send_message(message.chat.id, text="Please upload your doc")


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
