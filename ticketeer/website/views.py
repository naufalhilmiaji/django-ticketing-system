from django.http import HttpRequest, HttpResponse
from django.contrib.auth import login as django_login, logout as django_logout
from django.shortcuts import get_object_or_404, redirect, render

from .forms import LoginForm, RegistrationForm


def index(request: HttpRequest) -> HttpResponse:
    context = {
        'title': 'Ticketeer - Index',
        'app': 'Ticketeer',
    }

    return render(request, 'website/index.html', context)


def login(request: HttpRequest) -> HttpResponse:
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

    return render(request, 'website/form.html', context)


def register(request: HttpRequest) -> HttpResponse:
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

    return render(request, 'website/form.html', context)

