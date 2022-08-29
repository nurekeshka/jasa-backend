from http import HTTPStatus

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

from telegram.models import TelegramUser


User = get_user_model()


class UsersViewsTest(TestCase):
    
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.guest_client = Client()
        cls.user = User.objects.create_user(username='test_user')
        cls.tg_user_id = 1234567
        cls.tg_user = TelegramUser.objects.create(
            user=cls.user,
            id=cls.tg_user_id,
        )

    def setUp(self):
        self.reverse_kwargs = {
            'users:signup': {},
            'users:login': {},
            'users:logout': {},
        }
    
    def test_about_page_accessible_by_name(self):
        """Checks whether the about page is accessible by name."""
        for reverse_name, kwargs in self.reverse_kwargs.items():
            with self.subTest(reverse_name=reverse_name, kwargs=kwargs):
                response = self.guest_client.get(reverse(
                    reverse_name,
                    kwargs=kwargs
                ))
                self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_pages_use_correct_templates(self):
        """
        Checks whether the correct templates for the pages are being used.
        """
        template_names = {
            'users:signup': 'users/signup.html',
            'users:login': 'users/login.html',
            'users:logout': 'users/logout.html',
        }
        for reverse_name, kwargs in self.reverse_kwargs.items():
            with self.subTest(reverse_name=reverse_name, kwargs=kwargs):
                response = self.guest_client.get(reverse(
                    reverse_name,
                    kwargs=kwargs
                ))
                self.assertTemplateUsed(response, template_names[reverse_name])
