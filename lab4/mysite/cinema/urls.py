from django.urls import path

from .views import *

urlpatterns = [
    path('', FilmHome.as_view(), name='home'),
    path('film/<int:film_id>/', ShowFilm.as_view(), name='film'),
    path('about/', about, name='about'),
    path('halls/', halls, name='halls'),
    path('emploeeys/', cashiers, name='cashiers'),
    path('buyticket/', buy_ticket, name='buy_ticket'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),
    path('genre/<int:genre_id>/', FilmGenre.as_view(), name='genre'),
    path('tickets/', show_tickets, name='tickets'),
    path('tickets/deletetickets.html', delete_tickets, name='delete_tickets'),
path('tickets/changetickets.html', change_tickets, name='change_tickets'),
]
