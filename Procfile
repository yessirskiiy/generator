web: python manage.py runserver
worker: celery --app=generator worker -l INFO
beat: celery -A generator beat