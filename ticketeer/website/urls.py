from django.urls import include,path
from .views import index, login, logout, register


app_name = 'website'

urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register'),
    path('orders/', include('ticketeer.website.orders.urls')),
]
