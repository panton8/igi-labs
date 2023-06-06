from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from cinema.manager import CustomUserManager


class Genre(models.Model):
    ACTION = "Action"
    ADVENTURE = "Adventure"
    COMEDY = "Comedy"
    CRIME = "Crime"
    DRAMA = "Drama"
    HISTORICAL = "Historical"
    HORROR = "Horror"
    MUSICALS = "Musicals"
    SCIENCE = "Science"
    WAR = "War"
    WESTERN = "Western"
    DOCUMENTARY = "Documentary"

    GENRES = [
        (ACTION, "Action"),
        (ADVENTURE, "Adventure"),
        (COMEDY, "Comedy"),
        (CRIME, "Crime"),
        (DRAMA, "Drama"),
        (HISTORICAL, "Historical"),
        (HORROR, "Horror"),
        (MUSICALS, "Musicals"),
        (SCIENCE, "Science"),
        (WAR, "War"),
        (WESTERN, "Western"),
        (DOCUMENTARY, "Documentary")
    ]

    genre = models.CharField(max_length=11, choices=GENRES)

    def __str__(self):
        return f'{self.genre}'

    def get_absolute_url(self):
        return reverse('genre', kwargs={'genre_id': self.pk})


class Country(models.Model):
    US = "United Kingdom"
    UK = "United States"
    CHINA = "China"
    FRANCE = "France"
    JAPAN = "Japan"
    GERMANY = "Germany"
    CANADA = "Canada"
    INDIA = "India"
    RUSSIA = "Russia"
    TURKEY = "Turkey"
    ITALY = "Italy"
    SPAIN = "Spain"

    COUNTRIES = [
        (US, "United Kingdom"),
        (UK, "United States"),
        (CHINA, "China"),
        (FRANCE, "France"),
        (JAPAN, "Japan"),
        (GERMANY, "Germany"),
        (CANADA, "Canada"),
        (INDIA, "India"),
        (RUSSIA, "Russia"),
        (TURKEY, "Turkey"),
        (ITALY, "Italy"),
        (SPAIN, "Spain")
    ]

    country = models.CharField(max_length=14, choices=COUNTRIES)

    def __str__(self):
        return self.country


class Cashier(models.Model):
    full_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="photos/cashiers")

    def __str__(self):
        return self.full_name


class Film(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT)
    duration = models.PositiveIntegerField(validators=[MinValueValidator(45), MaxValueValidator(240)], help_text="duration(minutes)")
    budget = models.FloatField()
    poster = models.ImageField(upload_to="photos/films")
    description = models.TextField(blank=False)
    rating = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(10.0)], help_text="from 1.0 to 10.0")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('film', kwargs={'film_id': self.pk})


class Hall(models.Model):
    name = models.CharField(max_length=30)
    photo = models.ImageField(upload_to="photos/halls")
    capacity = models.IntegerField(validators=[MinValueValidator(50), MaxValueValidator(800)])
    cashiers = models.ManyToManyField(Cashier, through="Session")

    def __str__(self):
        return f"{self.name[-3:]}"


class Session(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    available_seats = models.IntegerField(validators=[MinValueValidator(0)])
    ticket_cost = models.PositiveIntegerField(default=8)
    cashier = models.ForeignKey(Cashier, on_delete=models.CASCADE)
    date = models.DateTimeField()

    def __str__(self):
        return f"Film: {self.film}," \
               f" Hall: {self.hall}," \
               f" Ticket Cost: {self.ticket_cost}," \
               f" Date: {self.date},"\
               f" Seats available: {self.available_seats}"


class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name}  {self.last_name}"


class Purchase(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.PROTECT)
    bought_at = models.DateTimeField(auto_now_add=True, help_text='Date and time when ticket was bought')
    updated_at = models.DateTimeField(help_text='Date and time when ticket was updated')
    amount_of_tickets = models.IntegerField(default=1)


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=200,
                                  help_text='Enter first name')
    last_name = models.CharField(max_length=200,
                                 help_text='Enter last name')
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=50)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name',
                       'last_name',
                       'email',
                       'date_of_birth',
                       'phone_number']
