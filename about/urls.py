"""urls for about app"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),
]
