from django.shortcuts import render, redirect, get_object_or_404

from clubs.models import Club
from .models import Player


def add_player(request):
    """
    The function added player. Function checking authentifications user and checking requests (GET or POST).
    If request 'GET' the function returned page adding player, if request 'POST' function create object Player and saves them.

    """
    if request.user.is_authenticated:
        if request.method == 'GET':
            clubs = Club.objects.all()
            return render(request, "players/add-player.html", {'clubs': clubs})
        else:
            print(request.POST)
            player = Player()
            player.first_name = request.POST['first_name']
            player.last_name = request.POST['last_name']
            player.birth_date = request.POST['birth_date']
            player.club = get_object_or_404(Club, id=request.POST['club_id'])
            player.user = request.user
            player.save()
            return redirect('/')
    else:
        return redirect('/')
