web: gunicorn generator.wsgi --log-file -
celery: celery --app=generator worker -loglevel=info
celerybeat: celery -A generator beat