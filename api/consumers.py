import json
from channels.generic.websocket import AsyncWebsocketConsumer

class VacancyConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.company_id = str(self.scope['url_route']['kwargs']['company_id'])
        await self.channel_layer.group_add(
            self.company_id, self.channel_name,
        )
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.company_id, self.channel_name,
        )

    async def send_noticification(self, event: dict):
        await self.send(text_data=json.dumps(event))