import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'generator.settings')

celery_app = Celery('generator')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()

celery_app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'backend.tasks.generate_number',
        'schedule': 5.0
    },
}