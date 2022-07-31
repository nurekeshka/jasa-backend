from telebot import TeleBot, types

from jasa.settings import BOT_TOKEN
from .decorators import get_telegram_user
from .utils import create_reply_keyboard
from .context import context


bot = TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['intro'])
def introduction(message, user = None):
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
    keyboard = create_reply_keyboard(
        context['start']['buttons'],
        placeholder_values={'user_id': {'web_app': user.id}}
    )
    print(keyboard)
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
