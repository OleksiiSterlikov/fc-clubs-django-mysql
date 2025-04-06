from django.urls import path
from .views import add_player
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('add', add_player, name='add_player'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
