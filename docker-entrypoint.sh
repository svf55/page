#!/bin/bash
./wait-for-it.sh db:5432
./manage.py migrate
./manage.py runserver 0.0.0.0:8000
