from typing import Optional
from django.db import models
from django.utils import timezone

from ticketeer.apps.transportations.models import Transportation


class Trip(models.Model):
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    departure_time = models.TimeField(blank=True, null=True)
    arrival_time = models.TimeField(blank=True, null=True)
    eta = models.TimeField(blank=True, null=True)
    available_seats = models.IntegerField(null=True)
    created = models.DateTimeField(auto_now_add=True)

    transportations = models.ManyToManyField(Transportation, related_name="trips")


    class Meta:
        ordering = ['origin']


    def __str__(self) -> str:
        return f'{self.origin} - {self.destination}'
    
    def get_time_diff(self) -> 'Trip':
        return self.departure_time - self.eta
    
    def reservation(self) -> Optional['Trip']:
        if self.available_seats != 0:
            return self.available_seats - 1
        return None
