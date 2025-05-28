from django import forms
from .models import Club


class ClubForm(forms.ModelForm):
    '''
    Class form for create Club.
    '''

    def save(self, commit=True):
        instance = super(ClubForm, self).save(commit=False)
        instance.description = instance.description + '...'
        if commit:
            instance.save(commit=True)
        return instance

    class Meta:
        model = Club
        fields = ['name',
                  'location',
                  'img_emblem',
                  'since_year',
                  'description',
                  'site_page',
                  'user',
                  ]
