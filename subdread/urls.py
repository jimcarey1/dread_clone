from django.urls import path

from .views import create_community, community_setup

urlpatterns = [
    path('create/', create_community, name='community_create_url'),
    path('<str:subdread>/setup/', community_setup , name='community_setup_url'),
]