from django.contrib import admin
from django.urls import path, include

from user.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('accounts/', include('user.urls')),
]
