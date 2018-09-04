from __future__ import absolute_import, unicode_literals
from django.db import transaction
from django.db.models import F
from content.models import Content
from page.celery import app


@app.task(ignore_result=True, max_retries=1, default_retry_delay=10)
def hello():
    print('\n*****  Hello! From Celery  ****** !!!\n')


@app.task
def increment_counter(pk):
    with transaction.atomic():
        content_qs = Content.objects.filter(page_id=pk)
        len(content_qs.order_by('id').select_for_update())
        content_qs.update(counter=F('counter') + 1)

