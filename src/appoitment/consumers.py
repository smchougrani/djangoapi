import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add(
            "notification_group",
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            "notification_group",
            self.channel_name
        )

    async def receive(self, text_data):
        pass
        # Cette méthode peut être utilisée pour recevoir des messages directement du client

    async def send_notification(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message
        }))