from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.sites import requests
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from .models import *

menu = [
    {'title': "About", 'url_name': 'about'},
    {'title': "Buy tickets", 'url_name': 'buy_ticket'},
    {'title': "Halls", 'url_name': 'halls'},
    {'title': "Employees", 'url_name': 'cashiers'},
    {'title': "Sign In", 'url_name': 'login'},
]


def index(request):
    films = Film.objects.all()
    genres = Genre.objects.all()
    context = {
        'films': films,
        'genres': genres,
        'menu': menu,
        'title': 'Main Page',
        'genre_selected': 0,
    }

    return render(request, 'index.html', context=context)


def genres(request):
    return HttpResponse("Films by genres")


def about(request):
    return render(request, 'about.html', {'title':'About'})


def buy_ticket(request):
    return HttpResponse("Tickets")


def halls(request):
    return HttpResponse("Halls")


def cashiers(request):
    return HttpResponse("Cashiers")


def login(request):
    return HttpResponse("Sign In")


def show_film(request, film_id):
    return HttpResponse(f"Film {film_id}")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')


def show_genre(request, genre_id):
    films = Film.objects.filter(genre_id=genre_id)
    genres = Genre.objects.all()

    if len(films) == 0:
        raise Http404()

    context = {
        'films': films,
        'genres': genres,
        'menu': menu,
        'title': 'Film by genre',
        'genre_selected': genre_id,
    }

    return render(request, 'index.html', context=context)
