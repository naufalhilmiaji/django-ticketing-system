from typing import Optional

from django.core.validators import MinValueValidator
from django.db import models


class Trip(models.Model):
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    departure_time = models.TimeField(blank=True, null=True)
    arrival_time = models.TimeField(blank=True, null=True)
    eta = models.TimeField(blank=True, null=True)
    price = models.FloatField(validators=[MinValueValidator(0)])
    available_seats = models.IntegerField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    total_passengers = models.IntegerField(null=False, default=0)

    transportation = models.ForeignKey('transportations.Transportation', related_name="transportation",
                                        on_delete=models.CASCADE)


    class Meta:
        ordering = ['origin']


    def __str__(self) -> str:
        return f'{self.transportation} ({self.origin} - {self.destination})'
    
    def get_time_diff(self) -> 'Trip':
        return self.departure_time - self.eta
    
    def reservation(self) -> Optional['Trip']:
        if self.available_seats != 0:
            return self.available_seats - 1
        return None
