from django.shortcuts import render
import telebot

from .bot import bot
from jasa.settings import URL, BOT_TOKEN


def webhook(request):
    """Setup a webhook."""
    bot.remove_webhook()
    bot.set_webhook(url=URL + BOT_TOKEN)
    return '!'


def process_updates(request):
    """Receive requests from telegram API."""
    if request.method == 'POST':
        bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
        return "!"
    else:
        return "Access Denied"