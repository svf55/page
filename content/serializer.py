from rest_framework import serializers
from content.models import Audio, Text, Video, Content


class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = ('id', 'title', 'counter', 'url', 'weight')


class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = ('id', 'title', 'counter', 'content', 'weight')


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'title', 'counter', 'url', 'weight')


class DefaultContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'

