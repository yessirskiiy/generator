import requests
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from celery import shared_task

channel_layer = get_channel_layer()


@shared_task
def get_number():
    url = 'http://127.0.0.1:8000/api/random/'
    response = requests.get(url)
    number = response.json()['random_number']

    async_to_sync(channel_layer.group_send)('random_number', {'type': 'send_number', 'text': number})

    return number
