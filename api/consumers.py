import json
from channels.generic.websocket import AsyncWebsocketConsumer

class VacancyConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add(
            "submitted", self.channel_name,
        )
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            "submitted", self.channel_name,
        )

    async def send_noticification(self, event: dict):
        await self.send(text_data=json.dumps(event))