web: gunicorn generator.wsgi:application
worker: celery --app=generator worker -l INFO
beat: celery -A generator beat