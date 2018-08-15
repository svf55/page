# Generated by Django 2.0.5 on 2018-08-14 17:04

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='Заголовок')),
                ('counter', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Счетчик просмотров')),
                ('weight', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('content_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='content.Content')),
                ('url', models.URLField(verbose_name='Ссылка на файл')),
            ],
            options={
                'verbose_name': 'Аудио-файл',
                'verbose_name_plural': 'Аудио-файлы',
            },
            bases=('content.content',),
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('content_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='content.Content')),
                ('content', models.TextField(default='', verbose_name='Контент текста')),
            ],
            options={
                'verbose_name': 'Текст',
                'verbose_name_plural': 'Тексты',
            },
            bases=('content.content',),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('content_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='content.Content')),
                ('url', models.URLField(verbose_name='Ссылка на файл')),
            ],
            options={
                'verbose_name': 'Видео-файл',
                'verbose_name_plural': 'Видео-файлы',
            },
            bases=('content.content',),
        ),
        migrations.AddField(
            model_name='content',
            name='page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='pages.Page'),
        ),
    ]
