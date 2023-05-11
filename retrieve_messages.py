import os
import json
from telegram import Bot

def retrieve_telegram_messages():
    token = os.environ['6260648302:AAHaX4DZ3C2780jJW90gXXGVFhdzYUmhq68']
    bot = Bot(token=token)
    chat_id = '6260648302'  # Replace with the actual group chat ID

    messages = bot.get_chat_history(chat_id=chat_id, limit=100)  # Adjust the limit as needed
    message_texts = [message.text for message in messages]

    with open('messages.json', 'w') as file:
        json.dump(message_texts, file)

retrieve_telegram_messages()


