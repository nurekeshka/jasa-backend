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
        
        cls.tg_user_id = 1234567
        cls.tg_user = TelegramUser.objects.create(
            user=cls.user,
            id=cls.tg_user_id,
        )

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
        # FIXME Doesn't work as redirects to login with no argument
        guest_response = self.guest_client.post(
            reverse('events:like_event'),
            form_data,
            follow=True
        )
        auth_response = self.auth_client.post(
            reverse('events:like_event'),
            form_data,
            follow=True
        )
        
        # Guest user is redirected to login page.
        self.assertRedirects(guest_response, reverse('users:login', kwargs={
            'user_id': self.tg_user_id
        }))
        # Authorized user is redirected to events page.
        # New number of likes is equal to the old number of likes + 1.


    def test_event_bookmark_is_valid(self):
        pass
