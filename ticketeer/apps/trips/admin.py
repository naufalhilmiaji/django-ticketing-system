from django.contrib import admin

from .models import Trip


class TripAdmin(admin.ModelAdmin):
    list_display = ('origin', 'destination', 'departure_time',
                    'departure_date', 'created')
    search_fields = ('origin', 'destination',)

admin.site.register(Trip, TripAdmin)
