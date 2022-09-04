from django.contrib import admin
from django.db import models
from ckeditor.widgets import CKEditorWidget


from .models import Event, Like, Bookmark, Tag

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title', 
        'pub_date', 
        'short_description',
        'long_description',
        'start_date', 'end_date'
    )
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }


admin.site.register(Like)
admin.site.register(Bookmark)
admin.site.register(Tag)