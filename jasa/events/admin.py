from django.contrib import admin

from .models import Event, Like, Bookmark

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title', 
        'pub_date', 
        'description', 
        'start_date', 'end_date'
    )

admin.site.register(Like)
admin.site.register(Bookmark)