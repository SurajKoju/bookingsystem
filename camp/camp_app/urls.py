from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views


urlpatterns = [
    path('', views.index),
    path('camp_one/', views.camp_one, name='camp_one'),
    path('camp_two/', views.camp_two, name='camp_two'),
    path('check_availability/', views.check_availability, name='check_availability'),
]
