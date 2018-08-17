import factory

from content.models import Content, Text, Audio, Video
from pages.models import Page


class PageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Page
        django_get_or_create = ('title',)

    title = 'page'


class TextFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Text

    title = 'text'
    page = factory.SubFactory(PageFactory)
    counter = 0
    weight = 0


class AudioFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Audio

    title = 'audio'
    page = factory.SubFactory(PageFactory)
    counter = 0
    weight = 0


class VideoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Video

    title = 'video'
    page = factory.SubFactory(PageFactory)
    counter = 0
    weight = 0

