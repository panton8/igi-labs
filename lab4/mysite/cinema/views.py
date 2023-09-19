from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.contrib.sites import requests
from django.core.exceptions import PermissionDenied
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .forms import *
from .utils import *
import requests
from django.shortcuts import render
import matplotlib.pyplot as plt
from django.db.models import Count
from django.db.models.functions import TruncMonth
from django.contrib.auth.decorators import login_required


class FilmHome(DataMixin, ListView):
    model = Film
    template_name = 'index.html'
    context_object_name = 'films'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        g_def = self.get_user_context(title="Main Page", main_page=True)
        return dict(list(context.items()) + list(g_def.items()))


def about(request):
    dog_photo = requests.get("https://dog.ceo/api/breeds/image/random").json()
    if not request.user.is_authenticated:
        return render(request, 'about.html', {'title': 'About', 'menu': menu[0::2]})
    return render(request, 'about.html', {'title': 'About', 'menu': menu, 'dog_photo': dog_photo['message']})


def privacy_policy(request):
    cat_fact = requests.get('https://catfact.ninja/fact').json()
    if not request.user.is_authenticated:
        return render(request, 'privacy_policy.html', {'title': 'Privacy Policy', 'menu': menu[0::2]})
    return render(request, 'privacy_policy.html', {'title': 'Privacy Policy', 'menu': menu, 'cat_fact': cat_fact['fact']})


def list_news(request):
    news = News.objects.all()
    if not request.user.is_authenticated:
        return render(request, 'list_news.html', {'news': news, 'title': 'News', 'menu': menu[0::2]})
    return render(request, 'list_news.html', {'news': news, 'title': 'News', 'menu': menu})


def main(request):
    if not request.user.is_authenticated:
        return render(request, 'main.html', {'title': 'Main Page', 'menu': menu[0::2]})
    return render(request, 'main.html', {'title': 'Main Page', 'menu': menu})


@login_required
def buy_ticket(request):
    time = requests.get("http://worldtimeapi.org/api/timezone/Europe/Minsk").json()
    session = ...
    available_seats = ...
    exception = ""
    if request.method == 'POST':
        session = Session.objects.get(id=request.POST.get('session'))
        form = TicketPostForm(request.POST)
        tickets = int(request.POST.get('seats'))
        if SaleCode.objects.filter(code=request.POST.get('code')) and session.available_seats >= tickets:
            tickets += 1
        if session.available_seats >= tickets and form.is_valid():
            try:
                user = CustomUser.objects.get(email=request.user.email)
                client = Client.objects.get(phone_number=user.phone_number)
                if Purchase.objects.filter(session_id=session.id, client_id=client.id):
                    print("WOW")
                    purchase = Purchase.objects.filter(session_id=session.id, client_id=client.id)[0]
                    purchase.amount_of_tickets += tickets
                    purchase.save()
                    session.available_seats -= tickets
                    session.save()
                else:
                    purchase = Purchase(client=client, session=session, updated_at=timezone.now().date(), amount_of_tickets=tickets)
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
        'timezone': time['timezone'],
        'time': time['datetime'][11:16]
    }
    return render(request, 'buyticket.html', context=context)


def questions(request):
    return render(request, 'questions.html', {'title': 'Questions', 'menu': menu})


def all_reviews(request):
    context = {
        'menu': menu,
        'title': 'Reviews',
        "reviews": Review.objects.all()
    }
    return render(request, 'all_reviews.html', context=context)


def reviews(request):
    if request.method == 'POST':
        cf = ReviewForm(request.POST or None)
        if request.user.is_authenticated:
            if cf.is_valid():
                content = request.POST.get('content')
                rating = request.POST.get('rating')
                reviewer = CustomUser.objects.filter(email=request.user.email)[0]
                print(reviewer)
                review = Review(author=reviewer, content=content, rating=rating)
                review.save()
                context = {
                    'form': cf,
                    'menu': menu,
                    'title': 'Reviews',
                    'exception': "",
                    "reviews": Review.objects.all()
                }
                return render(request, 'all_reviews.html', context=context)
            else:
                cf = ReviewForm()
                print("wrong")
        else:
            return redirect('login')
    context = {
            'form': ReviewForm(),
            'menu': menu,
            'title': 'Reviews',
            'exception': "",
    }
    return render(request, 'reviews.html', context=context)




def vacancies(request):
    vacancies = Vacancy.objects.all()
    if not request.user.is_authenticated:
        return render(request, 'vacancies.html', {'vacancies': vacancies, 'title': 'Careers', 'menu': menu[0::2]})
    return render(request, 'vacancies.html', {'vacancies': vacancies, 'title': 'Careers', 'menu': menu})


def halls(request):
    halls = Hall.objects.all()
    hall_menu = menu[0::2] if not request.user.is_authenticated else menu
    cat_fact = requests.get('https://catfact.ninja/fact').json()
    context = {
        'halls': halls,
        'title': 'Halls',
        'menu': hall_menu,
        'cat_fact': cat_fact['fact']
    }

    return render(request, 'hall.html', context=context)


def cashiers(request):
    cashiers = Cashier.objects.all()
    context = {
        'cashiers': cashiers,
        'menu': menu,
        'title': 'Employees'
    }

    return render(request, 'cashiers.html', context=context)


# def login(request):
#     return HttpResponse("Sign In")


class ShowFilm(DataMixin, DetailView):
    model = Film
    template_name = 'film.html'
    pk_url_kwarg = 'film_id'
    context_object_name = 'film'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        g_def = self.get_user_context(title=context['film'], genre_selected=context['film'].genre_id, main_page=True)
        return dict(list(context.items()) + list(g_def.items()))


def news(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    context = {
        'news': news,
        'menu': menu,
        'title': news.title
    }
    return render(request, 'news.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')


class FilmGenre(DataMixin, ListView):
    model = Film
    template_name = 'index.html'
    context_object_name = 'films'
    allow_empty = False

    def get_queryset(self):
        return Film.objects.filter(genre__id=self.kwargs['genre_id'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        g_def = self.get_user_context(title="Genre - " + str(context['films'][0].genre),
                                      genre_selected=context['films'][0].genre_id,
                                      main_page=True)
        return dict(list(context.items()) + list(g_def.items()))


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        g_def = self.get_user_context(title="Registration")
        return dict(list(context.items()) + list(g_def.items()))

    def form_valid(self, form):
        user = form.save()
        client = Client(first_name=form.cleaned_data.get("first_name"),
                        last_name=form.cleaned_data.get("last_name"),
                        date_of_birth=form.cleaned_data.get("date_of_birth"),
                        email=form.cleaned_data.get("email"),
                        phone_number=form.cleaned_data.get("phone_number"))
        client.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        g_def = self.get_user_context(title="Authorization")
        return dict(list(context.items()) + list(g_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


@login_required
def show_tickets(request):
    user = CustomUser.objects.get(email=request.user.email)
    client = Client.objects.get(phone_number=user.phone_number)
    purchases = Purchase.objects.filter(client_id=client.id)
    amount_of_tickets = iter([purchase.amount_of_tickets for purchase in purchases])
    sessions_id = [purchase.session_id for purchase in purchases]
    sessions = [Session.objects.get(pk=ses_id).__str__().strip("00:00").strip("+") for ses_id in sessions_id]
    sessions = [ses + ", Tickets: " + str(next(amount_of_tickets)) for ses in sessions]
    for i in range(len(sessions)):
        sessions[i] = str(i+1) + ') ' + sessions[i]
    context = {
        'tickets': sessions,
        'title': 'Tickets',
        'menu': menu
    }
    return render(request, 'ticketinfo.html', context=context)


@login_required
def delete_tickets(request):
    exception = False
    if request.method == 'POST':
        form = DeleteTicketForm(request.POST)
        session_num = int(request.POST.get('session_number')) - 1
        user = CustomUser.objects.get(email=request.user.email)
        client = Client.objects.get(phone_number=user.phone_number)
        purchases = Purchase.objects.filter(client_id=client.id)
        if form.is_valid() and session_num <= len(purchases):
            try:
                purc_id = purchases[session_num].id
                seats = purchases[session_num].amount_of_tickets
                ses_id = purchases[session_num].session_id
                print(ses_id)
                Purchase.objects.get(id=purc_id).delete()
                ses = Session.objects.get(id=ses_id)
                print(ses.available_seats)
                ses.available_seats += seats
                ses.save()
                print(ses.available_seats)
            except:
                exception = True
    else:
        form = DeleteTicketForm()
    context = {
        'form': form,
        'menu': menu,
        'title': 'Ticket refund',
        'exception': exception
    }
    return render(request, 'deletetickets.html', context=context)


@login_required
def change_tickets(request):
    exception = False
    if request.method == 'POST':
        form = ChangeTicketForm(request.POST)
        session_num = int(request.POST.get('session_number')) - 1
        user = CustomUser.objects.get(email=request.user.email)
        client = Client.objects.get(phone_number=user.phone_number)
        purchases = Purchase.objects.filter(client_id=client.id)
        seats = purchases[session_num].amount_of_tickets
        new_seats = int(request.POST.get('seats'))
        if form.is_valid() and session_num <= len(purchases) and new_seats <= seats:
            try:
                purc_id = purchases[session_num].id
                ses_id = purchases[session_num].session_id
                purch = Purchase.objects.get(id=purc_id)
                purch.amount_of_tickets = new_seats
                purch.save()
                ses = Session.objects.get(id=ses_id)
                print(ses.available_seats)
                ses.available_seats += (seats - new_seats)
                ses.save()
                print(ses.available_seats)
            except:
                exception = True
        else:
            exception = True
    else:
        form = ChangeTicketForm()
    context = {
        'form': form,
        'menu': menu,
        'title': 'Ticket refund',
        'exception': exception
    }
    return render(request, 'changetickets.html', context=context)


def stat(request):
    if not request.user.is_superuser:
        raise PermissionDenied("You do not have access to this page.")

    all_groups = (((Purchase.objects
                  .annotate(month=TruncMonth('bought_at')))
                  .values('month'))
                  .annotate(c=Count('id')))
    print(all_groups)
    mon = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr',
           5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug',
           9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
    x = []
    y = []
    for group in all_groups:
        x.append(mon[group['month'].month])
        y.append(group['c'])
    context = {
        'menu': menu,
        'title': 'Stats'
    }
    plt.bar(x, y, color="aquamarine", width=0.1)
    print(x)
    print(Purchase.objects.all())
    plt.xlabel('Month')
    plt.ylabel('Amount of purchases')
    plt.title('Stats')
    plt.savefig('cinema/static/app_statistics/stats.png', format='png')
    return render(request, 'stats.html', context=context)