import telebot

from jasa.settings import BOT_TOKEN
from .decorators import get_telegram_user

print(BOT_TOKEN)
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
@get_telegram_user
def start(message, user):
    bot.send_message(
        message.chat.id,
        'Hello user!'
    )
