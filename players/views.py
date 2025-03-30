from django.shortcuts import render, redirect

from clubs.models import Club
from .models import Player


def add_player(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            clubs = Club.objects.all()
            return render(request, "players/add-player.html", {'clubs': clubs})
        else:
            player = Player()
            player.first_name = request.POST['first_name']
            player.last_name = request.POST['last_name']
            player.birth_date = request.POST['birth_date']
            player.club = request.POST['club']
            player.user = request.user
            player.save()
            return redirect('/')
    else:
        return redirect('/')
