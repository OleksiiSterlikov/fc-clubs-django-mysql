from django.contrib import admin

from .models import Club, League, LeagueClub

# Register your models here.
admin.site.register(Club)
admin.site.register(League)
admin.site.register(LeagueClub)
