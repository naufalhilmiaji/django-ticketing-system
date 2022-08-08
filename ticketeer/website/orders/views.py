from datetime import datetime

from django.http import HttpRequest, JsonResponse
from django.db.models import Q

from ticketeer.apps.trips.models import Trip
from ticketeer.website.orders.forms import SearchForm


def search_trip(request: HttpRequest) -> JsonResponse:
    form = SearchForm(data=request.POST or None, trip=Trip)

    origin = form.data.get('origin')
    destination = form.data.get('destination')
    transportation = form.data.get('transportation')

    date_time_day = form.data.get('day')
    date_time_month = form.data.get('month')
    date_time_year = form.data.get('year')
    date_time_hour = form.data.get('hour')
    date_time_minute = form.data.get('minute')

    date = datetime.strptime(f'{date_time_year}-{date_time_month}-{date_time_day}', '%Y-%m-%d').date()
    time = datetime.strptime(f'{date_time_hour}:{date_time_minute}:00', '%H:%M:%S').time()
    
    trips = Trip.objects.filter(
        Q(origin=origin) &
        Q(destination=destination) &
        Q(transportation=transportation) &
        Q(departure_date=date) &
        Q(departure_time__gte=time)
    )

    if trips:
        print(trips)
        response = {
            'status_code': 200,
            'data': list(trips.values('origin', 'destination', 'transportation__name',
                                      'departure_date', 'departure_time', 'price',
                                      'available_seats')),
        }

        return JsonResponse(response, safe=False)
    else:
        response = {
            'status_code': 400,
            'message': 'Tidak Tersedia.'
        }

        return JsonResponse(response)

