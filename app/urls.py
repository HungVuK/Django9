from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [
   path('', views.index),
   path('contact/', views.contact),
   path('blog/', views.blog),
]
