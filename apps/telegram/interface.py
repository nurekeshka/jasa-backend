from apps.events.models import Event, Organization, Tag
from .constants import MONTHES
from .constants import Emoji
from telebot import types


class Start(object):
    name = 'start'
    message = 'Добро пожаловать!'
    photo = 'https://avatars.githubusercontent.com/u/16373529?v=4'


class Organizations(object):
    callback_data = 'organization:{}'

    def message(organization: Organization) -> str:
        text = organization.name
        text += organization.description
        return text
    
    def markup(organization: Organization, event_id: int or str) -> types.InlineKeyboardMarkup:
        inline = types.InlineKeyboardMarkup()

        inline.add(types.InlineKeyboardButton(
            text=Back.text,
            callback_data=Events.callback_data.format(event_id)
        ))

        return inline


class Events(object):
    callback_data = 'event:{}'

    def message(event: Event) -> str:
        text = [
                f'{Emoji.exclamation_mark_double.value} {event.name} {Emoji.exclamation_mark_double.value}\n\n',
                f'{Emoji.marker.value} Адрес: {event.address}\n',
                f'{Emoji.calendar.value} Начало:\t{event.start.date().day} {MONTHES[event.start.date().month]} в {event.start.time().strftime("%H:%M")}\n',
                f'{Emoji.clock.value} Конец:\t{event.end.date().day} {MONTHES[event.end.date().month]} в {event.end.time().strftime("%H:%M")}\n\n',
                f'{Emoji.paper_with_pencil.value} {event.description}\n\n'
            ]

        for tag in event.tags.all():
            text.append(f'#{tag} ')

        return ''.join(text)
    
    def markup(event: Event) -> types.InlineKeyboardMarkup:
        inline = types.InlineKeyboardMarkup()

        organization_btn = types.InlineKeyboardButton(
            text='Об организаторе',
            callback_data=Organizations.callback_data.format(event.organization.id) + ';' + Events.callback_data.format(event.id)
        )

        sign_up_btn = types.InlineKeyboardButton(
            text='Записаться',
            url=event.sign_up_url
        )

        inline.add(
            organization_btn, sign_up_btn
        )

        return inline


class Back(object):
    text = '« Вернуться назад'


class Search(object):
    def message():
        text = [
            'Отправьте мне сообщение с одним из предложенных тэгов:\n',
        ]

        tags = [f'#{x.name}' for x in Tag.objects.all()]

        text.extend(tags)
        return ' '.join(text)

    def markup(tag: Tag):
        events = tag.event_set.all()

        if events is None:
            return

        inline = types.InlineKeyboardMarkup()

        for event in events:
            inline.add(
                types.InlineKeyboardButton(
                    text=event.name,
                    callback_data=Events.callback_data.format(event.id)
                )
            )
        
        return inline
