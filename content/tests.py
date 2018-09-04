from rest_framework.test import APITestCase
from content.models import Audio, Text, Video
from page import celery
from pages.tests_factories import PageFactory, AudioFactory, TextFactory, VideoFactory


class TestContent(APITestCase):

    def test_increment_counter(self):
        """
        Ensure that the view count is increased by 1.
        """
        celery.conf.task_always_eager = True

        page = PageFactory.create(title='page with text, audio')
        text = TextFactory.create(page=page)
        text_counter = text.counter
        video = VideoFactory.create(page=page)
        video_counter = video.counter
        audio = AudioFactory.create(page=page)
        audio_counter = audio.counter

        response = self.client.get('/api/v1/pages/{}/'.format(page.id))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Text.objects.get(page=page).counter, text_counter + 1)
        self.assertEqual(Video.objects.get(page=page).counter, video_counter + 1)
        self.assertEqual(Audio.objects.get(page=page).counter, audio_counter + 1)

