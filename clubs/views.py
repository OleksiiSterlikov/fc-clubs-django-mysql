from django.shortcuts import render, redirect, get_object_or_404
from .models import Club


def add_club(request):
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


def edit_club(request, id):
    if request.user.is_authenticated:
        club = Club.objects.get(id=id)
        return render(request, 'clubs/add-club.html', {'club': club})
    else:
        raise PermissionError


def update_club(request, id):
    if request.user.is_authenticated:
        club = Club.objects.get(id=id)
    return redirect('/')


def details_club(request, id):
    club = get_object_or_404(Club, id=id)
    return render(request, 'clubs/details.html', {'club': club})
