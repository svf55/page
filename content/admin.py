from django.contrib import admin

from content.models import Text, Audio, Video


@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    list_display = ['id', 'weight', 'title', 'page', 'content']
    search_fields = ('title',)
    ordering = ('-weight', 'id')


@admin.register(Audio)
class AudioAdmin(admin.ModelAdmin):
    list_display = ['id', 'weight', 'title', 'page', 'url']
    search_fields = ['title']
    ordering = ('-weight', 'id')


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['id', 'weight', 'title', 'page', 'url']
    search_fields = ['title']
    ordering = ('-weight', 'id')

