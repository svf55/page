from django.db import models
from django.core.validators import MinValueValidator


class Content(models.Model):
    title = models.TextField('Заголовок')
    page = models.ForeignKey('pages.Page', related_name='contents', on_delete=models.CASCADE,)
    counter = models.IntegerField('Счетчик просмотров', default=0, validators=[MinValueValidator(0)])
    weight = models.IntegerField(default=0)

    def __str__(self):
        return '{}'.format(self.title)


class Text(Content):
    content = models.TextField('Контент текста', default='')

    class Meta:
        verbose_name = 'Текст'
        verbose_name_plural = 'Тексты'


class Video(Content):
    url = models.URLField('Ссылка на файл')

    class Meta:
        verbose_name = 'Видео-файл'
        verbose_name_plural = 'Видео-файлы'


class Audio(Content):
    url = models.URLField('Ссылка на файл')

    class Meta:
        verbose_name = 'Аудио-файл'
        verbose_name_plural = 'Аудио-файлы'

