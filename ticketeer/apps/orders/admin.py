from django.contrib import admin

from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('booking_code', 'name', 'total', 'order_date', 'status',
                    'created', 'is_verified', 'ordered_by')
    search_fields = ('name',)
    
    def save_model(self, request, obj, form, change) -> None:
        super().save_model(request, obj, form, change)
        obj.trip.available_seats -= 1
        obj.trip.total_passengers += 1
        obj.trip.save()

admin.site.register(Order, OrderAdmin)