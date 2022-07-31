from django.shortcuts import render, redirect

from telegram.models import TelegramUser
from .constants import NUM_LOAD_EVENTS
from .models import Event

def index(request, user_id: int):
    """Render 10 most recent events."""
    template_name = 'events/index.html'
    event_list = Event.objects.all()[:NUM_LOAD_EVENTS]
    user = TelegramUser.objects.get(id=user_id)

    context = {
        'events': event_list,
        'user': user,
    }

    return render(request, template_name, context)


def event_details(request, user_id: int, event_id: int):
    """Render event details."""
    template_name = 'events/event_details.html'
    event = Event.objects.get(id=event_id)
    user = TelegramUser.objects.get(id=user_id)

    context = {
        'event': event,
        'user': user,
    }

    return render(request, template_name, context)


def like_post(request, user_id: int):
    user = TelegramUser.objects.get(id=user_id)

    if request.method == 'POST':
        event_id = request.POST.get('event_id')
        event = Event.objects.get(id=event_id)
        
        if user in event.liked.all():
            event.liked.remove(user)
        else:
            event.liked.add(user)

    return redirect('events:index', user_id=user_id)