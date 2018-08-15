from django.db import connection, transaction
from django.db.models import F
from rest_framework import viewsets

from content.models import Content
from pages.serializers import PageSerializer, PagesSerializer
from pages.models import Page


class PageViewSet(viewsets.ModelViewSet):
    def retrieve(self, request, *args, **kwargs):
        pk = self.request.parser_context['kwargs']['pk']

        with transaction.atomic():
            cursor = connection.cursor()
            cursor.execute('SET LOCAL synchronous_commit TO OFF')
            Content.objects.filter(page_id=pk).update(counter=F('counter') + 1)

        return super().retrieve(request, *args, **kwargs)

    queryset = Page.objects.all()
    serializer_class = PageSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return PagesSerializer
        if self.action == 'retrieve':
            return PageSerializer

        return PagesSerializer

