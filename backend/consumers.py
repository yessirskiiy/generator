from channels.generic.websocket import AsyncWebsocketConsumer


class RandomNumberConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add('random_number', self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard('random_number', self.channel_name)

    async def send_number(self, event):
        text_message = str(event['text'])
        await self.send(text_message)
