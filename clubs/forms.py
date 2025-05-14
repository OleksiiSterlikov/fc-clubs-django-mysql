from django import forms
from .models import Club, LeagueClub


class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = ['name',
                  'location',
                  'img_emblem',
                  'since_year',
                  'description',
                  'site_page',
                  ]
