from django.db.models import IntegerChoices


class TRANSPORTATION_TYPE(IntegerChoices):
    bis = 1, 'Bis'
    kapal = 2, 'Kapal'
    kereta = 3, 'Kereta'
