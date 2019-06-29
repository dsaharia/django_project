
from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'githubAPI'

urlpatterns = [
    path('', views.github,name='github')
]
