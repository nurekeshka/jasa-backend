from typing import List
from http import HTTPStatus

from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

from events.models import Event


User = get_user_model()


class EventsViewTests(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        """Creates a user and a client for the tests."""
        super().setUpClass()

        cls.guest_client = Client()
        cls.auth_client = Client()
        
        cls.user = User.objects.create(username='Authorized-user')
        cls.organizer = User.objects.create(username='Organizer')

        cls.auth_client.force_login(cls.user)

    def setUp(self) -> None:
        """Creates an event for the tests."""
        self.event = Event.objects.create(
            organizer=self.organizer,
            title='Event title',
            sign_up_url='https://google.com',
        )
        self.reverse_kwargs = {
            'events:index': {},
            'events:event_details': {'event_id': self.event.id},
            'events:profile': {'username': self.user.username}
        }


    def test_about_page_accessible_by_name(self):
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
        reverse_template_names = {
            'events:index': 'events/index.html',
            'events:event_details': 'events/event_details.html',
            'events:profile': 'events/profile.html'
        }
        for reverse_name, template in reverse_template_names.items():
            with self.subTest(reverse=reverse_name, template=template):
                response = self.guest_client.get(reverse(
                    reverse_name,
                    kwargs=self.reverse_kwargs[reverse_name]
                ))
                self.assertTemplateUsed(response, template)

    def test_index_show_correct_context(self):
        """
        Checks whether the correct context is being used for the index page.
        """
        response = self.guest_client.get(reverse(
            'events:index',
            kwargs=self.reverse_kwargs['events:index']
        ))
        events = response.context['page_obj']
        self.assertIsInstance(events[0], Event)

    def test_event_details_show_correct_context(self):
        """
        Checks whether the correct context is being used for the event
        details page.
        """
        response = self.guest_client.get(reverse(
            'events:event_details',
            kwargs=self.reverse_kwargs['events:event_details']
        ))
        event = response.context['event']
        self.assertIsInstance(event, Event)

    def test_pages_latest_event_displayed(self):
        """Checks whether the latest event is being displayed on the pages."""
        reverse_names = [
            'events:index',
            'events:profile'
        ]
        new_event = Event.objects.create(
            organizer=self.user,
            title='New event title',
            sign_up_url='https://google.com',
        )
        for reverse_name in reverse_names:
            with self.subTest(reverse=reverse_name):
                response = self.guest_client.get(reverse(
                    reverse_name,
                    kwargs=self.reverse_kwargs[reverse_name]
                ))
                latest_event = response.context['page_obj'][0]
                self.assertEqual(latest_event, new_event)

    def test_pages_paginator_infinte_scroll(self):
        """
        Checks whether the paginator on pages works like an infinite scroll.
        """
        pass
