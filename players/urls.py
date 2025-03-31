from django.urls import path
from .views import add_player
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('add', add_player, name='add_player'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
