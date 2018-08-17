#!/bin/bash
./wait-for-it.sh db:5432
./manage.py test -v2 --no-input