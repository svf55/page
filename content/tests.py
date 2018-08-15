from rest_framework.test import APITestCase
from content.models import Audio, Text


class TestContent(APITestCase):
    fixtures = ['initial_content_data.json']

    def test_increment_counter(self):
        """
        Ensure that the view count is increased by 1.
        """
        response = self.client.get('/api/v1/pages/3/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Text.objects.get(id=11).counter, 1)
        self.assertEqual(Audio.objects.get(id=4).counter, 1)

