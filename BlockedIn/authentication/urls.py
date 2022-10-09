from django.urls import path
from . import views
from django.contrib.auth import views as auth

urlpatterns=[
    path('', views.welcome, name='welcome'),
    path('register/', views.register, name='register'),
    path('login/', views.Login, name='login'),
    path('logout/', auth.LogoutView.as_view(template_name='authentication/welcome.html'), name='logout'),
]