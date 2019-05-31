from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.readPosts, name="readPosts"),
    path('getCsrf', views.getCsrf, name="getCsrf"),
    path('<int:pk>/checkAuthToPost', views.checkAuthToPost, name="checkAuthToPost"),
    path('<int:pk>', views.readPost, name="readPost"),
    path('create', views.createPost, name="createPost"),
    path('<int:pk>/update', views.updatePost, name="updatePost"),
    path('<int:pk>/delete', views.deletePost, name="deletePost"),
]
