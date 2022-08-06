from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Event(models.Model):
    """Event model that saves necessary information about the event."""

    title = models.CharField('Event title', max_length=255)
    description = models.TextField('Event description')
    sign_up_url = models.URLField('Sign up URL')
    # TODO: Change the photo field to be a ImageField instead.
    photo = models.URLField('Event photo URL')
    liked = models.ManyToManyField(
        User, 
        related_name='liked_events',
        default=None,
        blank = True,
        verbose_name="likes"
    )
    bookmarked = models.ManyToManyField(
        User,
        related_name='bookmarked_events',
        default=None,
        blank = True,
        verbose_name="bookmarks"
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
        return self.liked.count()
    
    @property
    def num_bookmarks(self):
        return self.bookmarked.count()


LIKE_CHOICES = (
    ('like', 'like'),
    ('dislike', 'dislike'),
)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='like', max_length=10)


class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
