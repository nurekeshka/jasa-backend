from http import HTTPStatus

from django.test import TestCase, Client
from django.contrib.auth import get_user_model

from telegram.models import TelegramUser

User = get_user_model()


class UsersViewsTest(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()

        cls.guest_client = Client()
    
    def setUp(self) -> None:
        self.urls_template_names = {
            f'/auth/signup/': 'users/signup.html',
            f'/auth/login/': 'users/login.html',
            f'/auth/logout/': 'users/logout.html',
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

    def test_urls_use_correct_templates(self):
        """
        Checks whether the correct templates for the pages are being used.
        """
        for url, template_name in self.urls_template_names.items():
            with self.subTest(url=url, template_name=template_name):
                response = self.guest_client.get(url)
                self.assertTemplateUsed(response, template_name)
