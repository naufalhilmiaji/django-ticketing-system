from django.http import HttpRequest, HttpResponse
from django.contrib.auth import login as django_login, logout as django_logout
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from ticketeer.apps.trips.models import Trip
from ticketeer.website.orders.forms import SearchForm

from .forms import LoginForm, RegistrationForm


def index(request: HttpRequest) -> HttpResponse:
    form = SearchForm(data=request.POST or None, trip=Trip)        
    
    context = {
        'title': 'Ticketeer - Index',
        'app': 'Ticketeer',
        'search_form': form,
    }

    return render(request, 'website/index.html', context)


def login(request: HttpRequest) -> HttpResponse:
    if not request.user.is_authenticated:
        form = LoginForm(data=request.POST or None)

        if form.is_valid():
            user = form.authenticate()
            if user:
                django_login(request, user)
                return redirect('website:index')

        context = {
            'title': 'Login',
            'form': form,
        }

        return render(request, 'website/login.html', context)
    else:
        return redirect('website:index')


def logout(request: HttpRequest) -> HttpResponse:
    django_logout(request)
    return redirect('website:index')


def register(request: HttpRequest) -> HttpResponse:
    if not request.user.is_authenticated:
        form = RegistrationForm(data=request.POST or None)

        if form.is_valid():
            user = form.save()
            response = redirect('website:index')
            django_login(request, user)
            return response
        
        context = {
            'title': 'Ticketeer - Registration',
            'form': form,
        }

        return render(request, 'website/register.html', context)
    else:
        return redirect('website:index')

