from django.urls import path
from .views import add_player


urlpatterns = [
    path('/add', add_player, name='add_player'),
]
