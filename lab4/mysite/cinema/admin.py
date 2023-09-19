from django.contrib import admin
from .models import *
from django.contrib.auth import get_user_model

# Register your models here.
admin.site.register(Country)
admin.site.register(Genre)
User = get_user_model()
admin.site.register(User)



@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'genre', 'duration', 'budget', 'poster', 'description', 'rating')
    list_display_links = ('name',)
    search_fields = ('name',)
    ordering = ['-rating']
    list_editable = ('rating',)
    list_filter = ('country', 'genre')


@admin.register(Cashier)
class CashierAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'photo')


@admin.register(Hall)
class HallAdmin(admin.ModelAdmin):
    list_display = ('name', 'photo', 'capacity')
    ordering = ['-capacity']


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('film', 'hall', 'ticket_cost', 'cashier', 'date')


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'email', 'phone_number')



@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('client', 'session', 'bought_at', 'updated_at')


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('position', 'requirements', 'salary')


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('publish', 'title', 'text', "photo")


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', 'rating', 'pub_date')


@admin.register(SaleCode)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('code', )
