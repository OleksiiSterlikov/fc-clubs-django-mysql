from django.shortcuts import render, redirect, get_object_or_404
from .models import Club


def add_club(request):
    """
    The function added club. Function checking authentifications user and checking requests (GET or POST).
    If request 'GET' the function returned page adding clubs, if request 'POST' function create object Club and saves them.
    """
    if request.user.is_authenticated:
        if request.method == "GET":
            return render(request, 'clubs/add-club.html')
        else:
            club = Club()
            club.name = request.POST['name']
            club.location = request.POST['location']
            club.since_year = request.POST['since_year']
            club.description = request.POST['description']
            club.site_page = request.POST['site_page']
            club.user = request.user
            if 'img_emblem' in request.FILES:
                club.img_emblem = request.FILES['img_emblem']
            club.save()
            return redirect('/')
    else:
        return redirect('/')

def details_club(request, id):
    """
    The function of presenting the Club details.
    If club don't exist, it will be returned Error 404.
    """
    club = get_object_or_404(Club, id=id)
    return render(request, 'clubs/details.html', {'club': club})

