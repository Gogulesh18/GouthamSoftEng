from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login, name="login"),
    path('signup/',views.signup, name="signup"),
    path('',views.home, name="home"),
    path('logout/',views.logout,name="logout")
]