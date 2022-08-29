from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

from ..models import Event
from telegram.models import TelegramUser

User = get_user_model()


class EventsFormsTest(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        """Creates a user and a client for the tests."""
        super().setUpClass()

        cls.guest_client = Client()
        cls.auth_client = Client()

        cls.user = User.objects.create(username='Authorized-user')
        cls.organizer = User.objects.create(username='Organizer')

        cls.auth_client.force_login(cls.user)

    def setUp(self):
        """Creates an event for the tests."""
        self.event = Event.objects.create(
            organizer=self.organizer,
            title='Event title',
            sign_up_url='https://google.com',
        )

    def test_event_like_is_valid(self):
        form_data = {
            'event-id': self.event.id
        }
        old_num_likes = self.event.num_likes
        auth_response = self.auth_client.post(
            reverse('events:like_event'),
            form_data
        )
        
        self.assertEqual(self.event.num_likes, old_num_likes + 1)

    def test_event_bookmark_is_valid(self):
        form_data = {
            'event-id': self.event.id
        }
        old_num_bookmarks = self.event.num_bookmarks
        auth_response = self.auth_client.post(
            reverse('events:bookmark_event'),
            form_data
        )
        
        self.assertEqual(self.event.num_bookmarks, old_num_bookmarks + 1)
