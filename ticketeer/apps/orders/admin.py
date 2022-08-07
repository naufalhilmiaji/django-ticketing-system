from django.contrib import admin

from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('booking_code', 'name', 'total', 'status', 'created',
                    'is_verified', 'ordered_by')
    search_fields = ('name',)

admin.site.register(Order, OrderAdmin)