from django import forms
from .models import ArtistSearch

class ArtistSearchForm(forms.ModelForm):
    class Meta:
        model = ArtistSearch
        fields = ('artist_name',)