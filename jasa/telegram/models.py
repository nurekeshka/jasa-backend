from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser

User = get_user_model()


class TelegramUser(models.Model):
    """
    Saves current users who have used the bot.
    TelegramUser constists of `id`, `username`, `first_name` and `last_name`
    """

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='user',
        verbose_name='User account',
        blank=True,
        null=True
    )
    id = models.IntegerField(
        'User id',
        primary_key=True,
        unique=True,
        blank=False,
        null=False,
    )
    username = models.CharField(
        'Username',
        max_length=255,
        blank=True,
        null=True,
    )
    first_name = models.CharField(
        'First name',
        max_length=255,
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        'Last name',
        max_length=255,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Telegram user'
        verbose_name_plural = 'Telegram users'

    def __str__(self):
        return str(self.id)
