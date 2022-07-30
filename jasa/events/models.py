from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Event(models.Model):
    # TODO: Add docstring to the class.
    """"""

    title = models.CharField('Event title', max_length=255)
    description = models.TextField('Event description')
    sign_up_url = models.URLField('Sign up URL')
    photo = models.URLField('Event photo URL')

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
