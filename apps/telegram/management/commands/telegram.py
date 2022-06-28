from django.core.management.base import BaseCommand
from django.conf import settings
from telebot import TeleBot
from telebot import types
from ...utils import telegram_user
from ...models import Telegram
from ...interface import *


bot = TeleBot(settings.TELEGRAM_BOT_TOKEN, threaded=False)


@bot.message_handler(commands=[Start.name])
@telegram_user
def start(message: types.Message, user: Telegram):
    bot.send_photo(
        message.chat.id,
        photo='https://avatars.githubusercontent.com/u/16373529?v=4',
        caption=Start.message,
        parse_mode='html'
    )


def notificate_all_users_about_event(event: Event, bot: TeleBot):
    for users in Telegram.objects.all():
        bot.send_photo(
            chat_id=users.id,
            photo=event.photo,
            caption=Event.message.format(event.name, event.date)
        )


class Command(BaseCommand):
    help = 'Telegram bot setup command'

    def handle(self, *args, **kwargs):
        bot.enable_save_next_step_handlers(delay=2)
        bot.load_next_step_handlers()
        bot.infinity_polling()
