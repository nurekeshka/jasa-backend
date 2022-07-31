from django.db import models
from django.contrib.auth import get_user_model

from telegram.models import TelegramUser

User = get_user_model()

class Event(models.Model):
    # TODO: Add docstring to the class.
    """"""

    title = models.CharField('Event title', max_length=255)
    description = models.TextField('Event description')
    sign_up_url = models.URLField('Sign up URL')
    photo = models.URLField('Event photo URL')
    liked = models.ManyToManyField(
        TelegramUser, 
        related_name='liked_events',
        default=None,
        blank = True,
        verbose_name="likes"
    )

    pub_date = models.DateTimeField('Event publish date', auto_now_add=True)

    start_date = models.DateTimeField('Event start date')
    end_date = models.DateTimeField('Event end date')

    address = models.CharField('Address', max_length=255)
    longitude = models.FloatField('Longitude')
    latitude = models.FloatField('Latitude')

    organizer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='events',
        verbose_name='Event organizer',
    )

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
        ordering = ['-pub_date']

    @property
    def num_likes(self):
        return self.liked.all().count()


LIKE_CHOICES = (
    ('like', 'like'),
    ('dislike', 'dislike'),
)

class Like(models.Model):
    user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='like', max_length=10)

    def __str__(self):
        return str(self.post)
