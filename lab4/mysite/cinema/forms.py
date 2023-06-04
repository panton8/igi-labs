from django import forms
from .models import *


class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = "__all__"


class TicketPostForm(forms.Form):
    class Meta:
        model = Session
        fields = "__all__"
        widgets = {
            "Film": forms.Form
        }
    session = forms.ModelChoiceField(queryset=Session.objects.all())
    seats = forms.IntegerField(min_value=1, max_value=5)
