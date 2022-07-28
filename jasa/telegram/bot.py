import telebot
from jasa.settings import BOT_TOKEN


bot = telebot.Telebot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        'Hello user!'
    )