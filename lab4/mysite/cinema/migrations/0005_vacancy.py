# Generated by Django 4.2.1 on 2023-09-10 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0004_cashier_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(default='cashier', max_length=50)),
                ('requirements', models.CharField(default='higher education', max_length=500)),
                ('salary', models.FloatField(default=500)),
            ],
        ),
    ]