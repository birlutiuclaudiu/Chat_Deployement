import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import Room, Message
from django.contrib.auth.models import User
# This comnsumer was creted using these tutorials 
# https://www.honeybadger.io/blog/django-channels-websockets-chat/
# https://www.youtube.com/watch?v=SF1k_Twr9cg   

class ChatRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.chat_box_name = self.scope["url_route"]["kwargs"]["chat_box_name"]
        self.group_name = "chat_%s" % self.chat_box_name
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)


    # This function receive messages from WebSocket.
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        if text_data_json["type"] == 'MESSAGE':
            message = text_data_json["message"]
            username = text_data_json["username"]
            chat_box_name=text_data_json["chat_box_name"]
            image=text_data_json["image"]
            await self.channel_layer.group_send(
            self.group_name,
                {
                "type": "chatbox_message",
                "message": message,
                "username": username,
                "image": image,
            },
            )
        elif text_data_json["type"] == 'WRITING' :
            username = text_data_json["username"]
            await self.channel_layer.group_send(
            self.group_name,
                {
                "type": "writing_listener",
                "username": username,
            },
            )
        elif text_data_json["type"] == 'STOP_WRITING':
            await self.channel_layer.group_send(
            self.group_name,
                {
                "type": "stop_writing_listener",
            },
            )

    # Receive message from room group.
    async def chatbox_message(self, event):
        message = event["message"]
        username = event["username"]
        image = event["image"]
        #send message and username of sender to websocket
        await self.send(
            text_data=json.dumps(
                {   "type": "MESSAGE",
                    "message": message,
                    "username": username,
                    "image" : image
                }
            )
        )
    
    async def writing_listener(self, event):
        username = event["username"]
        #send message and username of sender to websocket
        await self.send(
            text_data=json.dumps(
                {   "type": "WRITING",
                    "username": username,
                }
            )
        )

    async def stop_writing_listener(self, event):
        #send message and username of sender to websocket
        await self.send(
            text_data=json.dumps(
                {   
                    "type": "STOP_WRITING",
                }
            )
        )


    @sync_to_async
    def persistence_messages(self, slug_room, message, username):
        user = User.objects.filter(username = username).first()
        room = Room.objects.filter(slug=slug_room).first()
     
        messagePersist = Message(user = user, room=room, message = message)
        messagePersist.save()

    pass