#!/bin/bash

git pull
python manage.py makemigrations           # Apply database migrations
python manage.py migrate
python manage.py makemigrations elastic
python manage.py migrate elastic
python manage.py collectstatic --noinput  # Collect static files

# load indices as require
#sleep 20
#python manage.py pipeline \
#    --dir /usr/src/app/src/data-pipeline/data_pipeline/data \
#    --ini download.ini --sections DISEASE --steps load

/usr/local/bin/gunicorn pydgin.wsgi:application -w 2 -b :8000
