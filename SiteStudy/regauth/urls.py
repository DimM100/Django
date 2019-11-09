from django.urls import path, include
from . import views

urlpatterns = [
    path('registr/', views.RegisterFormView.as_view(), name = 'registr'),
    path('', views.LoginFormView.as_view(), name = 'login'),
]
