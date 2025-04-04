from django.urls import path

from .views import create_community, community_setup
from .views_mod_setup import mod_tools, post_flair

urlpatterns = [
    path('create/', create_community, name='community_create_url'),
    path('<str:subdread>/setup/', community_setup , name='community_setup_url'),
    path('mod/<str:subdread>/', mod_tools, name='community_mod_tools'),
    path('mod/<str:subdread>/postflair', post_flair, name='community_post_flair'),
]