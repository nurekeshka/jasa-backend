from django.core.management.base import BaseCommand
from django.conf import settings
from apps.events.models import Event
from ...utils import telegram_user
from ...models import Telegram
from ...interface import *
from telebot import TeleBot
from telebot import types


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


@bot.callback_query_handler(func=lambda call: True)
@telegram_user
def callback_query_handler(call: types.CallbackQuery, user: Telegram):
    if call.data.startswith(Events.callback_data):
        id = int(call.data.split(':')[0])
        
        try:
            event = Event.objects.get(id=id)
        except Event.DoesNotExist:
            return
        
        bot.edit_message_media(
            chat_id=call.message.chat.id,
            media=types.InputMediaPhoto(
                media=event.photo,
                caption=Events.message(event),
                parse_mode='html'
            ),
            message_id=call.message.id,
            reply_markup=Events.markup(event)
        )


def notificate_all_users_about_event(event: Event):
    for user in Telegram.objects.all():
        bot.send_photo(
            chat_id=user.id,
            photo=event.photo,
            caption=Events.message(event),
            reply_markup=Events.markup(event),
            parse_mode='html'
        )


class Command(BaseCommand):
    help = 'Telegram bot setup command'

    def handle(self, *args, **kwargs):
        bot.enable_save_next_step_handlers(delay=2)
        bot.load_next_step_handlers()
        bot.infinity_polling()
