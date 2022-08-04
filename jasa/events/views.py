from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .constants import NUM_LOAD_EVENTS
from .models import Event

def index(request):
    """Render 10 most recent events."""
    template_name = 'events/index.html'
    event_list = Event.objects.all()[:NUM_LOAD_EVENTS]

    context = {
        'events': event_list,
        'show_full': False,
    }

    print(request.user)
    
    return render(request, template_name, context)


def event_details(request, event_id: int):
    """Render event details."""
    template_name = 'events/event_details.html'
    event = Event.objects.get(id=event_id)

    context = {
        'event': event,
        'show_full': True,
    }

    return render(request, template_name, context)


@login_required
def like_event(request):
    user = request.user

    if request.method == 'POST':
        event_id = request.POST.get('event-id')
        event = Event.objects.get(id=event_id)
        
        if user in event.liked.all():
            event.liked.remove(user)
        else:
            event.liked.add(user)

        return JsonResponse({
            'state': 'liked' if user in event.liked.all() else 'unliked',
            'likeCount': event.liked.count(),
            'eventId': event_id,
        })
    
    return JsonResponse({'error': 'Error'})


@login_required
def bookmark_event(request):
    user = request.user

    if request.method == 'POST':
        event_id = request.POST.get('event-id')
        event = Event.objects.get(id=event_id)
        
        if user in event.bookmarked.all():
            event.bookmarked.remove(user)
        else:
            event.bookmarked.add(user)

        return JsonResponse({
            'state': 'bookmarked' if user in event.bookmarked.all() else 'unbookmarked',
            'bookmarkCount': event.bookmarked.count(),
            'eventId': event_id,
        })
    
    return JsonResponse({'error': 'Error'})