from django.urls import path

from . import views


app_name = 'events'

urlpatterns = [
    path('events/', views.index , name='index'),
    path('events/<int:event_id>/', views.event_details, name='event_details'),
    path('events/like/', views.like_event, name='like_event'),
    path('events/bookmark/', views.bookmark_event, name='bookmark_event'),
]
