# encoding: utf8

from django.db import migrations


def load_data(apps, schema_editor):
    audio = apps.get_model("content", "Audio")
    audio(title='audio 1', page_id=1, weight=50, url='https://s3.eu-central-1.amazonaws.com/audio1.mp3',).save()
    audio(title='audio 2', page_id=1, weight=500, url='https://s3.eu-central-1.amazonaws.com/audio2.mp3',).save()
    audio(title='audio 3', page_id=2, url='https://s3.eu-central-1.amazonaws.com/audio3.mp3',).save()
    audio(title='audio 4', page_id=3, url='https://s3.eu-central-1.amazonaws.com/audio4.mp3',).save()

    video = apps.get_model("content", "Video")
    video(title='video 1', page_id=2, weight=50, url='https://s3.eu-central-1.amazonaws.com/video1.mp4',).save()
    video(title='video 2', page_id=2, weight=500, url='https://s3.eu-central-1.amazonaws.com/video2.mp4',).save()
    video(title='video 3', page_id=1, url='https://s3.eu-central-1.amazonaws.com/video3.mp4',).save()
    video(title='video 4', page_id=1, weight=1000, url='https://s3.eu-central-1.amazonaws.com/video4.mp4',).save()

    text = apps.get_model("content", "Text")
    text(title='text 1', page_id=1, weight=50, content='Текст 1',).save()
    text(title='text 2', page_id=2, weight=500, content='Текст Текст 2',).save()
    text(title='text 3', page_id=3, content='Текст Текст Текст 3',).save()


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20180814_2013'),
        ('content', '0001_initial')
    ]

    operations = [
        migrations.RunPython(load_data, reverse_code=lambda apps, schema_editor: None)
    ]

