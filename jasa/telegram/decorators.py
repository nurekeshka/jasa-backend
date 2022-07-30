from .models import TelegramUser
from telebot import types


def get_telegram_user(setup_function):
    """
    Decorator function that gets existing `TelegramUser` model 
    from current request. If it doesn't exists, create a new model.
    """
    def inner(function):
        def wrapper(message: types.Message):
            user, created = TelegramUser.objects.get_or_create(
                id=message.from_user.id,
                defaults={
                    'username': message.from_user.username,
                    'first_name': message.from_user.first_name,
                    'last_name': message.from_user.last_name
                }
            )
            if created:
                return setup_function(message, user)
            return function(message, user)
        return wrapper
    return inner
