from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views


urlpatterns = [
    path('', views.index),
    path('camp/', views.camp, name='camp'),
    path('camp_one/', views.camp_one, name='camp_one'),
    path('camp_two/', views.camp_two, name='camp_two'),
    path('camp_three/', views.camp_three, name='camp_three'),
    # path('check_availability/', views.check_availability, name='check_availability'),
    path('about/', views.about, name='about'),
    path('thankyou/', views.thankyou, name='thankyou'),
]
