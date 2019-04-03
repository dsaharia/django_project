from django.urls import path
from . import views # import the views file

urlpatterns = [
    path('', views.index, name='index')
]
