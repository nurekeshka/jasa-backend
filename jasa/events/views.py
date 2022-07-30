from django.shortcuts import render

from .constants import NUM_LOAD_EVENTS
from .models import Event

def index(request):
    """Render 10 most recent events."""
    template_name = 'events/index.html'
    event_list = Event.objects.all()[:NUM_LOAD_EVENTS]
    context = {
        'events': event_list,
    }

    return render(request, template_name, context)


def event_details(request, event_id: int):
    """Render event details."""
    template_name = 'events/event_details.html'
    event = Event.objects.get(id=event_id)
    context = {
        'event': event,
    }

    return render(request, template_name, context)