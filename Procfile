web: daphne -b 0.0.0.0 generator.asgi:application
worker: celery --app=generator worker -l INFO
beat: celery -A generator beat