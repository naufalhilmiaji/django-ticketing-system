from django.db.models import IntegerChoices


class TRANSPORTATION_TYPE(IntegerChoices):
    bis = 1, 'Bis'
    kapal = 2, 'Kapal'
    kereta = 3, 'Kereta'


class ORDER_STATUS(IntegerChoices):
    dibuat = 1, 'Pesanan dibuat'
    diverifikasi = 2, 'Diverifikasi'
    dibayar = 3, 'Dibayar'
    selesai = 4, 'Selesai'
    batal = 5, 'Batal'
