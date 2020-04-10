from django.urls import path, re_path

from . import consumers

websocket_urlpatterns = [
        path('ws/chat/<str:room_name>/', consumers.ChatConsumer, name='chatroom'),
        #re_path(r'^ws/chat/(?P<room_name>[^/]+)/s', ChatConsumer),
]


