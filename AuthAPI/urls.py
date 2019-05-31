from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('loginState', views.loginState, name="loginState"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),
]
