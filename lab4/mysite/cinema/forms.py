from django import forms
from .models import Film
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(forms.Form):
    user_name = forms.CharField(min_length=5, max_length=20)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())


class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = "__all__"
