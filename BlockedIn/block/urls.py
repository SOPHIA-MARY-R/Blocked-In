from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.sites, name='sites'),
    path('create/', views.create, name='create'),
    #path('update/<int:id>', views.update, name='update'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('add/', views.add, name='add'),
    path('get/', views.get, name='get')
]
