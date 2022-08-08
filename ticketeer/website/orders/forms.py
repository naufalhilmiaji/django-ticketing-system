from typing import Any, Dict, Optional

from django import forms
from django.db.models import Q

from ticketeer.apps.users.models import User
from ticketeer.apps.trips.models import Trip


class SearchForm(forms.Form):
    origin = forms.ModelChoiceField(queryset=Trip.objects.all().values_list('origin', flat=True).distinct())
    destination = forms.ModelChoiceField(queryset=Trip.objects.all().values_list('destination', flat=True).distinct())
    transportation = forms.ModelChoiceField(queryset=Trip.objects.all().values_list('transportation', flat=True).distinct())
    
    def clean(self) -> dict:
        cleaned_data = super().clean()
        if self.errors:
            return cleaned_data
        
        return cleaned_data
