from django.urls import path, include

from . import views


urlpatterns = [
	path('', views.index, name='index'),
	path('signup', views.signup, name='signup'),
	path('login', views.do_login, name='login'),
	path('logout', views.do_logout, name='logout'),
	path('<int:id>/edit/', views.item_update, name='item_update'),
	path('add_to_cart/<id>/', views.add_to_cart, name="add_to_cart"),
	path('remove_from_cart/<id>/', views.remove_from_cart, name="remove_from_cart"),
]
