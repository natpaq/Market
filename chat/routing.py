# chat/routing.py
from django.urls import re_path
#from . import consumers
from .consumers import ChatConsumer

websocket_urlpatterns = [
#    path('ws/chat/<str:room_name>/', consumers.ChatConsumer, name='chatroom'),
    re_path(r'^ws/chat/(?P<room_name>[^/]+)/$', ChatConsumer),
]