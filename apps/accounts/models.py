from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from datetime import date


class User(AbstractUser):
    is_school = models.BooleanField(default=False, verbose_name='is_school')
    birth_date = models.DateField(null=True, blank=True, verbose_name='birth date')

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        ordering = ('username',)
        
    def __str__(self):
        return self.get_full_name()
    
    def age(self):
        today = date.today()
        age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return age

@receiver(post_save, sender=User)
def create_user_token(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_token(sender, instance, **kwargs):
    Token.objects.get(user=instance).save()
