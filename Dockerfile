FROM python:3.6

COPY . ./page

WORKDIR ./page

RUN pip install Django==2.0.5

RUN pip install psycopg2

RUN pip install requests

RUN pip install djangorestframework

RUN pip install django-model-utils