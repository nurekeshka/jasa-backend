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
        cls.user = User.objects.create_user(username='test_user')
        cls.tg_user_id = 1234567
        cls.tg_user = TelegramUser.objects.create(
            user=cls.user,
            id=cls.tg_user_id,
        )
    
    def setUp(self) -> None:
        self.urls_template_names = {
            f'/auth/signup/{self.tg_user_id}/': 'users/signup.html',
            f'/auth/login/{self.tg_user_id}/': 'users/login.html',
            f'/auth/logout/{self.tg_user_id}/': 'users/logout.html',
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
