from http import HTTPStatus

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model


User = get_user_model()

class CreationFormTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
    
    def setUp(self):
        self.guest_client = Client()

    def test_signup(self):
        """
        Checks whether the user registration form is valid.
        """
        users_count = User.objects.count()
        form_data = {
            'first_name': 'test_first_name',
            'last_name': 'test_last_name',
            'username': 'test_user',
            'email': 'mail@gmail.com',
            'password1': 'mM6m-tG177-1',
            'password2': 'mM6m-tG177-1',
        }
        response = self.guest_client.post(
            reverse('users:signup'),
            data=form_data,
            follow=True
        )

        self.assertEqual(User.objects.count(), users_count + 1)
        self.assertTrue(
            User.objects.filter(username='test_user').exists()
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)


class UserLoginFormTest(TestCase):
    
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.user = User.objects.create_user(
            username='test_user',
            password='test_password_hard_to_guess',
        )
    
    def setUp(self):
        self.auth_client = Client()
    
    def test_login(self):
        """
        Checks whether the user login form is valid.
        """
        form_data = {
            'username': 'test_user',
            'password': 'test_password_hard_to_guess',
        }
        response = self.auth_client.post(
            reverse('users:login'),
            data=form_data,
            follow=True
        )

        self.assertRedirects(response, reverse('events:index'))
        self.assertEqual(response.status_code, HTTPStatus.OK)
