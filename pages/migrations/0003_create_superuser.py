# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import migrations
from django.contrib.auth.admin import User


def create_superuser(apps, schema_editor):
    superuser = User()
    superuser.is_active = True
    superuser.is_superuser = True
    superuser.is_staff = True
    superuser.username = 'justwork'
    superuser.email = 'admin@admin.net'
    superuser.set_password('justwork')
    superuser.save()


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
        ('pages', '0002_auto_20180814_2013'),
    ]

    operations = [
        migrations.RunPython(create_superuser, reverse_code=lambda apps, schema_editor: None)
    ]

