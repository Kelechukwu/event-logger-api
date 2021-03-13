from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from api.models import Event


class EventViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.dummy_event = Event.objects.create(email='test@test.com',
                                                environment='production', component='orders',
                                                message='stuff', data={'key1': 'someValue'})

    def test_can_create_an_event(self):
        response = self.client.post(
            '/event', {"email": "diego@chefhero.com",
                       "environment": "staging",
                       "component": "orders",
                       "message": "the buyer #123456 has placed an order successfully",
                       "data": {"key": "value"}}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_can_get_events(self):
        response = self.client.get('/event')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)
