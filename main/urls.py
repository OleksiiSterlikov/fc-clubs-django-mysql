from django.urls import path
from .views import home, sign_up, sign_in, logout_user


urlpatterns = [
    path('', home, name='home'),
    path('sign-up', sign_up, name='sign_up'),
    path('sign-in', sign_in, name='sign_in'),
    path('logout', logout_user, name='logout'),
]
