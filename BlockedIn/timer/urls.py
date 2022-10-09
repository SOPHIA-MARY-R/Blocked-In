from django.urls import path
from . import views
from django.contrib.auth import views as auth

urlpatterns=[
    path('', views.home, name='home'),
]