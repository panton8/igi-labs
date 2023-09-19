from django.urls import path

from .views import *

urlpatterns = [
    path('', FilmHome.as_view(), name='home'),
    path('film/<int:film_id>/', ShowFilm.as_view(), name='film'),
    #path('halls/', halls, name='halls'),
    path('emploeeys/', cashiers, name='cashiers'),
    path('buyticket/', buy_ticket, name='buy_ticket'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),
    path('genre/<int:genre_id>/', FilmGenre.as_view(), name='genre'),
    path('tickets/', show_tickets, name='tickets'),
    path('tickets/deletetickets.html', delete_tickets, name='delete_tickets'),
    path('tickets/changetickets.html', change_tickets, name='change_tickets'),
    path('news/', list_news, name='list_news'),
    path('news/<int:news_id>/', news, name='news'),
    path('about/', about, name='about'),
    path('main/', main, name="main"),
    path('privacy/', privacy_policy, name="privacy_policy"),
    path('careers/', vacancies, name='vacancies'),
    path('reviews/', reviews, name='reviews'),
    path('all_reviews', all_reviews, name='all_reviews'),
    path('questions/', questions, name="questions"),
    path('stats/', stat, name='stat')
]