import json
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Message,Room




class ChatConsumer(AsyncWebsocketConsumer):

    @database_sync_to_async
    def save_message(self, room, message):
        room = Room.objects.get(slug=room)
        return Message.objects.create(room=room, text=message)
    
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        room = text_data_json['room']
        

        # Send message to room group
        await self.save_message(room, message)
        
        await self.channel_layer.group_send(
            self.room_group_name, 
            {
                "type": "chat_message", 
                "message": message,
                'room':room
                
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]
        room= event['room']
        # new_msg = await self.save_message(room,message)
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            "message": message,
            'room': room
        }))

