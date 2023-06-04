from datetime import date, datetime
from django.utils import timezone
from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.sites import requests
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from .models import *
from .forms import *

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
        'main_page': True
    }

    return render(request, 'index.html', context=context)


def genres(request):
    return HttpResponse("Films by genres")


def about(request):
    return render(request, 'about.html', {'title': 'About'})


def buy_ticket(request):
    session = ...
    available_seats = ...
    exception = ""
    if request.method == 'POST':
        session = Session.objects.get(id=request.POST.get('session'))
        form = TicketPostForm(request.POST)
        tickets = int(request.POST.get('seats'))
        if session.available_seats >= tickets and form.is_valid():
            print(Hall.objects.get(name=session.hall.name))
            try:
                client = Client(first_name="A", last_name="B", date_of_birth=date.today(), email="w@gmail.com",phone_number="+375448574123")
                client.save()
                purchase = Purchase(client=client, session=session, updated_at=datetime.now())
                purchase.save()
                session.available_seats -= tickets
                session.save()
                return redirect('home')
            except:
                form.add_error(None, "Ticket purchase error")
        else:
            exception = f"Amount of available seats only: {available_seats}"
    else:
        form = TicketPostForm()
    context = {
        'form': form,
        'menu': menu,
        'title': 'Tickets',
        'exception': exception,
    }
    return render(request, 'buyticket.html', context=context)


def halls(request):
    halls = Hall.objects.all()
    context = {
        'halls': halls,
        'menu': menu,
        'title': 'Halls',
    }

    return render(request, 'hall.html', context=context)


def cashiers(request):
    cashiers = Cashier.objects.all()
    context = {
        'cashiers': cashiers,
        'menu': menu,
        'title': 'Cashiers'
    }

    return render(request, 'cashiers.html', context=context)


def login(request):
    return HttpResponse("Sign In")


def show_film(request, film_id):
    film = get_object_or_404(Film, pk=film_id)

    context = {
        'film': film,
        'menu': menu,
        'title': film.name,
        'genre_selected': film.genre_id
    }

    return render(request, 'film.html', context=context)


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
        'main_page': True
    }

    return render(request, 'index.html', context=context)
