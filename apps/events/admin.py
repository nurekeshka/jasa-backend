from django.contrib import admin
from .models import *


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'type')
    fields = ('name', 'description', 'type')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('type', 'value', 'organization')
    fields = ('type', 'value', 'organization')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    fields = ('name',)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'organization', 'date', 'start', 'end')
    fields = ('name', 'organization', 'date', 'start', 'end', 'tags', 'longitude', 'latitude')
