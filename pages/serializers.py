from rest_framework import serializers
from content.models import Content, Text, Audio, Video
from content.serializer import TextSerializer, AudioSerializer, VideoSerializer, DefaultContentSerializer
from pages.models import Page


class ContentSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        if isinstance(instance, Text):
            return TextSerializer(instance=instance).data
        elif isinstance(instance, Audio):
            return AudioSerializer(instance=instance).data
        elif isinstance(instance, Video):
            return VideoSerializer(instance=instance).data
        else:
            return DefaultContentSerializer(instance=instance).data

    class Meta:
        model = Content
        fields = '__all__'


class PageSerializer(serializers.ModelSerializer):

    contents = serializers.SerializerMethodField()

    @staticmethod
    def get_contents(obj):
        objects = Content.objects.filter(page=obj).order_by('id').select_subclasses()
        objects_serialize = ContentSerializer(objects, many=True).data

        for i, obj_srlz in enumerate(objects_serialize):
            class_name_obj = type(objects[i]).__name__

            if class_name_obj == 'Text':
                type_content = 1
            elif class_name_obj == 'Video':
                type_content = 2
            elif class_name_obj == 'Audio':
                type_content = 3
            else:
                type_content = 0

            obj_srlz.update({'type_content': type_content})

        objects_serialize.sort(key=lambda k: (k['type_content'], -k['weight']))

        for element in objects_serialize:
            del element['type_content']

        return objects_serialize

    class Meta:
        model = Page
        fields = ('id', 'title', 'contents')


class PagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Page
        fields = ('id', 'title', 'url',)

