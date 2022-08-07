from django.contrib import admin

from .models import Transportation


class TransportationAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Transportation, TransportationAdmin)
