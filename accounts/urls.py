from django.urls import path, include

from . import views


urlpatterns = [
	path('', views.index, name='index'),
	path('signup', views.signup, name='signup'),
	path('login', views.do_login, name='login'),
	path('logout', views.do_logout, name='logout'),
	path('<int:id>/edit/', views.item_update, name='item_update'),
]
