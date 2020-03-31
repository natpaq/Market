from django.urls import path, include
from . import views

urlpatterns = [
    path('list_item', views.add_item, name="list_item"),
    path('my_items', views.my_items, name="my_items"),
    path('add_to_cart/<id>/', views.add_to_cart, name="add_to_cart"),
    path('remove_from_cart/<id>/', views.remove_from_cart, name="remove_from_cart"),
    path('my_cart', views.my_cart, name="my_cart"),
    path('delete_from_cart/<id>/', views.delete_from_cart, name="delete_from_cart"),
    path('checkout', views.checkout, name="checkout"),
]
