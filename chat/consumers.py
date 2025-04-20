import json
from channels.generic.websocket import AsyncWebsocketConsumer
from user.models import User
from .models import Chat

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.other_username = self.scope['url_route']['kwargs']['username']
        self.user = self.scope['user']
        if self.scope['user'].username == self.other_username:
            await self.disconnect()

        self.room_name = f'chat_{min(self.user.username, self.other_username)}_{max(self.user.username, self.other_username)}'
        self.room_group_name = f'chat_{self.room_name}'


        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']

        recipient = await self.get_user(self.other_username)
        if recipient:
            await self.save_message(self.user, recipient, message)

            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message,
                    'sender': self.user.username,
                }
            )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            'message': event['message'],
            'sender': event['sender'],
        }))

    @staticmethod
    async def get_user(username):
        try:
            return await User.objects.aget(username=username)
        except User.DoesNotExist:
            return None
        
    @staticmethod
    async def save_message(sender, recipient, message):
        await Chat.objects.acreate(sender=sender, recipient=recipient, message=message)
