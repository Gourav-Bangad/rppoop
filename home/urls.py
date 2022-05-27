from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("login", views.login, name='login'),
    path("register", views.register, name='register'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'), 
    path("profile", views.profile, name='profile'), 
    path("forms", views.forms, name='forms'), 
]
