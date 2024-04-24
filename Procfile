web: daphne --port 10000 --bind 0.0.0.0 generator.asgi:application
worker: celery --app=generator worker -l INFO
beat: celery -A generator beat