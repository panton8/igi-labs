from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .forms import SignUpForm


def home_screen_view(request):
    return render(request, 'index.html', {})


def films_view(request):
    return render(request, 'index.html', {})


def halls_view(request):
    return render(request, 'index.html', {})


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')


def sign_up(request):
    context = {}
    context['form'] = SignUpForm()
    return render(request, 'signup.html', context)
