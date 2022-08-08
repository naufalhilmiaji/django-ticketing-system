from typing import Any, Dict, Optional

from django import forms
from django.db.models import Q
from django.utils import timezone
from libraries.ui_utils.widgets import SelectDatetimeWidget

from ticketeer.apps.trips.models import Trip
from ticketeer.apps.transportations.models import Transportation


class SearchForm(forms.Form):
    origin = forms.ModelChoiceField(queryset=None, to_field_name=None)
    destination = forms.ModelChoiceField(queryset=None, to_field_name=None)
    transportation = forms.ModelChoiceField(queryset=None, to_field_name=None)
    departure_date = forms.ModelChoiceField(queryset=None, to_field_name=None)
    departure_time = forms.ModelChoiceField(queryset=None, to_field_name=None)

    # date_time = forms.DateTimeField(
    #     label='Tanggal Pemesanan', required=True,
    #     widget=SelectDatetimeWidget(years=range(timezone.localdate().year,
    #                                             timezone.localdate().year + 10))
    # )

    def __init__(self, trip: Trip, *args, **kwargs):
        self.trip = trip
        super().__init__(*args, **kwargs)
        self.fields['origin'].queryset = self.trip.objects.all().distinct().values_list('origin', flat=True)
        self.fields['origin'].to_field_name = 'origin'
        self.fields['destination'].queryset = self.trip.objects.all().distinct().values_list('destination', flat=True)
        self.fields['destination'].to_field_name = 'destination'
        self.fields['departure_date'].queryset = self.trip.objects.all().distinct().values_list('departure_date', flat=True)
        self.fields['departure_date'].to_field_name = 'departure_date'
        self.fields['departure_time'].queryset = self.trip.objects.all().distinct().values_list('departure_time', flat=True)
        self.fields['departure_time'].to_field_name = 'departure_time'
        self.fields['transportation'].queryset = Transportation.objects.all().distinct()
        self.fields['transportation'].to_field_name = 'id'

    
    def clean(self) -> dict:
        cleaned_data = super().clean()
        if self.errors:
            return cleaned_data
        
        return cleaned_data
