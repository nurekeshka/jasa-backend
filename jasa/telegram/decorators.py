from .models import TelegramUser
from telebot import types


def get_telegram_user(function):
    """
    Decorator function that gets existing `TelegramUser` model 
    from current request. If doesn't exists create a new model.
    """
    def wrapper(message: types.Message):
        user, _created = TelegramUser.objects.get_or_create(
            id=message.from_user.id,
            defaults={
                'username': message.from_user.username,
                'first_name': message.from_user.first_name,
                'last_name': message.from_user.last_name
            }
        )

        return function(message, user)
    return wrapper