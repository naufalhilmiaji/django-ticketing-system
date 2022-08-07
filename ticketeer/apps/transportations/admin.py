from django.contrib import admin

from .models import Transportation


class TransportationAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'units')
    search_fields = ('name', 'type',)

admin.site.register(Transportation, TransportationAdmin)
