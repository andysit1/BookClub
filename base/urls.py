
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homeView, name='home'),
    path('room/<str:pk>', views.roomView, name='room'),
    path('edit-blog/<str:pk>', views.editBlog, name='edit-blog'),
    path('add_blog/<str:pk>', views.addBlog, name='add-blog'),
    path('add-book/<str:pk>', views.addBook, name='add-book'),

    path('find-book/', views.selectBook, name='select-book')
]

