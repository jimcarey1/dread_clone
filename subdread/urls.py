from django.urls import path

from .views import create_community, community_setup, community_home
from .views_mod_setup import mod_tools, post_flair, rules, create_new_rule

urlpatterns = [
    path('create/', create_community, name='community_create_url'),
    path('<str:subdread>/', community_home, name='community_homepage_url'),
    path('<str:subdread>/setup/', community_setup , name='community_setup_url'),
    path('mod/<str:subdread>/', mod_tools, name='community_mod_tools'),
    path('mod/<str:subdread>/postflair', post_flair, name='community_post_flair'),
    path('mod/<str:subdread>/rules', rules, name='community_mod_rules'),
    path('mod/<str:subdread>/rules/new', create_new_rule, name='community_mod_create_new_rule'),
]