from django.urls import path

from .views import create_post, create_post_to_community, view_post

urlpatterns = [
    path('submit/', create_post, name='post_create_url'),
    path('<str:subdread>/submit/', create_post_to_community, name='post_create_community_url'),
    path('<str:subdread>/post/<int:post_id>/', view_post, name='post_view_url'),
]