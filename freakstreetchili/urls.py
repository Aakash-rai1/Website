from sys import path

"""freakstreetchili URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
   https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auser',views.admindashboard),
    path('admindashboard',views.admindashboard),
    path('adminpanel',views.adminpanel),
    path('adminlogin',views.alogin),
    path('edit/<int:id>',views.edit),
    path('adminedit/<int:aid>',views.adminedit),
    path('update/<int:id>',views.update),
    path('adminupdate/<int:aid>',views.adminupdate),
    path('login',views.login),
    path('alogin',views.alogin),
    path('loginpage',views.loginpage),
    path('aloginpage',views.aloginpage),
    path('delete/<int:id>',views.delete),
    path('adelete/<int:aid>',views.adelete),
    path('',include('app.urls'))
]
 