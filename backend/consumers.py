import json

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import RandomNumber


class RandomNumberConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        await self.accept()
        await self.send_last_random_number()

    async def send_last_random_number(self):
        while True:
            last_number = await database_sync_to_async(RandomNumber.objects.last)()
            if last_number:
                await self.send(text_data=json.dumps({'number': last_number.number}))
