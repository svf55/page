from django.db import models


class Page(models.Model):
    title = models.TextField('Заголовок')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'

