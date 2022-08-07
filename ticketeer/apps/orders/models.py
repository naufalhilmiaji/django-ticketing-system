from django.db import models

from ticketeer.constants import ORDER_STATUS


class Order(models.Model):
    name = models.CharField(max_length=255)
    total = models.FloatField()
    status = models.PositiveSmallIntegerField(choices=ORDER_STATUS.choices, default=ORDER_STATUS.dibuat)
    is_verified = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    ordered_by = models.OneToOneField('users.User', related_name='ordered_by', on_delete=models.CASCADE)
    trip = models.OneToOneField('trips.Trip', related_name='trip', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.name} ({self.type})'
