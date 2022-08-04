import requests

from telebot import TeleBot, types

from jasa.settings import BOT_TOKEN, DOMAIN
from .decorators import get_telegram_user
from .context import context


bot = TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['intro'])
def introduction(message, user):
    """
    Sends an introduction message that guides users on how
    to use the app.
    """
    bot.send_message(
        user.id,
        context['introduction']['text'],
        parse_mode='markdown'
    )


@bot.message_handler(commands=['start'])
@get_telegram_user(introduction)
def start(message, user):
    """Send a welcome back text message."""
    keyboard = context['start']['keyboard'].create()
    bot.send_message(
        user.id,
        context['start']['text'].format(
            user=user.first_name
        ),
        reply_markup=keyboard,
    )


@bot.message_handler(commands=['help'])
@get_telegram_user(introduction)
def help(message, user):
    """Send a message listing all available commands."""
    bot.send_message(
        user.id,
        context['help']['text'],
        parse_mode='markdown'
    )


@bot.message_handler(commands=['signup'])
@get_telegram_user(introduction)
def signup(message, user):
    """Send a sign up message."""
    keyboard = context['signup']['keyboard'].create({ 'id': user.id })
    bot.send_message(
        user.id,
        context['signup']['text'],
        reply_markup=keyboard,
    )


@bot.message_handler(commands=['login'])
@get_telegram_user(introduction)
def login(message, user):
    """Log in to your account."""
    keyboard = context['login']['keyboard'].create({ 'id': user.id})
    bot.send_message(
        user.id,
        context['login']['text'],
        reply_markup=keyboard,
    )


@bot.message_handler(commands=['logout'])
@get_telegram_user(introduction)
def logout(message, user):
    """Log out of your account."""
    keyboard = context['logout']['keyboard'].create()
    bot.send_message(
        user.id,
        context['logout']['text'],
        reply_markup=keyboard,
        parse_mode='markdown',
    )
