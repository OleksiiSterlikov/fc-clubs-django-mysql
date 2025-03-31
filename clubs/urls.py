from django.urls import path
from django.views.generic import detail

from .views import add_club, details_club


urlpatterns = [
    path('add', add_club, name='add_club'),
    path('<int:id>', details_club, name='details_club'),
]