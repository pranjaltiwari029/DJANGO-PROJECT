from django.contrib import admin
from django.urls import path
from apps import views

urlpatterns = [
    path("", views.index,name='home'),
    path("about/", views.about,name='about'),
    path("service/", views.index,name='service'),
]
