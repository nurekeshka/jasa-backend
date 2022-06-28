from django.core.management.base import BaseCommand
from django.conf import settings
from telebot import TeleBot
from telebot import types


bot = TeleBot(settings.TELEGRAM_BOT_TOKEN, threaded=False)




class Command(BaseCommand):
    help = 'Telegram bot setup command'

    def handle(self, *args, **kwargs):
        bot.enable_save_next_step_handlers(delay=2)
        bot.load_next_step_handlers()
        bot.infinity_polling()
