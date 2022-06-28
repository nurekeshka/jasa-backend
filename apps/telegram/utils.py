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


def telegram_user(function):
    def inner(message: types.Message):
        user, created = Telegram.objects.get_or_create(
            id=message.from_user.id,
            defaults={
                'username': message.from_user.username,
                'first_name': message.from_user.first_name,
                'last_name': message.from_user.last_name
            }
        )

        function(message, user)
    return inner
