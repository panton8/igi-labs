from .models import *

menu = [
    {'title': "About", 'url_name': 'about'},
    {'title': "Buy tickets", 'url_name': 'buy_ticket'},
    {'title': "Halls", 'url_name': 'halls'},
    {'title': "Employees", 'url_name': 'cashiers'},
    {'title': "Tickets", 'url_name': 'tickets'}
]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        genres = Genre.objects.all()

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)
            user_menu.pop(2)
        context['menu'] = user_menu
        context['genres'] = genres
        if 'genre_selected' not in context:
            context['genre_selected'] = 0
        if 'main_page' not in context:
            context['main_page'] = False
        return context