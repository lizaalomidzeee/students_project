from django.urls import path
from . import views
from django.shortcuts import render

urlpatterns = [
    path('', views.home_view, name='home'),
    path('main/', views.main_page_view, name='main_page'),
    path('students/', views.students_page_view, name='students_page'),
]



