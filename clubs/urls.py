from django.urls import path
from .views import add_club


urlpatterns = [
    path('/add', add_club, name='add_club'),
]