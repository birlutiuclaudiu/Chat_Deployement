
from django.urls import re_path , include
from aso_chat.consumers import ChatRoomConsumer
 
# Here, "" is routing to the URL ChatConsumer which
# will handle the chat functionality.
websocket_urlpatterns=[
                    re_path(r'ws/chat/(?P<chat_box_name>[\w\-]+)/$', ChatRoomConsumer.as_asgi()),
                ]