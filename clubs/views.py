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
            club.save()
            return redirect('/')
    else:
        return redirect('/')

def details_club(request, id):
    club = get_object_or_404(Club, id=id)
    return render(request, 'clubs/details.html', {'club': club})

