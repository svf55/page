from django.contrib import admin
from pages.models import Page

@admin.register(Page)
class TextAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

