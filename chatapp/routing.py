from django.urls import re_path
from .import consumers
websocket_urlpatterns=[
    re_path(r'ws/chatroom/(?P<receiver>\w+)/$',consumers.chatconsumer.as_asgi()),
    re_path(R'ws/mainsocket/',consumers.Mainsocket.as_asgi())
]