from django.core.management.base import BaseCommand
from django.conf import settings
from apps.events.models import Event, Tag
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
        photo=Start.photo,
        caption=Start.message,
        parse_mode='html'
    )


@bot.callback_query_handler(func=lambda call: True)
@telegram_user
def callback_query_handler(call: types.CallbackQuery, user: Telegram):
    if call.data.startswith(Events.callback_data.split(':')[0]):
        id = int(call.data.split(':')[1])
        
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
    elif call.data.startswith(Organizations.callback_data.split(':')[0]):
        id_org, id_eve = tuple(map(lambda x: int(x.split(':')[1]), call.data.split(';')))

        try:
            organization = Organization.objects.get(id=id_org)
        except Organization.DoesNotExist:
            return
        
        bot.edit_message_media(
            chat_id=call.message.chat.id,
            media=types.InputMediaPhoto(
                media=organization.photo,
                caption=Organizations.message(organization),
                parse_mode='html'
            ),
            message_id=call.message.id,
            reply_markup=Organizations.markup(organization, id_eve)
        )


def notificate_all_users_about_event(event: Event):
    for user in Telegram.objects.all():
        bot.send_photo(
            chat_id=user.id,
            photo=event.photo,
            caption=Events.message(event),
            reply_markup=Events.markup(event)
        )


@bot.message_handler(commands=['search'])
def search_by_tag(message: types.Message):
    message = bot.send_message(
        chat_id=message.chat.id,
        text=Search.message()
    )

    bot.register_next_step_handler(message, search)


def search(message: types.Message):
    try:
        tag = Tag.objects.get(name=message.text)
    except Tag.DoesNotExist:
        return bot.send_message(
            chat_id=message.chat.id,
            text='Этого тэга не существует'
        )

    if not tag.event_set.exists():
        return bot.send_message(
            chat_id=message.chat.id,
            text='Мероприятий по такому тэгу сейчас нет',
        )

    bot.send_photo(
        chat_id=message.chat.id,
        reply_markup=Search.markup(tag),
        photo=Start.photo,
    )


class Command(BaseCommand):
    help = 'Это команда запуска телеграм бота'

    def handle(self, *args, **kwargs):
        bot.enable_save_next_step_handlers(delay=2)
        bot.load_next_step_handlers()
        # bot.infinity_polling()
        bot.polling()
