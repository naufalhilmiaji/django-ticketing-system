from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    context = {
        'title': 'Ticketeer - Index',
        'app': 'Ticketeer',
    }

    return render(request, 'website/index.html', context)

