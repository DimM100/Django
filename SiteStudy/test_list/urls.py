from django.urls import path
from . import views

urlpatterns = [
    path('test_begin', views.test_index, name = 'test_index'),
    path('', views.test_lobby_index, name = 'test_lobby_index'),
]
