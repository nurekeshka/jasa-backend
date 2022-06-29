from apps.events.models import Event
from .constants import MONTHES
from .constants import Emoji
from telebot import types


class Start(object):
    name = 'start'
    message = 'Добро пожаловать!'


class Organizations(object):
    callback_data = 'organization:{}'


class Events(object):
    callback_data = 'event:{}'

    def message(event: Event) -> str:
        text = f'{Emoji.exclamation_mark_double.value} {event.name} {Emoji.exclamation_mark_double.value}\n\n'

        text += f'{Emoji.marker.value} Адрес: {event.address}\n'
        text += f'{Emoji.calendar.value} Начало:\t{event.start.date().day} {MONTHES[event.start.date().month]} в {event.start.time().strftime("%H:%M")}\n'
        text += f'{Emoji.clock.value} Конец:\t{event.end.date().day} {MONTHES[event.end.date().month]} в {event.end.time().strftime("%H:%M")}\n\n'
        
        text += f'{Emoji.paper_with_pencil.value} {event.description}\n\n'

        for tag in event.tags.all():
            text += f'#{tag} '

        return text
    
    def markup(event: Event) -> types.InlineKeyboardMarkup:
        inline = types.InlineKeyboardMarkup()

        organization_btn = types.InlineKeyboardButton(
            text='Об организаторе',
            callback_data=Organizations.callback_data.format(event.organization.id)
        )

        sign_up_btn = types.InlineKeyboardButton(
            text='Записаться',
            callback_data=Events.callback_data.format(event.id)
        )

        inline.add(
            organization_btn, sign_up_btn
        )

        return inline
