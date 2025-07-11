from django.contrib import admin
from django.contrib.auth import login
from django.urls import path

from myapp import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('home/', views.index, name='home'),
    path('', views.register, name='register'),

]
