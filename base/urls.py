
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homeView, name='home'),
    path('room/<str:pk>', views.roomView, name='room'),
    path('create-book/', views.createBook, name='create-book'),
    path('edit-blog/<str:pk>', views.editBlog, name='edit-blog'),
    path('add-blog/<str:pk>', views.addBlog, name='add-blog')
]

