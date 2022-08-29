from typing import Optional

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import get_user_model

from core.decorators.ajax_decorator import ajax_login_required
from .constants import NUM_LOAD_EVENTS
from .models import Event


User = get_user_model()


def paginator_events(request, event_list, num_of_events_per_page):
    """Paginator events."""
    page_number = request.GET.get('page')
    paginator = Paginator(event_list, num_of_events_per_page)

    return paginator.get_page(page_number)


def index(request):
    """Render NUM_LOAD_EVENTS most recent events."""
    template_name = 'events/index.html'
    event_list = Event.objects.all()
    page_obj = paginator_events(request, event_list, NUM_LOAD_EVENTS)

    context = {
        'page_obj': page_obj,
        'show_full': False,
    }
    
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


def profile(request, username: str):
    """Render profile page."""
    template_name = 'events/profile.html',

    username = username or request.user.username
    if not username:
        return redirect('users:login')

    user = get_object_or_404(User, username=username)
    event_list = user.events.all()
    page_obj = paginator_events(request, event_list, NUM_LOAD_EVENTS)

    context = {
        'profile': user,
        'page_obj': page_obj,
    }

    return render(request, template_name, context)


@ajax_login_required
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
            'status': 'OK',
            'count': event.num_likes,
            'event-id': event_id,
        })

    return JsonResponse({
        'status': 'ERROR',
        'redirect': '???'
    })


@ajax_login_required
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
            'status': 'OK',
            'count': event.num_bookmarks,
            'event-id': event_id,
        })

    return JsonResponse({
        'status': 'ERROR',
        'redirect': '???'
    })