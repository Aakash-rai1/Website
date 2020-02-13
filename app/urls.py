from django.urls import path
from . import views

urlpatterns	=[
	path("",views.index),
	path("index",views.index),
	path("login",views.login),
	path("signup",views.signup),
	path("adsignup",views.adsignup),
	path("menu",views.menu),
	path('admins',views.admindashboard),
	path('userdashboard', views.dashboard),
	path('users',views.adminpanel)
]