import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'generator.settings')

celery_app = Celery('generator')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()

celery_app.conf.beat_schedule = {
    'add-every-5-seconds': {
        'task': 'backend.tasks.get_number',
        'schedule': 5.0
    },
}