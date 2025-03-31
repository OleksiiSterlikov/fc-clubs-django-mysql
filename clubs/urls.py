from django.urls import path
from django.views.generic import detail
from django.conf import settings
from django.conf.urls.static import static
from .views import add_club, details_club


urlpatterns = [
    path('add', add_club, name='add_club'),
    path('<int:id>', details_club, name='details_club'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)