from http import HTTPStatus

from django.test import TestCase, Client
from django.contrib.auth import get_user_model

from events.models import Event


User = get_user_model()


class EventsURLTests(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()

        cls.guest_client = Client()
        cls.auth_client = Client()
        
        cls.user = User.objects.create(username='Authorized-user')
        cls.organizer = User.objects.create(username='Organizer')

        cls.auth_client.force_login(cls.user)

    def setUp(self) -> None:
        self.event = Event.objects.create(
            organizer=self.organizer,
            title='Event title',
            description='Event description',
            sign_up_url='https://google.com',
            photo='https://picsum.photos/200/300',
        )
        self.urls_template_names = {
            '/events/': 'events/index.html',
            f'/events/{self.event.id}/': 'events/event_details.html',
            f'/profile/{self.user.username}/': 'events/profile.html',
        }

    def test_urls_exists_at_desired_location(self):
        """
        Checks if the URL exists in the right place and is available
        whether for an anonymous user.
        """
        for url in self.urls_template_names.keys():
            with self.subTest(url=url):
                response = self.guest_client.get(url)
                self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_unexisting_page(self):
        """Checks whether a non-existent page returns 404."""
        response = self.auth_client.get('/unexisting_page/')
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

    def test_urls_use_correct_templates(self):
        """
        Checks whether the correct templates for the pages are being used.
        """
        for url, template_name in self.urls_template_names.items():
            with self.subTest(url=url, template_name=template_name):
                response = self.guest_client.get(url)
                self.assertTemplateUsed(response, template_name)
