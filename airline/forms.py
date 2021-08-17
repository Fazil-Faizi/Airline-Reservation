from django import forms
from .models import Flight


class FlightSearch(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ('date','departure', 'arrival')
