from celery import shared_task
import random
from .models import RandomNumber


@shared_task
def generate_number():
    number = random.randint(1, 100)
    obj, created = RandomNumber.objects.update_or_create(
        defaults={'number': number}
    )