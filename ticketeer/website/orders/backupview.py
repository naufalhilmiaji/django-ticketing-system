from datetime import datetime

from django.http import HttpRequest, HttpResponse, JsonResponse
from django.db.models import Q
from django.shortcuts import redirect

from ticketeer.apps.trips.models import Trip
from ticketeer.website.orders.forms import SearchForm


def search_departure_date(request: HttpRequest) -> HttpResponse:
    origin = request.GET.get('origin')
    destination = request.GET.get('destination')
    transportation = request.GET.get('transportation')

    data = []
    trips = Trip.objects.filter(
                Q(origin=origin) &
                Q(destination=destination) &
                Q(transportation=transportation)
            )

    for trip in trips:
        data.append({
            'date': trip.departure_date
        })
    
    return JsonResponse(data, safe=False)


def search_trip(request: HttpRequest) -> HttpResponse:
    form = SearchForm(data=request.POST or None, trip=Trip)
    
    if form.is_valid():
        print(form.data)

        origin = form.data.get('origin')
        destination = form.data.get('destination')
        transportation = form.data.get('transportation')
        departure_date = form.data.get('departure_date')
        departure_time = form.data.get('departure_time')

        date = datetime.strptime(f'{departure_date}', '%Y-%m-%d').date()
        time = datetime.strptime(f'{departure_time}', '%H:%M:%S').time()
        
        trip = Trip.objects.filter(
            Q(origin=origin) &
            Q(destination=destination) &
            Q(transportation=transportation) &
            Q(departure_date=date) &
            Q(departure_time=time)
        )

        print(origin, destination, transportation, date, time)

        if trip:
            response = {
                ''
            }

            print(trip)

            return redirect('website:index')
        else:
            print('\nTidak tersedia.\n')
    return redirect('website:index')

