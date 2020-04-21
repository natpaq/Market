# chat/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_chat, name='main_chat'),
    path('<str:room_name>', views.room, name='room'),
]


