from random import randint
from time import sleep
import json
from channels.generic.websocket import WebsocketConsumer
import asyncio
import random
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import RandomNumber


class RandomNumberConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        await self.accept()
        await self.send_last_random_number()

    async def send_last_random_number(self):
        last_number = RandomNumber.objects.last()
        if last_number:
            await self.send(text_data=json.dumps({'number': last_number.value}))
# class RandomNumberConsumer(AsyncWebsocketConsumer):
#     random_number = None
#
#     async def connect(self):
#         await self.accept()
#         while True:
#             if RandomNumberConsumer.random_number is None:
#                 RandomNumberConsumer.random_number = randint(1, 100)
#             await self.send_number()
#             await asyncio.sleep(1)
#
#     async def send_number(self):
#         await self.send(json.dumps({'number': RandomNumberConsumer.random_number}))


# class RandomNumberConsumer(AsyncWebsocketConsumer):
#     random_number = None
#
#     async def connect(self):
#         await self.accept()
#
#         while True:
#             if RandomNumberConsumer.random_number is None:
#                 RandomNumberConsumer.random_number = random.randint(1, 100)
#             await self.send_number()
#             await asyncio.sleep(5)
#
#     async def send_number(self):
#         await self.send(json.dumps({'number': RandomNumberConsumer.random_number}))

# async def receive(self, text_data):
#     RandomNumberConsumer.random_number = random.randint(1, 100)
#     await self.send_number()
