from rest_framework import serializers
from pages.models import Page


class PageSerializer(serializers.ModelSerializer):
    contents = serializers.StringRelatedField(many=True)

    class Meta:
        model = Page
        fields = ('id', 'title', 'contents')


class PagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Page
        fields = ('id', 'title', 'url',)

