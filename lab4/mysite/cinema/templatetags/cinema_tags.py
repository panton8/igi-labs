from django import template
from cinema.models import *

register = template.Library()


@register.simple_tag()
def get_genres(filter=None):
    if not filter:
        return Genre.objects.all()
    else:
        return Genre.objects.filter(pk=filter)


@register.inclusion_tag('list_genres.html')
def show_genres(sort=None, genre_selected=0):
    if not sort:
        genres = Genre.objects.all()
    else:
        genres = Genre.objects.order_by(sort)

    return {"genres": genres, "genre_selected": genre_selected}