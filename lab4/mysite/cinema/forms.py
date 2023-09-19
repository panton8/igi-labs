from datetime import date

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from .models import *


def validate_age(value):
    today = date.today()
    age = today.year - value.year - int((today.month, today.day) < (value.month, value.day))
    print(today.year)
    print(value.year)
    print(age)
    if int(age) < 18:
        raise ValidationError("Restriction 18+")


class SortForm(forms.Form):
    sort_form = forms.TypedChoiceField(label='Sorting parameter',
                                       choices=[('Default', 'Default'),
                                                ('Price', 'By price'),
                                                ('Date', 'By date'),
                                                ('Hall', 'By hall')])


class TicketPostForm(forms.Form):
     session = forms.ModelChoiceField(queryset=Session.objects.all(), empty_label="Session not selected")
     seats = forms.IntegerField(min_value=1, max_value=5)
     code = forms.CharField(max_length=8, initial="NOSALE")


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    first_name = forms.CharField(max_length=100, label='First_name', widget=forms.TextInput(attrs={'class': 'form-input'}))
    last_name = forms.CharField(max_length=100, label='Last_name', widget=forms.TextInput(attrs={'class': 'form-input'}))
    date_of_birth = forms.DateField(validators=[validate_age], label='Birthday', widget=forms.DateInput(attrs={'class': 'form-input'}))
    phone_number = forms.CharField(max_length=50, label='Phone', widget=forms.TextInput(attrs={'class': 'form-input'}),
                                   validators=[RegexValidator(
                                       regex=r'^(\+375 \(29\) [0-9]{3}-[0-9]{2}-[0-9]{2})$',
                                       message='Format +375 (29) XXX-XX-XX',
                                   )])

    class Meta:
        model = CustomUser
        fields = ('username',
                  'email',
                  'first_name',
                  'last_name',
                  'date_of_birth',
                  'phone_number',
                  'password1',
                  'password2'
                  )

        widgets = {
            'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-input'})
        }


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class DeleteTicketForm(forms.Form):
    session_number = forms.IntegerField(min_value=1)


class ChangeTicketForm(forms.Form):
    session_number = forms.IntegerField(min_value=1)
    seats = forms.IntegerField(min_value=1)


class ReviewForm(forms.Form):
    content = forms.CharField(label="", widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Comment here !',
            'rows': 10,
            'cols': 50
        }))

    class Meta:
        model = Review
        fields = ['content']

    rating = forms.FloatField(min_value=1, max_value=10)