from django.urls import path, include
from . import views

urlpatterns = [
    path('list_item', views.add_item, name="list_item")
]
