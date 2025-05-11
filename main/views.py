from django.conf import settings
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import MenuItem
from clubs.models import Club
from players.models import Player
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q

# Create your views here.
def home(request):
    """
    Function to render the home page and return clubs and players
    """
    menu_items = MenuItem.objects.all()
    clubs = Club.objects.filter(display_on_main_page=True, approved=True).order_by("name")
    players = Player.objects.filter(Q(display_on_main_page=True) | Q(approved=True))
    return render(request, 'main/index.html',
                  {
                      'menu_items': menu_items,
                      'clubs': clubs,
                      'players': players,
                  })
def sign_up(request):
    """
    Function to sign up new user
    If request POST creates a new user and save them.
    If request GET render sign up page.
    """
    if request.method == "POST":
        user = User()
        user.username = request.POST['username']
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.set_password(request.POST['password'])
        user.is_superuser = False
        user.is_staff = False
        user.is_active = True
        user.save()
        if user is not None:
            login(request, user)
        return redirect('/')
    else:
        return render(request, 'main/sign-up.html', {})

def sign_in(request):
    """
    Function to sign in user.
    If request POST checking username, password and redirect main page.
    If request GET render sign in page.
    """
    if request.method == "POST":
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
        return redirect('/')
    else:
        return render(request, 'main/sign-in.html', {})

def logout_user(request):
    """
    Function to log out user.
    """
    if request.user.is_authenticated:
        logout(request)
    return redirect('/')
