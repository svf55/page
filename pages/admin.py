from django.contrib import admin

from content.models import Audio, Text, Video
from pages.models import Page


class TextInline(admin.TabularInline):
    model = Text
    extra = 0


class AudioInline(admin.TabularInline):
    model = Audio
    extra = 0


class VideoInline(admin.TabularInline):
    model = Video
    extra = 0


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    inlines = [
        TextInline,
        VideoInline,
        AudioInline
    ]
    list_display = ['id', 'title']
    search_fields = ('^title',)

