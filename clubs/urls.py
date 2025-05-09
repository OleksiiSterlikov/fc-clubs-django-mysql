from django.urls import path
from .views import add_club, details_club, edit_club, update_club, add_league

urlpatterns = [
    path('add', add_club, name='add_club'),
    path('edit/<int:id>', edit_club, name='edit_club'),
    path('update/<int:id>', update_club, name='update_club'),
    path('league/add', add_league, name='add_league'),
    path('<int:id>', details_club, name='details_club'),
]
