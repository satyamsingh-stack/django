"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from home.views import *
from vege.views import *

urlpatterns = [
    path('',home),
    path("sucess/",sucess),
    path('reciepes/',reciepes),
    path('delete_rec/<id>/', delete_rec),
    path('update_recipe/<id>', update_recipe),
    path('login_page/', login_page),
    path('register/', register),
    path('logout_page/',logout_page),
    path('admin/', admin.site.urls),
]
