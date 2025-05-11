from django.contrib import admin

from .models import Club, League, LeagueClub

# Register models Club, League and Connections LeagueClub.
admin.site.register(Club)
admin.site.register(League)
admin.site.register(LeagueClub)
