
from django.urls import re_path , include
from aso_chat.consumers import ChatRoomConsumer
 

websocket_urlpatterns=[
                    re_path(r'ws/chat/(?P<chat_box_name>[\w\-]+)/$', ChatRoomConsumer.as_asgi()),
                ]