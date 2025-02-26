from django.urls import path

from .views import registration_view

urlpatterns = [
    path('register/', registration_view, name='user_registration_url'),
]