from django.urls import path

from .views import create_post

urlpatterns = [
    path('create/', create_post, name='post_create_url'),
]