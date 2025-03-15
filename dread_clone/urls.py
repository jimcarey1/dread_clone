from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from user.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home_url'),
    path('accounts/', include('user.urls')),
    path('community/', include('subdread.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
