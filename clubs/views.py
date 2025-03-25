from django.shortcuts import render, redirect
from .models import Club


def add_club(request):
    if request.method == "GET":
        return render(request, 'clubs/add-club.html')
    else:
        club = Club()
        club.name = request.POST['name']
        club.location = request.POST['location']
        club.user = request.user
        club.save()
        return redirect('/')
