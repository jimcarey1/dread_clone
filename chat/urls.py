from django.urls import path
from . import views

urlpatterns = [
    path('<str:base32_username>/', views.chat_view, name='chat'),
]
