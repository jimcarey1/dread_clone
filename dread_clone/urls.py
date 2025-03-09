from django.contrib import admin
from django.urls import path, include

from user.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home_url'),
    path('accounts/', include('user.urls')),
    path('community/', include('subdread.urls'))
]
