from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('film/<int:film_id>/', show_film, name='film'),
    path('about/', about, name='about'),
    path('halls/', halls, name='halls'),
    path('emploeeys/', cashiers, name='cashiers'),
    path('buyticket/', buy_ticket, name='buy_ticket'),
    path('login/', login, name='login'),
    path('genre/<int:genre_id>/', show_genre, name='genre')
]
