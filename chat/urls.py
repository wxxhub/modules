"""chat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app import views

urlpatterns = [
    path('', views.welcome),
    path('index/', views.index),
    path('1/', views.welcome1),
    path('index1/', views.index1),
    path('2/', views.welcome2),
    path('index2/', views.index2),
    path('3/', views.welcome3),
    path('index3/', views.index3),
    path('submit_problem/', views.submitProblem),
    path('submit_number/', views.submitNumber),
    path('test/', views.test),
    path('download/', views.download),
    path('download_file/', views.responseFile),
    path('delete_file/', views.deleteFile),
]
