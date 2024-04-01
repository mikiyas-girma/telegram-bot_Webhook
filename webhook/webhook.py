import requests
import os
from flask import Flask, request

app = Flask(__name__)

BOT_TOKEN = os.getenv('BOT_TOKEN')


def send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    data = {'chat_id': chat_id, 'text': text}
    response = requests.post(url, json=data)
    return response.json()


@app.route('/webhook', methods=['POST'])
def webhook_handler():
    update = request.json
    if update and 'message' in update:
        message_text = update['message'].get('text', '')
        chat_id = update['message']['chat']['id']

        if message_text == '/start':
            send_message(chat_id, "Welcome to the bot! How can I assist you?")
        else:
            # simply echoing back the received message
            send_message(chat_id, message_text)
    return '', 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
