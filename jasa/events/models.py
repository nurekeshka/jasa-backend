from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Event(models.Model):
    """Event model that saves necessary information about the event."""

    organizer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='events',
        verbose_name='Event organizer',
    )
    title = models.CharField(
        'Event title',
        max_length=255
    )
    short_description = models.CharField(
        'Event short description',
        max_length=255,
        blank=True
    )
    long_description = models.TextField(
        'Event detailed description',
        blank=True
    )
    sign_up_url = models.URLField(
        'Sign up URL'
    )
    photo = models.ImageField(
        'Event photo',
        upload_to='events/',
        blank=True,
    )
    liked = models.ManyToManyField(
        User, 
        related_name='liked_events',
        default=None,
        blank=True,
        verbose_name="likes"
    )
    bookmarked = models.ManyToManyField(
        User,
        related_name='bookmarked_events',
        default=None,
        blank=True,
        verbose_name="bookmarks"
    )

    pub_date = models.DateTimeField(
        'Event publish date',
        auto_now_add=True,
    )

    start_date = models.DateTimeField(
        'Event start date',
        auto_now_add=True,
    )
    end_date = models.DateTimeField(
        'Event end date',
        auto_now_add=True,
    )

    address = models.CharField(
        'Address',
        max_length=255,
        blank=True,
    )
    longitude = models.FloatField(
        'Longitude',
        null=True,
        blank=True,
    )
    latitude = models.FloatField(
        'Latitude',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
        ordering = ['-pub_date']

    @property
    def num_likes(self):
        return self.liked.count()
    
    @property
    def num_bookmarks(self):
        return self.bookmarked.count()


LIKE_CHOICES = (
    ('like', 'like'),
    ('dislike', 'dislike'),
)


class Like(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
    )
    value = models.CharField(
        choices=LIKE_CHOICES,
        default='like',
        max_length=10,
    )


class Bookmark(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
    )

