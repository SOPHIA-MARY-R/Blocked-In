from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('sites/', views.sites, name='sites'),
    path('edit/', views.edit, name='edit'),
    path('delete/', views.delete, name='delete'),
    path('add/', views.add, name='add'),
    path('load/', views.load, name='load'),
    path('get/', views.get, name='get')
]
