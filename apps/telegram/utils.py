from .models import Telegram
from telebot import types


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
