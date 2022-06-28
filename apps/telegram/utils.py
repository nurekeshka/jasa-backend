from apps.events.models import Event
from .constants import event_text_description
from .models import Telegram
from telebot import TeleBot
from telebot import types


def notificate_all_users_about_event(event: Event, bot: TeleBot) -> bool:
    for users in Telegram.objects.all():
        bot.send_photo(
            chat_id=users.id,
            photo=event.photo,
            caption=event_text_description.format(event.name, event.date)
        )
