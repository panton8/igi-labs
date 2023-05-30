from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


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

    def __str__(self):
        return self.full_name


class Film(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT)
    duration = models.PositiveIntegerField(validators=[MinValueValidator(45), MaxValueValidator(240)], help_text="duration(minutes)")
    budget = models.FloatField()
    poster = models.ImageField(upload_to="photos/")
    description = models.TextField(blank=False)
    rating = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(10.0)], help_text="from 1.0 to 10.0")

    def __str__(self):
        return f'Film info:\n' \
               f'Title: {self.name}\n' \
               f'Country of production: {self.country}\n' \
               f'Genre: {self.genre}\n' \
               f'Running Time: {self.duration}\n' \
               f'Budget: {self.budget}\n' \
               f'Rating: {self.rating}'


class Hall(models.Model):
    name = models.CharField(max_length=30)
    capacity = models.PositiveIntegerField(default=150, validators=[MinValueValidator(50), MaxValueValidator(800)])
    available_seats = models.IntegerField(default=capacity, validators=[MinValueValidator(0), MaxValueValidator(capacity)])
    cashiers = models.ManyToManyField(Cashier, through="Session")

    def __str__(self):
        return f"Hall Info:\n" \
               f"Name: {self.name}\n" \
               f"Capacity: {self.capacity}"


class Session(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    ticket_cost = models.PositiveIntegerField(default=8)
    cashier = models.ForeignKey(Cashier, on_delete=models.CASCADE)
    date = models.DateTimeField()

    def __str__(self):
        return f"Film: {self.film}\n" \
               f"Hall: {self.hall}\n" \
               f"Ticket Cost: {self.ticket_cost}\n" \
               f"Date: {self.date}"


class Purchase(models.Model):
    session = models.ForeignKey(Session, on_delete=models.PROTECT)
    bought_at = models.DateTimeField(auto_now_add=True, help_text='Date and time when ticket was bought')