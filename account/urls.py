from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.check, name = "check"),
    path('signup', views.signup, name = "signup"),
    path('assign', views.assign, name = "assign"),
]