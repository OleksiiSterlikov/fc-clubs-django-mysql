from django.shortcuts import render, redirect, get_object_or_404
from .models import Club, League, LeagueClub
from .forms import ClubForm


def add_club(request):
    """
    The function added club. Function checking authentifications user and checking requests (GET or POST).
    If request 'GET' the function returned page adding clubs, if request 'POST' function create object Club and saves them.
    """
    if request.user.is_authenticated:
        if request.method == 'GET':
            form = ClubForm()
            leagues = League.objects.all()
            return render(request, 'clubs/add-club.html', {'form': form, 'leagues': leagues})
        else:
            form = ClubForm(request.POST, request.FILES)
            if form.is_valid():
                instance = form.save()
                for league in request.POST.getlist('leagues', []):
                    league_club = LeagueClub()
                    league_club.club = Club.objects.get(id=instance.id)
                    league_club.league = League.objects.get(id=int(league))
                    league_club.save()
                return redirect('/')
            else:
                return render(request, 'clubs/add-club.html', {'form': form})
    else:
        return redirect('/')


def edit_club(request, id):
    """
    The function edit club. Function checking authentifications user.
    If the user is authenticated, the function posts information about the club to the page.
    """
    if request.user.is_authenticated:
        club = Club.objects.get(id=id)
        leagues = League.objects.all()
        club_leagues = LeagueClub.objects.filter(club_id=club.id)
        return render(request, 'clubs/add-club.html', {
            'club': club,
            'club_leagues': club_leagues,
            'leagues': leagues
        })
    else:
        raise PermissionError


def add_league(request):
    """
    The function added league. Function checking authentifications user and checking requests (GET or POST).
    If request 'GET' the function returned page adding league, if request 'POST' function create object League and saves them.
    """
    if request.user.is_authenticated:
        if request.method == 'GET':
            return render(request, 'clubs/league/add-league.html')
        else:
            league = League()
            league.title = request.POST['title']
            league.description = request.POST['description']
            if 'img_emblem' in request.FILES:
                league.img_emblem = request.FILES['img_emblem']
            league.save()
            return redirect('/')
    else:
        return redirect('/')


def update_club(request, id):
    """
    The function updated information about club. Function checking authentifications user
    If the user is authenticated, the function accepts requests changed information about the club and saves them.
    """
    if request.user.is_authenticated:
        club = Club.objects.get(id=id)
        club.name = request.POST['name']
        club.location = request.POST['location']
        club.since_year = request.POST['since_year']
        club.description = request.POST['description']
        club.site_page = request.POST['site_page']
        club.save()
        LeagueClub.objects.filter(club_id=club.id).delete()
        for league in request.POST.getlist('leagues', []):
            league_club = LeagueClub()
            league_club.club = club
            league_club.league = League.objects.get(id=int(league))
            league_club.save()
    return redirect('/')


def details_club(request, id):
    """
    The function of presenting the Club details.
    If the club don't exist, it will be returned Error 404.
    """
    club = get_object_or_404(Club, id=id)
    return render(request, 'clubs/details.html', {'club': club})
