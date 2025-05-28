from django import forms
from .models import Player


class PlayerForm(forms.ModelForm):
    '''
    Class form for create Player.
    '''

    def save(self, commit=True):
        instance = super(PlayerForm, self).save(commit=False)
        instance.description = instance.description + '...'
        if commit:
            instance.save(commit=True)
        return instance

    class Meta:
        model = Player
        fields = ['first_name',
                  'last_name',
                  'photo',
                  'birth_date',
                  'club',
                  'user',
                  ]
