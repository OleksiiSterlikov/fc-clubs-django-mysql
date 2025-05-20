from django import forms
from .models import Player


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['first_name',
                  'last_name',
                  'photo',
                  'birth_date',
                  'club',
                  ]
