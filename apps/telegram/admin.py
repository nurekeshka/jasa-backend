from django.contrib import admin
from .models import Telegram


@admin.register(Telegram)
class TelegramAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name')
    fields = ('username', 'first_name', 'last_name')
