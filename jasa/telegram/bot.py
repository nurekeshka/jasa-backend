from dataclasses import dataclass
from telebot import TeleBot
from telebot.handler_backends import BaseMiddleware, SkipHandler

from jasa.settings import BOT_TOKEN
from .context import context
from .models import TelegramUser


bot = TeleBot(BOT_TOKEN, use_class_middlewares=True)


@dataclass
class Middleware(BaseMiddleware):
    update_types = ['message']

    def pre_process(self, message, data):
        """
        Function that gets existing `TelegramUser` model 
        from current request. If it doesn't exists, create a new model.
        """
        data['user'], created = TelegramUser.objects.get_or_create(
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



@bot.message_handler(commands=['intro'])
def intro(message, data):
    bot.send_message(
        data['user'].id,
        context['intro']['text'],
        parse_mode='markdown'
    )


@bot.message_handler(commands=['start'])
def start(message, data):
    """Send a welcome back text message."""
    keyboard = context['start']['keyboard'].create()
    bot.send_message(
        data['user'].id,
        context['start']['text'].format(
            user=data['user'].first_name
        ),
        reply_markup=keyboard,
    )


@bot.message_handler(commands=['help'])
def help(message, data):
    """Send a message listing all available commands."""
    bot.send_message(
        data['user'].id,
        context['help']['text'],
        parse_mode='markdown'
    )


@bot.message_handler(commands=['signup'])
def signup(message, data):
    """Send a sign up message."""
    keyboard = context['signup']['keyboard'].create({ 'id': data['user'].id })
    bot.send_message(
        data['user'].id,
        context['signup']['text'],
        reply_markup=keyboard,
    )


@bot.message_handler(commands=['login'])
def login(message, data):
    """Log in to your account."""
    keyboard = context['login']['keyboard'].create({ 'id': data['user'].id})
    bot.send_message(
        data['user'].id,
        context['login']['text'],
        reply_markup=keyboard,
    )


@bot.message_handler(commands=['logout'])
def logout(message, data):
    """Log out of your account."""
    keyboard = context['logout']['keyboard'].create({ 'id': data['user'].id})
    bot.send_message(
        data['user'].id,
        context['logout']['text'],
        reply_markup=keyboard,
        parse_mode='markdown',
    )

@bot.message_handler(commands=['about'])
def about(message, data):
    """Send an about message."""
    bot.send_message(
        data['user'].id,
        context['about']['text'],
        parse_mode='html',
    )


bot.setup_middleware(Middleware())