from apps.telegram.management.commands import telegram
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
    list_display = ('name', 'organization', 'start', 'end', 'address')
    fields = ('name', 'description', 'organization', 'address', ('start', 'end'), ('photo', 'tags'), ('longitude', 'latitude'))
    actions = ('notificate_all_users_about_event',)
    
    @admin.action(description='Notificate all users')
    def notificate_all_users_about_event(self, request, queryset):
        for event in queryset:
            telegram.notificate_all_users_about_event(event)
