from dataclasses import dataclass

from telebot import TeleBot
from telebot.handler_backends import BaseMiddleware, SkipHandler
from django.contrib.auth.models import AnonymousUser

from jasa.settings import BOT_TOKEN, DEBUG
from .context import context
from .models import TelegramUser


bot = TeleBot(BOT_TOKEN, use_class_middlewares=True)
if DEBUG:
    import logging
    from telebot import logger
    logger.setLevel(logging.DEBUG)

@dataclass
class Middleware(BaseMiddleware):
    update_types = ['message']

    def pre_process(self, message, data):
        """
        Function that gets existing `TelegramUser` model 
        from current request. If it doesn't exists, create a new model.
        """
        data['tg-user'], created = TelegramUser.objects.get_or_create(
            id=message.from_user.id,
            defaults={
                'username': message.from_user.username,
                'first_name': message.from_user.first_name,
                'last_name': message.from_user.last_name,
            }
        )
        if created:
            intro(message, data)
            return SkipHandler()
    
    def post_process(self, message, data, exception):
        pass


@bot.message_handler(commands=['intro'])
def intro(message, data):
    """Send an introduction message that guides users on how to use the app."""
    bot.send_message(
        data['tg-user'].id,
        context['intro']['text'],
        parse_mode='markdown'
    )


@bot.message_handler(commands=['start'])
def start(message, data):
    """Send a welcome back text message."""
    user = data['tg-user'].user or AnonymousUser
    keyboard = context['start']['keyboard'].create(
        {'username': user.username}
    )
    bot.send_message(
        data['tg-user'].id,
        context['start']['text'].format(
            user=data['tg-user'].first_name
        ),
        reply_markup=keyboard,
    )



@bot.message_handler(commands=['help'])
def help(message, data):
    """Send a message listing all available commands."""
    bot.send_message(
        data['tg-user'].id,
        context['help']['text'],
        parse_mode='markdown'
    )


@bot.message_handler(commands=['signup'])
def signup(message, data):
    """Send a sign up message."""
    keyboard = context['signup']['keyboard'].create(
        {'id': data['tg-user'].id}
    )
    bot.send_message(
        data['tg-user'].id,
        context['signup']['text'],
        reply_markup=keyboard,
    )


@bot.message_handler(commands=['login'])
def login(message, data):
    """Log in to your account."""
    keyboard = context['login']['keyboard'].create(
        {'id': data['tg-user'].id}
    )
    bot.send_message(
        data['tg-user'].id,
        context['login']['text'],
        reply_markup=keyboard,
    )


@bot.message_handler(commands=['logout'])
def logout(message, data):
    """Log out of your account."""
    keyboard = context['logout']['keyboard'].create(
        {'id': data['tg-user'].id}
    )
    bot.send_message(
        data['tg-user'].id,
        context['logout']['text'],
        reply_markup=keyboard,
        parse_mode='markdown',
    )

@bot.message_handler(commands=['about'])
def about(message, data):
    """Send an about message."""
    bot.send_message(
        data['tg-user'].id,
        context['about']['text'],
        parse_mode='html',
    )


@bot.message_handler(commands=['explore'])
def explore(message, data):
    """Send an explore message that redirects users to event:index page."""
    keyboard = context['explore']['keyboard'].create()
    bot.send_message(
        data['tg-user'].id,
        context['explore']['text'],
        reply_markup=keyboard,
    )


@bot.message_handler(commands=['profile'])
def profile(message, data):
    """
    Send an profile message that redirects users to their profile. If
    they are logged in.
    """
    user = data['tg-user'].user or AnonymousUser
    if not user:
        # If user is not logged into an account then redirect to login message.
        bot.send_message(
            data['tg-user'].id,
            context['profile']['warning_text']
        )
        login(message, data)
        return

    keyboard = context['profile']['keyboard'].create(
        {'username': user.username}
    )
    bot.send_message(
        data['tg-user'].id,
        context['profile']['text'],
        reply_markup=keyboard
    )

bot.setup_middleware(Middleware())