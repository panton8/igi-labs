from django.urls import path

from .views import *

urlpatterns = [
    path('', FilmHome.as_view(), name='home'),
    path('film/<int:film_id>/', ShowFilm.as_view(), name='film'),
    path('about/', about, name='about'),
    path('halls/', halls, name='halls'),
    path('emploeeys/', cashiers, name='cashiers'),
    path('buyticket/', buy_ticket, name='buy_ticket'),
    path('login/', login, name='login'),
    path('genre/<int:genre_id>/', FilmGenre.as_view(), name='genre')
]
