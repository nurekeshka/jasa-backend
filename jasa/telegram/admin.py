from django.contrib import admin
from typing import Sequence

from .models import TelegramUser

@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    """Displays necessary information about a telegram user"""

    list_display: Sequence[str] = (
        'id',
        'username',
        'first_name',
        'last_name',
    )
    readonly_fields: Sequence[str] = ('id',)
    search_fields: Sequence[str] = ('username',)
    empty_value_display: str = '-пусто-'