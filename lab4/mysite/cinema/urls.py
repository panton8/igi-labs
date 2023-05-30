from django.urls import path

from .views import *

urlpatterns = [
    path('', home_screen_view, name='home'),
    path('films', films_view, name="film"),
    path('films/<int:hall_id>/', films_view),
    path('halls', halls_view, name='hall'),
    path('halls/<int:hall_id>/', halls_view),
    path('register/', sign_up, name='signup'),
]
