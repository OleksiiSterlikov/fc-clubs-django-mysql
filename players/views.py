from django.shortcuts import render, redirect, get_object_or_404

from clubs.models import Club
from .models import Player
from .forms import PlayerForm


def add_player(request):
    """
    The function added player. Function checking authentifications user and checking requests (GET or POST).
    If request 'GET' the function returned page adding player, if request 'POST' function create object Player and saves them.

    """
    if request.user.is_authenticated:
        if request.method == 'GET':
            form = PlayerForm()
            clubs = Club.objects.all()
            return render(request, "players/add-player.html", {'form': form,'clubs': clubs})
        else:
            form = PlayerForm(request.POST, request.FILES)
            print('+++++++++++++++++++++++++++++++')
            print(form.is_valid())
            print(form.data)
            print('+++++++++++++++++++++++++++++++')
            if form.is_valid():
                print(form.data)
                form.save()
                return redirect('/')
            return redirect('/')
    else:
        return redirect('/')
