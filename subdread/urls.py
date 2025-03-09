from django.urls import path

from .views import create_community

urlpatterns = [
    path('create/', create_community, name='community_create_url'),
]