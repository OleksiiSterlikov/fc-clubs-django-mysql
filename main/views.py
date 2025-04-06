from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from .models import MenuItem
from clubs.models import Club
from players.models import Player
from django.db.models import Q

# Create your views here.
def home(request):
    menu_items = MenuItem.objects.all()
    for menu_item in menu_items:
        print(menu_item.url)
        # for element in menu_item.elements.all():
        #     print(element)
    print(settings.BASE_DIR)
    print(settings.STATIC_ROOT)
    print(settings.STATIC_URL)

    clubs = Club.objects.filter(display_on_main_page=True, approved=True).order_by("name")
    players = Player.objects.filter(Q(display_on_main_page=True) | Q(approved=True))
    return render(request, 'main/index.html',
                  {
                      'menu_items': menu_items,
                      'clubs': clubs,
                      'players': players,
                  })
def sign_up(request):
    if request.method == "POST":
        pass
    else:
        return render(request, 'main/sign-up.html', {})