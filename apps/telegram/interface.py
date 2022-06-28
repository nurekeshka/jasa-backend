from apps.events.models import Event
from .constants import MONTHES
from .constants import Emoji


class Start(object):
    name = 'start'
    message = 'Добро пожаловать!'


class Events(object):
    def message(event: Event):
        text = f'{Emoji.exclamation_mark_double.value} {event.name} {Emoji.exclamation_mark_double.value}\n\n'
        
        text += f'{Emoji.marker.value} Адрес: {event.address}\n'
        text += f'{Emoji.calendar.value} Начало:\t{event.start.date().day} {MONTHES[event.start.date().month]} в {event.start.time().strftime("%H:%M")}\n'
        text += f'{Emoji.clock.value} Конец:\t{event.end.date().day} {MONTHES[event.end.date().month]} в {event.end.time().strftime("%H:%M")}\n\n'
        
        text += f'{Emoji.paper_with_pencil.value} {event.description}\n\n'

        for tag in event.tags.all():
            text += f'#{tag} '

        return text
