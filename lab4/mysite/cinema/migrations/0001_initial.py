# Generated by Django 4.2.1 on 2023-05-29 19:31

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cashier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(choices=[('United Kingdom', 'United Kingdom'), ('United States', 'United States'), ('China', 'China'), ('France', 'France'), ('Japan', 'Japan'), ('Germany', 'Germany'), ('Canada', 'Canada'), ('India', 'India'), ('Russia', 'Russia'), ('Turkey', 'Turkey'), ('Italy', 'Italy'), ('Spain', 'Spain')], max_length=14)),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('duration', models.PositiveIntegerField(help_text='duration(minutes)', validators=[django.core.validators.MinValueValidator(45), django.core.validators.MaxValueValidator(240)])),
                ('budget', models.FloatField()),
                ('poster', models.ImageField(upload_to='photos/')),
                ('description', models.TextField()),
                ('rating', models.FloatField(help_text='from 1.0 to 10.0', validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(10.0)])),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cinema.country')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(choices=[('Action', 'Action'), ('Adventure', 'Adventure'), ('Comedy', 'Comedy'), ('Crime', 'Crime'), ('Drama', 'Drama'), ('Historical', 'Historical'), ('Horror', 'Horror'), ('Musicals', 'Musicals'), ('Science', 'Science'), ('War', 'War'), ('Western', 'Western'), ('Documentary', 'Documentary')], max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('capacity', models.PositiveIntegerField(default=150, validators=[django.core.validators.MinValueValidator(50), django.core.validators.MaxValueValidator(800)])),
                ('available_seats', models.IntegerField(default=models.PositiveIntegerField(default=150, validators=[django.core.validators.MinValueValidator(50), django.core.validators.MaxValueValidator(800)]), validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(models.PositiveIntegerField(default=150, validators=[django.core.validators.MinValueValidator(50), django.core.validators.MaxValueValidator(800)]))])),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_cost', models.PositiveIntegerField(default=8)),
                ('date', models.DateTimeField()),
                ('cashier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema.cashier')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema.film')),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema.hall')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bought_at', models.DateTimeField(auto_now_add=True, help_text='Date and time when ticket was bought')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cinema.session')),
            ],
        ),
        migrations.AddField(
            model_name='hall',
            name='cashiers',
            field=models.ManyToManyField(through='cinema.Session', to='cinema.cashier'),
        ),
        migrations.AddField(
            model_name='film',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cinema.genre'),
        ),
    ]
