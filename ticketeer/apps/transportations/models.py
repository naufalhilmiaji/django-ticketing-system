from django.db import models

from ticketeer.constants import TRANSPORTATION_TYPE


class Transportation(models.Model):
    name = models.CharField(max_length=255)
    type = models.PositiveSmallIntegerField(choices=TRANSPORTATION_TYPE.choices,
                                            default=TRANSPORTATION_TYPE.bis)
    units = models.IntegerField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f'{self.name}'
