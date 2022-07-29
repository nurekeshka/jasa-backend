from django.db import models

# Create your models here.
class TelegramUser(models.Model):
    """
    Saves current users who have used the bot.
    TelegramUser constists of `id`, `username`, `first_name` and `last_name`
    """

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
        verbose_name_plural= 'Telegram users'

    def __str__(self):
        return (
            f'id: {self.id}\n'
            f'username: {self.username}\n'
            f'full name: {self.first_name} {self.last_name}\n'
        )
