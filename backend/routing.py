from django.urls import path

from .consumers import RandomNumberConsumer

ws_urlpatterns = [
    path('ws/random_number/', RandomNumberConsumer.as_asgi()),
]
