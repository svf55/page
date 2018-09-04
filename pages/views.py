from rest_framework import viewsets
from pages.serializers import PageSerializer, PagesSerializer
from pages.models import Page
from pages.tasks import increment_counter


class PageViewSet(viewsets.ModelViewSet):
    def retrieve(self, request, *args, **kwargs):
        pk = self.request.parser_context['kwargs']['pk']
        increment_counter.delay(pk)
        return super().retrieve(request, *args, **kwargs)

    queryset = Page.objects.all()
    serializer_class = PageSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return PagesSerializer
        if self.action == 'retrieve':
            return PageSerializer

        return PagesSerializer

