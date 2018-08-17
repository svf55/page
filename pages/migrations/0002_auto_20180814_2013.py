# encoding: utf8

from django.db import migrations


def load_data(apps, schema_editor):
    page = apps.get_model("pages", "Page")

    page(title='page 1',).save()
    page(title='page 2',).save()
    page(title='page 3',).save()


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_data, reverse_code=lambda apps, schema_editor: None)
    ]

