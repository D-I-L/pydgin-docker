#!/bin/bash
python manage.py makemigrations           # Apply database migrations
python manage.py migrate
python manage.py makemigrations elastic
python manage.py migrate elastic
python manage.py collectstatic --noinput  # Collect static files
/usr/local/bin/gunicorn pydgin.wsgi:application -w 2 -b :8000
