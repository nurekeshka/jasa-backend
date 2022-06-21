from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_school = models.BooleanField(default=False, verbose_name='is_school')

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        ordering = ('username',)
