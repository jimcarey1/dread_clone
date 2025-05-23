from django.urls import path

from .views import logout_view, profile_view, user_profile_view

urlpatterns = [
    # path('register/', registration_view, name='user_registration_url'),
    # path('login/', login_view, name='user_login_url'),
    path('logout/', logout_view, name='user_logout_url'),
    path('profile/', profile_view, name='user_profile_url'),
    path('<str:username>/profile/', user_profile_view, name='other_user_profile_url'),
]