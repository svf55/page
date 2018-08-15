from rest_framework import status
from rest_framework.test import APITestCase
from pages.models import Page


class TestPage(APITestCase):

    fixtures = ['initial_pages_data.json']

    def test_create_page(self):
        """
        Ensure we can create a new Page object.
        """
        count_before = Page.objects.count()
        data = {
            'title': 'page'
        }
        response = self.client.post('/api/v1/pages/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Page.objects.count(), count_before + 1)

    def test_update_page(self):
        """
        Ensure we can update a new Page object.
        """
        data = {
            'id': 3,
            'title': 'page'
        }
        response = self.client.patch('/api/v1/pages/3/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

