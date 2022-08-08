from xml.etree.ElementInclude import include
from django.urls import path
from .views import search_trip


app_name = 'orders'

urlpatterns = [
    path('search/', search_trip, name='search_trip'),
]
