from .models import *

menu = [
    {'title': "Main", 'url_name': 'main'},
    {'title': "Buy tickets", 'url_name': 'buy_ticket'},
    {'title': "About", 'url_name': 'about'},
    {'title': "Employees", 'url_name': 'cashiers'},
    #{'title': "Halls", 'url_name': 'halls'},
    {'title': "Tickets", 'url_name': 'tickets'},
    #{'title': "Privacy Policy", 'url_name': 'privacy_policy'},
    {'title': 'Reviews', 'url_name': 'reviews'},
    #{'title': "Careers", 'url_name': 'vacancies'},
    {'title': "Questions", 'url_name': 'questions'},
    {'title': "News", 'url_name': 'list_news'},
    {'title': "Stats", 'url_name': 'stat'}
]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        genres = Genre.objects.all()

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)
            user_menu.pop(2)
            user_menu.pop(2)
        context['menu'] = user_menu
        context['genres'] = genres
        if 'genre_selected' not in context:
            context['genre_selected'] = 0
        if 'main_page' not in context:
            context['main_page'] = False
        return context