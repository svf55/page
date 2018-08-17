from rest_framework import status
from rest_framework.test import APITestCase
from pages.models import Page
from pages.tests_factories import PageFactory


class TestPage(APITestCase):

    def test_create_page(self):
        """
        Ensure we can create a new Page object.
        """
        count_before = Page.objects.all().count()
        data = {
            'title': 'page new id'
        }
        response = self.client.post('/api/v1/pages/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Page.objects.count(), count_before + 1)

    def test_update_page(self):
        """
        Ensure we can update a new Page object.
        """
        page = PageFactory.create(title='page old_title')

        data = {
            'id': page.id,
            'title': 'page new_title'
        }
        response = self.client.patch('/api/v1/pages/{}/'.format(page.id), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

